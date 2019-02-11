# Getting started with hcOS in 9 min or less. (Python edition)

## hcOS

hcOS (“Healthcare Operating System”) is a web-based software platform under development at UPMC. The hcOS platform makes it easy for app developers to build software solutions that access clinical data and clinical systems. Using hcOS you can build a variety of healthcare applications for clinicians, patients or healthcare administrators. You can learn more about hcOS at [https://enterprises.upmc.com/portfolio/hcos/](https://enterprises.upmc.com/portfolio/hcos/)

## Prerequisites

These examples are written in [python3](https://www.python.org/download/releases/3.0/) using [virtualenv](https://virtualenv.pypa.io/en/latest/). You'll also need to have [git](https://git-scm.com/) installed and be familiar with [GitHub Forking](https://guides.github.com/activities/forking/). Instructions on development environment setup and configuration can be found [here](Setup.md).

## Introduction

This example demonstrates everything you need to know in order to get started developing with hcOS in **9 minutes** or less. We'll use our access keys to retrieve Oauth2 tokens, search hcOS Documents, and retrieve hcOS Documents that are part of the search result set. Topics include:

* [Load hcOS API configurations](#load-hcos-api-configurations)
* [Retrieve Oauth2 Tokens](#retrieve-oauth2-tokens)
* [hcOS Client Setup](#hcos-client-setup)
* [Search hcOS](#search-hcos)
* [Process hcOS Search Results](#process-hcos-search-results)
* [Retrieve hcOS Documents](#retrieve-hcos-documents)

The hcOS Search APIs are extremely powerful and support a wide variety [search use cases](../Searches.json). You can view the completed [GettingStarted.py](GettingStarted.py) if you'd like to skip ahead to the end.

## Load hcOS API configurations

Your hcOS [configuration file](../configurations/Configuration.sample.json) will contain the following information:

* name - name of the configuration in the file (Note: not necessary to call hcOS APIs)
* baseUrl - the base url of hcOS APIs e.g. api.hcos.upmc.com
* clientId - your application specific client id
* clientSecret - your application specific secret
* tokenUrl - Oauth2 token url
* tenantId - The ID of the hcOS tenant your application is authorized to use

```JSON
{
    "name" : "Configuration Name",
    "baseUrl" : "https://hostname",
    "clientId":"oauth2 client id",
    "clientSecret": "oauth2 secret",
    "tokenUrl": "oauth2 token url",
    "tenantId" : "A tenant id"
}
```

Note: The hcOS Search and Document APIs are secured behind a cryptography standard known as [Oauth2 Client Credentials](https://oauth.net/2/grant-types/client-credentials/).

In general, your application pseudo will look something like:

```python
# load api configuration
# use your client id and client secret to retrieve an oauth2 token
# call hcOS APIs
# process hcOS API results
```

### Loading hcOS Configurations

We typically store the API configurations in files (or environment variables) so we can automate deployments across environments. Here, we load both hcOS Search API and hcOS Document API configurations because our [app](./python/GettingStarted.py) will both search for documents and retrieve the documents which are part of the result set. Since our configuration is stored in json files, loading the configuration is as simple as:

```python
with open('../configurations/Configuration.json') as f:
    config = json.load(f)
```

Once loaded, we can store the configuration parameters as variables for use throughout the program.

```python
base_url = config['baseUrl']
client_id = config['clientId']
client_secret = config['clientSecret']
token_url = os.path.join(config['oauthBaseUrl'], 'oauth2/token')
tenant_id = config['tenantId']
```

### Request specific configuration

hcOS APIs also require that you specificy information related to the end user making the request. Sometimes this is a person, other times this is your application server. Regardless, these fields must be populated:

* hcos_user_root - the user domain e.g. hcos.upmce.net
* hcos_user_extension - the user name e.g. doej

```python
hcos_user_root = 'hcos.upmce.net'
hcos_user_extension = 'username'
```

### Correlation ID

A correlation ID can be specified if your application makes a series of calls to hcOS for a single task. An example might be that a user searches for a result set and then retrieves documents (as shown in this example). Using the same correlation ID across all requests aids in the ability to debug issues if they arise.

```python
x_correlation_id = str(uuid.uuid4())
```

## Retrieve Oauth2 Tokens

Since Oauth2 is a widely adopted standard we are able to pick from a variety of 3rd party libraries. In this example we use the following python packages:

* `requests` for issuing web requests
* `oauthlib.oauth2` for providing Oauth2 support
* `requests_oauthlib` for integration of Oauth2 and requests

These packages can be imported as follows:

```python
import requests
from oauthlib.oauth2 import BackendApplicationClient, TokenExpiredError
from requests_oauthlib import OAuth2, OAuth2Session
```

Once imported an Oauth2 token can be retrieved by using the `client_id`, `client_secret`, and `token_url`. Since we'll periodically refresh the token when it expires, we define a utility function.

```python
def refresh_token(client_id, client_secret, token_url):
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(
        token_url=token_url,
        client_id=client_id,
        client_secret=client_secret
    )
    return token
```

Now that the helper function has been created, you can retrieve your Oauth2 token.

```python
token = refresh_token(client_id, client_secret, token_url)
```

## hcOS Client Setup

Since the hcOS API is compliant with the [Open API 3](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md) specification, you are able to generate hcOS client libraries in nearly any programming language of your choice. This examnple uses python and includes a generated python client. You can import the python hcOS client as follows:

```python
import hcos_client
```

Once imported you'll create an api client configuration

```python
configuration = hcos_client.Configuration()
configuration.host = base_url
configuration.access_token = token['access_token']
```

and initialize the api client by passing in your configuration

```python
api_client = hcos_client.api_client.ApiClient(configuration=configuration)
```

API clients allow you to call any of the hcOS APIs.

## Search hcOS

Using the API Client you'll create a Search API object to issue the search

```python
search_api = hcos_client.api.search_api.SearchApi(api_client=api_client)
```

The hcOS Search API supports a wide range of free text and structured query parameters. Some examples can be found [here](../Searches.json). Here, we'll take a single query from the collection to use as an example. This query searches over all clinical documents within your hcOS tenant for the literal text 'ulcerative colitis'.

```python
query = { "criterion": "literal='ulcerative colitis'" }
```

and use the hcOS Search API to issue the request

```python
search_response = search_api.post_search_by_kdsl(
                body=query,
                x_correlation_id=x_correlation_id,
                hcos_user_root=hcos_user_root,
                hcos_user_extension=hcos_user_extension,
                tenant_id=tenant_id)
```

## Process hcOS Search Results

The hcOS Search API returns results contained within a json object. The field ```hits``` contains an array of the results. In python we can ```enumerate``` over these results getting an ```index``` and ```search_entry``` object that contains each item in the array.

```python
# iterate over the results and retrieve documents
for index, search_entry in enumerate(search_response.hits):
    print(f"{index} {search_entry.document_root}-{search_entry.document_extension}-{search_entry.document_type_extension}")

    # Retrieve hcOS Documents
    # ...
```

## Retrieve hcOS Documents

The final step of this demo is to parse out the ```document_root``` and ```document_extension``` from the ```search_entry``` result item and use that information to retrieve the document.

The ```document_root``` and ```document_entry``` uniquely identify a document inside of hcOS.

```python
document_root = search_entry.document_root
document_extension = search_entry.document_extension
```

Once the document id's have been extracted, we can issue a document retrieve request.

```python
document_response = document_api.get_document_by_root_extension(
    x_correlation_id=x_correlation_id,
    hcos_user_root=hcos_user_root,
    hcos_user_extension=hcos_user_extension,
    tenant_id=tenant_id,
    document_root=document_root,
    document_extension=document_extension)
```

Finally, we can process the results pulling out key information from the ```document_response_data```.

```python
print(f'\tdocument_root: {document_response.document_root}')
print(f'\tdocument_extension: {document_response.document_extension}')
print(f'\tdocument_type-description: {document_response.document_type_description}')
```

## Refreshing Tokens

Oauth2 uses something called [Bearer Tokens](https://oauth.net/2/bearer-tokens/) which expire and periodically need to be refreshed. If your token has expired the `oauthlib` library will throw a `TokenExpiredError` exception which we can catch in a `try...except` block.

```python
try:
    document_response = document_api.get_document_by_root_extension(
        x_correlation_id=x_correlation_id,
        hcos_user_root=hcos_user_root,
        hcos_user_extension=hcos_user_extension,
        tenant_id=tenant_id,
        document_root=document_root,
        document_extension=document_extension)
except TokenExpiredError as e:
    token = refresh_token(client_id, client_secret, token_url)
    document_response = document_api.get_document_by_root_extension(
        x_correlation_id=x_correlation_id,
        hcos_user_root=hcos_user_root,
        hcos_user_extension=hcos_user_extension,
        tenant_id=tenant_id,
        document_root=document_root,
        document_extension=document_extension)
```

When we catch the `TokenExpiredError` we'll refresh the token and reissue the API request. in this instance we're retrieving a document from hcOS.

## Other Exception Handling

Expired tokens only represent one type of exception you'll need to handle. Since hcOS provides a [RESTful Web API](https://en.wikipedia.org/wiki/Representational_state_transfer) you will want to handle a meaningful set of [HTTP Status Codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) in your application. the `hcos_client.rest` library contains an `ApiException` class which you can use to catch and handle any HTTP related error. It's important to note that successful calls return the payload e.g. `search_response` whereas failures thrown an `hcos_client.rest.ApiException` as seen next.

```python
try:
    search_response = search_api.post_search_by_kdsl(
        body=search_example['query'],
        x_correlation_id=x_correlation_id,
        hcos_user_root=hcos_user_root,
        hcos_user_extension=hcos_user_extension,
        tenant_id=tenant_id)
except hcos_client.rest.ApiException as e:
    print(f'{e.status} - {e.reason}\n\t{e.body}')
    raise e
```

The exception class contains properties for `status`, `reason`, and the full response `body`.

## Closing Thoughts

We hope you enjoyed this tutorial. You can request API keys from hcOS and use the [working example](GettingStarted.py) to get started innovating.
