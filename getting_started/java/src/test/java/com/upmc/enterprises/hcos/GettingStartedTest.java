package com.upmc.enterprises.hcos;

import static org.junit.Assert.assertNotNull;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Map;

import org.junit.BeforeClass;
import org.junit.Test;

import com.google.gson.Gson;
import com.google.gson.JsonIOException;
import com.google.gson.JsonSyntaxException;
import com.google.gson.reflect.TypeToken;
import com.upmc.enterprises.hcos.model.DocumentMeta;
import com.upmc.enterprises.hcos.model.SearchCriterion;
import com.upmc.enterprises.hcos.model.SearchResult;

public class GettingStartedTest {

  private static String basePath;
  private static String oauthBaseUrl;
  private static String clientId;
  private static String clientSecret;
  private static String tenantId;

  @BeforeClass
  public static void oneTimeSetUp() throws IOException {
    // one-time initialization code
    Gson gson = new Gson();
    Type mapType = new TypeToken<Map<String, String>>() {}.getType();
    Map<String, String> map =
        gson.fromJson(new FileReader("../configurations/Configuration.json"), mapType);

    basePath = map.get("baseUrl");
    oauthBaseUrl = map.get("oauthBaseUrl");
    clientId = map.get("clientId");
    clientSecret = map.get("clientSecret");
    tenantId = map.get("tenantId");
  }

  @Test
  public void runDemo() throws JsonIOException, JsonSyntaxException, FileNotFoundException {
    System.out.println("Getting Started demo begins...");
    Gson gson = new Gson();
    Type searchType = new TypeToken<List<Search>>() {}.getType();
    List<Search> list = gson.fromJson(new FileReader("../Searches.json"), searchType);
    System.out.println("search list size=[" + list.size() + "]");
    for (Search search : list) {
      System.out.println("search=[" + search + "]");
      GettingStarted client = new GettingStarted();
      client.setBasePath(basePath);
      client.setOauthPassword(clientSecret);
      client.setOauthUrl(oauthBaseUrl);
      client.setOauthUsername(clientId);
      client.setVerifyingSsl(true);
      client.setDebugging(false);
      SearchCriterion body = new SearchCriterion();
      body.setCriterion(search.getQuery().get("criterion"));
      SearchResult searchResult = client.postSearchByKDSL(body, tenantId);
      // System.out.println("searchResult=[" + searchResult + "]");
      assertNotNull(searchResult);
      System.out.println("offset=[" + searchResult.getOffset() + "]");
      System.out.println("record_count=[" + searchResult.getRecordCount() + "]");
      System.out.println("total_record_count=[" + searchResult.getTotalRecordCount() + "]");
      List<DocumentMeta> hits = searchResult.getHits();
      int i = 1;
      for (DocumentMeta hit : hits) {
        DocumentMeta meta = client.getDocumentByRootExtension(tenantId, hit.getDocumentRoot(),
            hit.getDocumentExtension(), "text/plain");
        // System.out.println("meta=[" + meta + "]");
        System.out.println("\t" + i + "\tdocument_root=[" + meta.getDocumentRoot() + "]");
        System.out.println("\t\tdocument_extension=[" + meta.getDocumentExtension() + "]");
        System.out
            .println("\t\tdocument_type-description=[" + meta.getDocumentTypeDescription() + "]");
        i++;
      }
    }
    System.out.println("Getting Started demo ends.");
  }
  
}
