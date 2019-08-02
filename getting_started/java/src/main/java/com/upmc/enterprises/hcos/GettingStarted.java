package com.upmc.enterprises.hcos;

import java.io.IOException;
import java.util.Date;
import java.util.Map;

import com.auth0.jwt.JWT;
import com.auth0.jwt.exceptions.JWTDecodeException;
import com.auth0.jwt.interfaces.Claim;
import com.auth0.jwt.interfaces.DecodedJWT;
import com.google.gson.Gson;
import com.squareup.okhttp.Call;
import com.squareup.okhttp.Credentials;
import com.squareup.okhttp.HttpUrl;
import com.squareup.okhttp.MediaType;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;
import com.squareup.okhttp.logging.HttpLoggingInterceptor;
import com.squareup.okhttp.logging.HttpLoggingInterceptor.Level;
import com.upmc.enterprises.hcos.api.DocumentApi;
import com.upmc.enterprises.hcos.api.SearchApi;
import com.upmc.enterprises.hcos.model.DocumentMeta;
import com.upmc.enterprises.hcos.model.SearchCriterion;
import com.upmc.enterprises.hcos.model.SearchResult;

public class GettingStarted {

  private OauthToken oauthToken;

  private String basePath;
  private String oauthUrl;
  private String oauthUsername;
  private String oauthPassword;
  private boolean debugging = false;
  private boolean verifyingSsl = true;

  public SearchResult postSearchByKDSL(SearchCriterion body, String tenantId) {
    SearchResult searchResult = null;
    if (tenantId != null && tenantId.trim().length() > 0 && body != null) {
      String token = null;
      try {
        token = getToken();
      } catch (IOException e1) {
        e1.printStackTrace();
      }
      if (token != null) {
        SearchApi client = new SearchApi();
        client.getApiClient().setDebugging(debugging);
        client.getApiClient().setVerifyingSsl(verifyingSsl);
        client.getApiClient().setBasePath(basePath);
        client.getApiClient().setAccessToken(token);
        client.getApiClient().setConnectTimeout(0);
        client.getApiClient().setReadTimeout(0);
        try {
          searchResult = client.postSearchByKDSL(body, "correlationId", "xHcosUserRoot",
              "xHcosUserExtension", tenantId, null, null, null);
        } catch (Exception e) {
          e.printStackTrace();
        }
      }
    }
    return searchResult;
  }

  public DocumentMeta getDocumentByRootExtension(String tenantId, String documentRoot,
      String documentExtension, String acceptHeaderValue) {
    DocumentMeta meta = null;
    String token = null;
    try {
      token = getToken();
    } catch (IOException e1) {
      e1.printStackTrace();
    }
    if (token != null) {
      DocumentApi client = new DocumentApi();
      if (acceptHeaderValue != null && acceptHeaderValue.length() > 0) {
        HeaderInterceptor interceptor = new HeaderInterceptor();
        interceptor.setAcceptHeaderValue(acceptHeaderValue);
        client.getApiClient().getHttpClient().interceptors().add(interceptor);
      }
      client.getApiClient().setDebugging(debugging);
      client.getApiClient().setVerifyingSsl(verifyingSsl);
      client.getApiClient().setBasePath(basePath);
      client.getApiClient().setAccessToken(token);
      client.getApiClient().setConnectTimeout(0);
      client.getApiClient().setReadTimeout(0);
      try {
        meta = client.getDocumentByRootExtension("xCorrelationId", "xHcosUserRoot",
            "xHcosUserExtension", tenantId, documentRoot, documentExtension);
      } catch (Exception e) {
        e.printStackTrace();
      }
    }
    return meta;
  }

  private String getToken() throws IOException {
    String token = null;
    if (oauthToken != null && !oauthToken.isExpired()) {
      token = oauthToken.getAccessToken();
    } else {
      OkHttpClient client = new OkHttpClient();
      if (debugging) {
        HttpLoggingInterceptor loggingInterceptor = new HttpLoggingInterceptor();
        loggingInterceptor.setLevel(Level.BODY);
        client.interceptors().add(loggingInterceptor);
      }
      HttpUrl.Builder urlBuilder = HttpUrl.parse(oauthUrl + "/oauth2/token").newBuilder();
      urlBuilder.addQueryParameter("grant_type", "client_credentials").addQueryParameter("scope",
          "");
      String url = urlBuilder.build().toString();
      String postBody = "";
      Request request = new Request.Builder().url(url)
          .addHeader("Content-Type", "application/x-www-form-urlencoded")
          .addHeader("Authorization", Credentials.basic(oauthUsername, oauthPassword))
          .post(RequestBody.create(
              MediaType.parse("application/x-www-form-urlencoded; charset=utf-8"), postBody))
          .build();

      Call call = client.newCall(request);
      Response response = call.execute();

      String json = response.body().string();
      Gson gson = new Gson();
      oauthToken = gson.fromJson(json, OauthToken.class);
      oauthToken.setLastUpdated(new Date());
      token = oauthToken.getAccessToken();
      // If you need to investigate the token you can use the auth0 library.
      if (debugging) {
        try {
          DecodedJWT jwt = JWT.decode(token);
          Map<String, Claim> claims = jwt.getClaims();
          for (String name : claims.keySet()) {
            System.out.println("claim=[" + name + "], value=[" + claims.get(name).asString() + "]");
          }
        } catch (JWTDecodeException exception) {
          exception.printStackTrace();
        }
      }
    }
    return token;
  }

  public OauthToken getOauthToken() {
    return oauthToken;
  }

  public void setOauthToken(OauthToken oauthToken) {
    this.oauthToken = oauthToken;
  }

  public String getBasePath() {
    return basePath;
  }

  public void setBasePath(String basePath) {
    this.basePath = basePath;
  }

  public String getOauthUrl() {
    return oauthUrl;
  }

  public void setOauthUrl(String oauthUrl) {
    this.oauthUrl = oauthUrl;
  }

  public String getOauthUsername() {
    return oauthUsername;
  }

  public void setOauthUsername(String oauthUsername) {
    this.oauthUsername = oauthUsername;
  }

  public String getOauthPassword() {
    return oauthPassword;
  }

  public void setOauthPassword(String oauthPassword) {
    this.oauthPassword = oauthPassword;
  }

  public boolean isDebugging() {
    return debugging;
  }

  public void setDebugging(boolean debugging) {
    this.debugging = debugging;
  }

  public boolean isVerifyingSsl() {
    return verifyingSsl;
  }

  public void setVerifyingSsl(boolean verifyingSsl) {
    this.verifyingSsl = verifyingSsl;
  }
}
