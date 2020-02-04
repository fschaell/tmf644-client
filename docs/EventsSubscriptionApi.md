# swagger_client.EventsSubscriptionApi

All URIs are relative to *https://serverRoot/tmf-api/privacyManagement/v4/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**register_listener**](EventsSubscriptionApi.md#register_listener) | **POST** /hub | Register a listener
[**unregister_listener**](EventsSubscriptionApi.md#unregister_listener) | **DELETE** /hub/{id} | Unregister a listener


# **register_listener**
> EventSubscription register_listener(data)

Register a listener

Sets the communication endpoint address the service instance must use to deliver information about its health state, execution state, failures and metrics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsSubscriptionApi()
data = swagger_client.EventSubscriptionInput() # EventSubscriptionInput | Data containing the callback endpoint to deliver the information

try:
    # Register a listener
    api_response = api_instance.register_listener(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsSubscriptionApi->register_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**EventSubscriptionInput**](EventSubscriptionInput.md)| Data containing the callback endpoint to deliver the information | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_listener**
> unregister_listener(id)

Unregister a listener

Resets the communication endpoint address the service instance must use to deliver information about its health state, execution state, failures and metrics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EventsSubscriptionApi()
id = 'id_example' # str | The id of the registered listener

try:
    # Unregister a listener
    api_instance.unregister_listener(id)
except ApiException as e:
    print("Exception when calling EventsSubscriptionApi->unregister_listener: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the registered listener | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

