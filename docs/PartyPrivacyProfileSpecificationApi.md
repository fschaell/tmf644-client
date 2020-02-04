# swagger_client.PartyPrivacyProfileSpecificationApi

All URIs are relative to *https://serverRoot/tmf-api/privacyManagement/v4/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_party_privacy_profile_specification**](PartyPrivacyProfileSpecificationApi.md#create_party_privacy_profile_specification) | **POST** /partyPrivacyProfileSpecification | Creates a PartyPrivacyProfileSpecification
[**delete_party_privacy_profile_specification**](PartyPrivacyProfileSpecificationApi.md#delete_party_privacy_profile_specification) | **DELETE** /partyPrivacyProfileSpecification/{id} | Deletes a PartyPrivacyProfileSpecification
[**list_party_privacy_profile_specification**](PartyPrivacyProfileSpecificationApi.md#list_party_privacy_profile_specification) | **GET** /partyPrivacyProfileSpecification | List or find PartyPrivacyProfileSpecification objects
[**patch_party_privacy_profile_specification**](PartyPrivacyProfileSpecificationApi.md#patch_party_privacy_profile_specification) | **PATCH** /partyPrivacyProfileSpecification/{id} | Updates partially a PartyPrivacyProfileSpecification
[**retrieve_party_privacy_profile_specification**](PartyPrivacyProfileSpecificationApi.md#retrieve_party_privacy_profile_specification) | **GET** /partyPrivacyProfileSpecification/{id} | Retrieves a PartyPrivacyProfileSpecification by ID


# **create_party_privacy_profile_specification**
> PartyPrivacyProfileSpecification create_party_privacy_profile_specification(party_privacy_profile_specification)

Creates a PartyPrivacyProfileSpecification

This operation creates a PartyPrivacyProfileSpecification entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyProfileSpecificationApi()
party_privacy_profile_specification = swagger_client.PartyPrivacyProfileSpecificationCreate() # PartyPrivacyProfileSpecificationCreate | The PartyPrivacyProfileSpecification to be created

try:
    # Creates a PartyPrivacyProfileSpecification
    api_response = api_instance.create_party_privacy_profile_specification(party_privacy_profile_specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyProfileSpecificationApi->create_party_privacy_profile_specification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_privacy_profile_specification** | [**PartyPrivacyProfileSpecificationCreate**](PartyPrivacyProfileSpecificationCreate.md)| The PartyPrivacyProfileSpecification to be created | 

### Return type

[**PartyPrivacyProfileSpecification**](PartyPrivacyProfileSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_party_privacy_profile_specification**
> delete_party_privacy_profile_specification(id)

Deletes a PartyPrivacyProfileSpecification

This operation deletes a PartyPrivacyProfileSpecification entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyProfileSpecificationApi()
id = 'id_example' # str | Identifier of the PartyPrivacyProfileSpecification

try:
    # Deletes a PartyPrivacyProfileSpecification
    api_instance.delete_party_privacy_profile_specification(id)
except ApiException as e:
    print("Exception when calling PartyPrivacyProfileSpecificationApi->delete_party_privacy_profile_specification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the PartyPrivacyProfileSpecification | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_party_privacy_profile_specification**
> list[PartyPrivacyProfileSpecification] list_party_privacy_profile_specification(fields=fields, offset=offset, limit=limit)

List or find PartyPrivacyProfileSpecification objects

This operation list or find PartyPrivacyProfileSpecification entities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyProfileSpecificationApi()
fields = 'fields_example' # str | Comma-separated properties to be provided in response (optional)
offset = 56 # int | Requested index for start of resources to be provided in response (optional)
limit = 56 # int | Requested number of resources to be provided in response (optional)

try:
    # List or find PartyPrivacyProfileSpecification objects
    api_response = api_instance.list_party_privacy_profile_specification(fields=fields, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyProfileSpecificationApi->list_party_privacy_profile_specification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated properties to be provided in response | [optional] 
 **offset** | **int**| Requested index for start of resources to be provided in response | [optional] 
 **limit** | **int**| Requested number of resources to be provided in response | [optional] 

### Return type

[**list[PartyPrivacyProfileSpecification]**](PartyPrivacyProfileSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_party_privacy_profile_specification**
> PartyPrivacyProfileSpecification patch_party_privacy_profile_specification(id, party_privacy_profile_specification)

Updates partially a PartyPrivacyProfileSpecification

This operation updates partially a PartyPrivacyProfileSpecification entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyProfileSpecificationApi()
id = 'id_example' # str | Identifier of the PartyPrivacyProfileSpecification
party_privacy_profile_specification = swagger_client.PartyPrivacyProfileSpecificationUpdate() # PartyPrivacyProfileSpecificationUpdate | The PartyPrivacyProfileSpecification to be updated

try:
    # Updates partially a PartyPrivacyProfileSpecification
    api_response = api_instance.patch_party_privacy_profile_specification(id, party_privacy_profile_specification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyProfileSpecificationApi->patch_party_privacy_profile_specification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the PartyPrivacyProfileSpecification | 
 **party_privacy_profile_specification** | [**PartyPrivacyProfileSpecificationUpdate**](PartyPrivacyProfileSpecificationUpdate.md)| The PartyPrivacyProfileSpecification to be updated | 

### Return type

[**PartyPrivacyProfileSpecification**](PartyPrivacyProfileSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_party_privacy_profile_specification**
> PartyPrivacyProfileSpecification retrieve_party_privacy_profile_specification(id, fields=fields)

Retrieves a PartyPrivacyProfileSpecification by ID

This operation retrieves a PartyPrivacyProfileSpecification entity. Attribute selection is enabled for all first level attributes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyProfileSpecificationApi()
id = 'id_example' # str | Identifier of the PartyPrivacyProfileSpecification
fields = 'fields_example' # str | Comma-separated properties to provide in response (optional)

try:
    # Retrieves a PartyPrivacyProfileSpecification by ID
    api_response = api_instance.retrieve_party_privacy_profile_specification(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyProfileSpecificationApi->retrieve_party_privacy_profile_specification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the PartyPrivacyProfileSpecification | 
 **fields** | **str**| Comma-separated properties to provide in response | [optional] 

### Return type

[**PartyPrivacyProfileSpecification**](PartyPrivacyProfileSpecification.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

