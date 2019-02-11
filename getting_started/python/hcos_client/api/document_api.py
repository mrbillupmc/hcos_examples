# coding: utf-8

"""
    hcOS Developer Experience

    hcOS Developer Experience API  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hcos_client.api_client import ApiClient


class DocumentApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_document_by_root_extension(self, x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, **kwargs):  # noqa: E501
        """Requests current primary document by document root, extension.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_by_root_extension(x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_correlation_id: (required)
        :param str x_hcos_user_root: (required)
        :param str x_hcos_user_extension: (required)
        :param str tenant_id: (required)
        :param str document_root: (required)
        :param str document_extension: (required)
        :return: DocumentMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_document_by_root_extension_with_http_info(x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, **kwargs)  # noqa: E501
        else:
            (data) = self.get_document_by_root_extension_with_http_info(x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, **kwargs)  # noqa: E501
            return data

    def get_document_by_root_extension_with_http_info(self, x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, **kwargs):  # noqa: E501
        """Requests current primary document by document root, extension.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_by_root_extension_with_http_info(x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_correlation_id: (required)
        :param str x_hcos_user_root: (required)
        :param str x_hcos_user_extension: (required)
        :param str tenant_id: (required)
        :param str document_root: (required)
        :param str document_extension: (required)
        :return: DocumentMeta
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_correlation_id', 'x_hcos_user_root', 'x_hcos_user_extension', 'tenant_id', 'document_root', 'document_extension']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_by_root_extension" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_correlation_id' is set
        if ('x_correlation_id' not in params or
                params['x_correlation_id'] is None):
            raise ValueError("Missing the required parameter `x_correlation_id` when calling `get_document_by_root_extension`")  # noqa: E501
        # verify the required parameter 'x_hcos_user_root' is set
        if ('x_hcos_user_root' not in params or
                params['x_hcos_user_root'] is None):
            raise ValueError("Missing the required parameter `x_hcos_user_root` when calling `get_document_by_root_extension`")  # noqa: E501
        # verify the required parameter 'x_hcos_user_extension' is set
        if ('x_hcos_user_extension' not in params or
                params['x_hcos_user_extension'] is None):
            raise ValueError("Missing the required parameter `x_hcos_user_extension` when calling `get_document_by_root_extension`")  # noqa: E501
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_document_by_root_extension`")  # noqa: E501
        # verify the required parameter 'document_root' is set
        if ('document_root' not in params or
                params['document_root'] is None):
            raise ValueError("Missing the required parameter `document_root` when calling `get_document_by_root_extension`")  # noqa: E501
        # verify the required parameter 'document_extension' is set
        if ('document_extension' not in params or
                params['document_extension'] is None):
            raise ValueError("Missing the required parameter `document_extension` when calling `get_document_by_root_extension`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenant_id'] = params['tenant_id']  # noqa: E501
        if 'document_root' in params:
            path_params['document_root'] = params['document_root']  # noqa: E501
        if 'document_extension' in params:
            path_params['document_extension'] = params['document_extension']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_correlation_id' in params:
            header_params['x-correlation-id'] = params['x_correlation_id']  # noqa: E501
        if 'x_hcos_user_root' in params:
            header_params['x-hcos-user-root'] = params['x_hcos_user_root']  # noqa: E501
        if 'x_hcos_user_extension' in params:
            header_params['x-hcos-user-extension'] = params['x_hcos_user_extension']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/{tenant_id}/document/root/{document_root}/extension/{document_extension}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DocumentMeta',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_data_by_root_extension(self, x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, **kwargs):  # noqa: E501
        """Requests document data by document root, extension.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_data_by_root_extension(x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_correlation_id: (required)
        :param str x_hcos_user_root: (required)
        :param str x_hcos_user_extension: (required)
        :param str tenant_id: (required)
        :param str document_root: (required)
        :param str document_extension: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_document_data_by_root_extension_with_http_info(x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, **kwargs)  # noqa: E501
        else:
            (data) = self.get_document_data_by_root_extension_with_http_info(x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, **kwargs)  # noqa: E501
            return data

    def get_document_data_by_root_extension_with_http_info(self, x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, **kwargs):  # noqa: E501
        """Requests document data by document root, extension.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_data_by_root_extension_with_http_info(x_correlation_id, x_hcos_user_root, x_hcos_user_extension, tenant_id, document_root, document_extension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_correlation_id: (required)
        :param str x_hcos_user_root: (required)
        :param str x_hcos_user_extension: (required)
        :param str tenant_id: (required)
        :param str document_root: (required)
        :param str document_extension: (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_correlation_id', 'x_hcos_user_root', 'x_hcos_user_extension', 'tenant_id', 'document_root', 'document_extension']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_data_by_root_extension" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_correlation_id' is set
        if ('x_correlation_id' not in params or
                params['x_correlation_id'] is None):
            raise ValueError("Missing the required parameter `x_correlation_id` when calling `get_document_data_by_root_extension`")  # noqa: E501
        # verify the required parameter 'x_hcos_user_root' is set
        if ('x_hcos_user_root' not in params or
                params['x_hcos_user_root'] is None):
            raise ValueError("Missing the required parameter `x_hcos_user_root` when calling `get_document_data_by_root_extension`")  # noqa: E501
        # verify the required parameter 'x_hcos_user_extension' is set
        if ('x_hcos_user_extension' not in params or
                params['x_hcos_user_extension'] is None):
            raise ValueError("Missing the required parameter `x_hcos_user_extension` when calling `get_document_data_by_root_extension`")  # noqa: E501
        # verify the required parameter 'tenant_id' is set
        if ('tenant_id' not in params or
                params['tenant_id'] is None):
            raise ValueError("Missing the required parameter `tenant_id` when calling `get_document_data_by_root_extension`")  # noqa: E501
        # verify the required parameter 'document_root' is set
        if ('document_root' not in params or
                params['document_root'] is None):
            raise ValueError("Missing the required parameter `document_root` when calling `get_document_data_by_root_extension`")  # noqa: E501
        # verify the required parameter 'document_extension' is set
        if ('document_extension' not in params or
                params['document_extension'] is None):
            raise ValueError("Missing the required parameter `document_extension` when calling `get_document_data_by_root_extension`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tenant_id' in params:
            path_params['tenant_id'] = params['tenant_id']  # noqa: E501
        if 'document_root' in params:
            path_params['document_root'] = params['document_root']  # noqa: E501
        if 'document_extension' in params:
            path_params['document_extension'] = params['document_extension']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_correlation_id' in params:
            header_params['x-correlation-id'] = params['x_correlation_id']  # noqa: E501
        if 'x_hcos_user_root' in params:
            header_params['x-hcos-user-root'] = params['x_hcos_user_root']  # noqa: E501
        if 'x_hcos_user_extension' in params:
            header_params['x-hcos-user-extension'] = params['x_hcos_user_extension']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'text/html', 'application/pdf'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/{tenant_id}/document/root/{document_root}/extension/{document_extension}/data', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
