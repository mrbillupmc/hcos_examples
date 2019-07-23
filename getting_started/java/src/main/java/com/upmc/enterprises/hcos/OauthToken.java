package com.upmc.enterprises.hcos;

import java.util.Date;

import com.google.gson.annotations.SerializedName;

public class OauthToken {

  @SerializedName("access_token")
  private String accessToken;
  @SerializedName("expires_in")
  private int expiresIn;
  @SerializedName("token_type")
  private String tokenType;

  private Date lastUpdated;

  public String getAccessToken() {
    return accessToken;
  }

  public void setAccessToken(String accessToken) {
    this.accessToken = accessToken;
  }

  public int getExpiresIn() {
    return expiresIn;
  }

  public void setExpiresIn(int expiresIn) {
    this.expiresIn = expiresIn;
  }

  public Date getLastUpdated() {
    return lastUpdated;
  }

  public void setLastUpdated(Date lastUpdated) {
    this.lastUpdated = lastUpdated;
  }

  public String getTokenType() {
    return tokenType;
  }

  public void setTokenType(String tokenType) {
    this.tokenType = tokenType;
  }

  public boolean isExpired() {
    boolean isExpired = true;
    if (lastUpdated != null) {
      Date now = new Date();
      if (((now.getTime() - lastUpdated.getTime()) / 1000) < expiresIn) {
        isExpired = false;
      }
    }
    return isExpired;
  }

}
