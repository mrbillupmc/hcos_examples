package com.upmc.enterprises.hcos;

import java.util.Map;

public class Search {

  private String description;
  private Map<String, String> query;

  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  public Map<String, String> getQuery() {
    return query;
  }

  public void setQuery(Map<String, String> query) {
    this.query = query;
  }

  @Override
  public String toString() {
    return "Search [description=" + description + ", query=" + query + "]";
  }

}
