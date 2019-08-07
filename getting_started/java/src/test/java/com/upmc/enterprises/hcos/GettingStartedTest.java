package com.upmc.enterprises.hcos;

import static org.junit.Assert.assertNotNull;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.List;
import java.util.Map;
import java.util.UUID;

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
  private static UUID correlationId;
  private static String userRoot;
  private static String userExtension;

  @BeforeClass
  public static void initialize() throws IOException {
    Gson gson = new Gson();
    Type mapType = new TypeToken<Map<String, String>>() {}.getType();
    Map<String, String> map =
        gson.fromJson(new FileReader("../configurations/Configuration.json"), mapType);

    basePath = map.get("basePath");
    oauthBaseUrl = map.get("oauthBaseUrl");
    clientId = map.get("clientId");
    clientSecret = map.get("clientSecret");
    tenantId = map.get("tenantId");

    // TODO : add headers to calls
    correlationId = UUID.randomUUID();
    userRoot = "hcos.upmce.net";
    userExtension = "username";
  }

  @Test
  public void demo() throws JsonIOException, JsonSyntaxException, FileNotFoundException {
    System.out.println("Getting Started demo begins...");

    Gson gson = new Gson();
    Type searchType = new TypeToken<List<Search>>() {}.getType();
    List<Search> searchExamples = gson.fromJson(new FileReader("../Searches.json"), searchType);
    Search searchExample = searchExamples.get(0);

    System.out.println(searchExample.getDescription());

    GettingStarted demo =
        new GettingStarted(basePath, clientId, clientSecret, oauthBaseUrl, true, false);

    SearchCriterion body = new SearchCriterion();
    body.setCriterion(searchExample.getQuery().get("criterion"));

    SearchResult searchResult =
        demo.postSearchByKDSL(correlationId, userRoot, userExtension, body, tenantId);
    assertNotNull(searchResult);
    System.out.println("offset: " + searchResult.getOffset());
    System.out.println("record_count:" + searchResult.getRecordCount());
    System.out.println("total_record_count:" + searchResult.getTotalRecordCount());

    int index = 0;
    for (DocumentMeta searchHit : searchResult.getHits()) {
      System.out.println("" + index + " " + searchHit.getDocumentRoot() + "-"
          + searchHit.getDocumentExtension() + "-" + searchHit.getDocumentTypeExtension());

      DocumentMeta documentMetaData =
          demo.getDocumentByRootExtension(correlationId, userRoot, userExtension, tenantId,
              searchHit.getDocumentRoot(), searchHit.getDocumentExtension(), "text/plain");
      System.out.println("\tdocument_root: " + documentMetaData.getDocumentRoot());
      System.out.println("\tdocument_extension: " + documentMetaData.getDocumentExtension());
      System.out
          .println("\tdocument_type-description: " + documentMetaData.getDocumentTypeDescription());
      index++;
    }
    System.out.println("Getting Started demo ends.");
  }
}
