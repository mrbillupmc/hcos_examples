package com.upmc.enterprises.hcos;

import java.io.IOException;

import com.squareup.okhttp.Interceptor;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.Response;

public class HeaderInterceptor implements Interceptor {

  private String acceptHeaderValue;

  @Override
  public Response intercept(Chain chain) throws IOException {
    Request original = chain.request();
    // Request customization: add request headers
    Request.Builder requestBuilder = original.newBuilder().header("Accept", acceptHeaderValue);
    Request request = requestBuilder.build();
    return chain.proceed(request);
  }

  public String getAcceptHeaderValue() {
    return acceptHeaderValue;
  }

  public void setAcceptHeaderValue(String acceptHeaderValue) {
    this.acceptHeaderValue = acceptHeaderValue;
  }

}
