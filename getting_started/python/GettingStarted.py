import os
import json
import requests
import traceback
import uuid
import urllib3
import hcos_client
from oauthlib.oauth2 import BackendApplicationClient, TokenExpiredError
from requests_oauthlib import OAuth2, OAuth2Session

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def refresh_token(client_id, client_secret, token_url):
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(
        token_url=token_url,
        client_id=client_id,
        client_secret=client_secret
    )
    return token

def demo():
    print('Getting Started demo begins...')

    # load hcOS Search API configuration
    with open('../configurations/Configuration.json') as f:
        config = json.load(f)

    base_path = config['basePath']
    client_id = config['clientId']
    client_secret = config['clientSecret']
    token_url = os.path.join(config['oauthBaseUrl'], 'oauth2/token')
    tenant_id = config['tenantId']

    x_correlation_id = str(uuid.uuid4())
    x_hcos_user_root = 'hcos.upmce.net'
    x_hcos_user_extension = 'username'

    token = refresh_token(client_id, client_secret, token_url) # get an Oauth2 token

    configuration = hcos_client.Configuration()
    configuration.host = base_path
    configuration.verify_ssl = False
    configuration.access_token = token['access_token']

    api_client = hcos_client.api_client.ApiClient(configuration=configuration)

    search_api = hcos_client.api.search_api.SearchApi(api_client=api_client)
    document_api = hcos_client.api.document_api.DocumentApi(api_client=api_client)

    try:
        # load searches
        with open('../Searches.json') as f:
            search_examples = json.load(f)

        search_example = search_examples[0]
        print(search_example["description"])

        # Search hcOS
        try:
            search_result = search_api.post_search_by_kdsl(
                body=search_example['query'], 
                x_correlation_id=x_correlation_id, 
                x_hcos_user_root=x_hcos_user_root, 
                x_hcos_user_extension=x_hcos_user_extension, 
                tenant_id=tenant_id)
        except TokenExpiredError as e:
            token = refresh_token(client_id, client_secret, token_url)
            search_result = search_api.post_search_by_kdsl(
                body=search_example['query'], 
                x_correlation_id=x_correlation_id, 
                x_hcos_user_root=x_hcos_user_root, 
                x_hcos_user_extension=x_hcos_user_extension, 
                tenant_id=tenant_id)
        except hcos_client.rest.ApiException as e:
            print(f'{e.status} - {e.reason}\n\t{e.body}')
            raise e

        # Process hcOS Search Results
        print(f'offset: {search_result.offset}')
        print(f'record_count: {search_result.record_count}')
        print(f'total_record_count: {search_result.total_record_count}')

        # iterate over the results and retrieve documents
        for index, search_hit in enumerate(search_result.hits):
            print(f"{index} {search_hit.document_root}-{search_hit.document_extension}-{search_hit.document_type_extension}")

            document_root = search_hit.document_root
            document_extension = search_hit.document_extension

            # Retrieve document from hcOS
            try:
                document_meta_data = document_api.get_document_by_root_extension(
                    x_correlation_id=x_correlation_id, 
                    x_hcos_user_root=x_hcos_user_root, 
                    x_hcos_user_extension=x_hcos_user_extension, 
                    tenant_id=tenant_id,
                    document_root=document_root, 
                    document_extension=document_extension)
            except TokenExpiredError as e:
                token = refresh_token(client_id, client_secret, token_url)
                document_meta_data = document_api.get_document_by_root_extension(
                    x_correlation_id=x_correlation_id, 
                    x_hcos_user_root=x_hcos_user_root, 
                    x_hcos_user_extension=x_hcos_user_extension, 
                    tenant_id=tenant_id,
                    document_root=document_root, 
                    document_extension=document_extension)
            except hcos_client.rest.ApiException as e:
                print(f'{e.status} - {e.reason}\n\t{e.body}')
                raise e

            print(f'\tdocument_root: {document_meta_data.document_root}')
            print(f'\tdocument_extension: {document_meta_data.document_extension}')
            print(f'\tdocument_type-description: {document_meta_data.document_type_description}')
    except Exception as e:
        print(traceback.print_exc())

    print("Getting Started demo ends...")

if __name__ == '__main__':
    demo()
