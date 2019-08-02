package com.upmc.enterprises.hcos;

import java.io.IOException;
import java.util.Date;
import java.util.Map;
import java.util.UUID;

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
  private String oauthBaseUrl;
  private String clientId;
  private String clientSecret;
  private boolean debugging = false;
  private boolean verifyingSsl = true;

  private ApiClient apiClient;
  SearchApi searchApi;
  DocumentApi documentApi;

  public GettingStarted(
          String basePath,
          String clientId,
          String clientSecret,
          String oauthBaseUrl,
          Boolean verifyingSsl,
          Boolean debugging) {
    this.basePath = basePath;
    this.clientId = clientId;
    this.clientSecret = clientSecret;
    this.oauthBaseUrl  = oauthBaseUrl;
    this.verifyingSsl = verifyingSsl;
    this.debugging = debugging;

    apiClient = new ApiClient();
    apiClient.setBasePath(basePath);
    apiClient.setVerifyingSsl(verifyingSsl);

    apiClient.setDebugging(debugging);
    apiClient.setConnectTimeout(0);
    apiClient.setReadTimeout(0);

    searchApi = new SearchApi(apiClient=apiClient);
    documentApi = new DocumentApi(apiClient=apiClient);
  }

  public SearchResult postSearchByKDSL(UUID correlationId, String userRoot, String userExtension, SearchCriterion body, String tenantId) {
    SearchResult searchResult = null;
    if (tenantId != null && tenantId.trim().length() > 0 && body != null) {
      String token = null;
      try {
        token = getToken();
      } catch (IOException e1) {
        e1.printStackTrace();
      }
      if (token != null) {
        try {
          searchApi.getApiClient().setAccessToken(token);
          searchResult = searchApi.postSearchByKDSL(body, correlationId.toString(), userRoot, userExtension, tenantId, null, null, null);
        } catch (Exception e) {
          e.printStackTrace();
        }
      }
    }
    return searchResult;
  }

  public DocumentMeta getDocumentByRootExtension(UUID correlationId, String userRoot, String userExtension, String tenantId, String documentRoot,
    String documentExtension, String acceptHeaderValue) {
    DocumentMeta meta = null;
    String token = null;
    try {
      token = getToken();
    } catch (IOException e1) {
      e1.printStackTrace();
    }
    if (token != null) {
      if (acceptHeaderValue != null && acceptHeaderValue.length() > 0) {
        HeaderInterceptor interceptor = new HeaderInterceptor();
        interceptor.setAcceptHeaderValue(acceptHeaderValue);
        documentApi.getApiClient().setAccessToken(token);
        documentApi.getApiClient().getHttpClient().interceptors().add(interceptor);
      }
      try {
        meta = documentApi.getDocumentByRootExtension(correlationId.toString(), userRoot, userExtension, tenantId, documentRoot, documentExtension);
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
      HttpUrl.Builder urlBuilder = HttpUrl.parse(oauthBaseUrl + "/oauth2/token").newBuilder();
      urlBuilder.addQueryParameter("grant_type", "client_credentials").addQueryParameter("scope",
          "");
      String url = urlBuilder.build().toString();
      String postBody = "";
      Request request = new Request.Builder().url(url)
          .addHeader("Content-Type", "application/x-www-form-urlencoded")
          .addHeader("Authorization", Credentials.basic(clientId, clientSecret))
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
}
