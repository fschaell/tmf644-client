# swagger_client.PartyPrivacyProfileApi

All URIs are relative to *https://serverRoot/tmf-api/privacyManagement/v4/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_party_privacy_profile**](PartyPrivacyProfileApi.md#create_party_privacy_profile) | **POST** /partyPrivacyProfile | Creates a PartyPrivacyProfile
[**delete_party_privacy_profile**](PartyPrivacyProfileApi.md#delete_party_privacy_profile) | **DELETE** /partyPrivacyProfile/{id} | Deletes a PartyPrivacyProfile
[**list_party_privacy_profile**](PartyPrivacyProfileApi.md#list_party_privacy_profile) | **GET** /partyPrivacyProfile | List or find PartyPrivacyProfile objects
[**patch_party_privacy_profile**](PartyPrivacyProfileApi.md#patch_party_privacy_profile) | **PATCH** /partyPrivacyProfile/{id} | Updates partially a PartyPrivacyProfile
[**retrieve_party_privacy_profile**](PartyPrivacyProfileApi.md#retrieve_party_privacy_profile) | **GET** /partyPrivacyProfile/{id} | Retrieves a PartyPrivacyProfile by ID


# **create_party_privacy_profile**
> PartyPrivacyProfile create_party_privacy_profile(party_privacy_profile)

Creates a PartyPrivacyProfile

This operation creates a PartyPrivacyProfile entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyProfileApi()
party_privacy_profile = swagger_client.PartyPrivacyProfileCreate() # PartyPrivacyProfileCreate | The PartyPrivacyProfile to be created

try:
    # Creates a PartyPrivacyProfile
    api_response = api_instance.create_party_privacy_profile(party_privacy_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyProfileApi->create_party_privacy_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_privacy_profile** | [**PartyPrivacyProfileCreate**](PartyPrivacyProfileCreate.md)| The PartyPrivacyProfile to be created | 

### Return type

[**PartyPrivacyProfile**](PartyPrivacyProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_party_privacy_profile**
> delete_party_privacy_profile(id)

Deletes a PartyPrivacyProfile

This operation deletes a PartyPrivacyProfile entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyProfileApi()
id = 'id_example' # str | Identifier of the PartyPrivacyProfile

try:
    # Deletes a PartyPrivacyProfile
    api_instance.delete_party_privacy_profile(id)
except ApiException as e:
    print("Exception when calling PartyPrivacyProfileApi->delete_party_privacy_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the PartyPrivacyProfile | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_party_privacy_profile**
> list[PartyPrivacyProfile] list_party_privacy_profile(fields=fields, offset=offset, limit=limit)

List or find PartyPrivacyProfile objects

This operation list or find PartyPrivacyProfile entities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyProfileApi()
fields = 'fields_example' # str | Comma-separated properties to be provided in response (optional)
offset = 56 # int | Requested index for start of resources to be provided in response (optional)
limit = 56 # int | Requested number of resources to be provided in response (optional)

try:
    # List or find PartyPrivacyProfile objects
    api_response = api_instance.list_party_privacy_profile(fields=fields, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyProfileApi->list_party_privacy_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated properties to be provided in response | [optional] 
 **offset** | **int**| Requested index for start of resources to be provided in response | [optional] 
 **limit** | **int**| Requested number of resources to be provided in response | [optional] 

### Return type

[**list[PartyPrivacyProfile]**](PartyPrivacyProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_party_privacy_profile**
> PartyPrivacyProfile patch_party_privacy_profile(id, party_privacy_profile)

Updates partially a PartyPrivacyProfile

This operation updates partially a PartyPrivacyProfile entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyProfileApi()
id = 'id_example' # str | Identifier of the PartyPrivacyProfile
party_privacy_profile = swagger_client.PartyPrivacyProfileUpdate() # PartyPrivacyProfileUpdate | The PartyPrivacyProfile to be updated

try:
    # Updates partially a PartyPrivacyProfile
    api_response = api_instance.patch_party_privacy_profile(id, party_privacy_profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyProfileApi->patch_party_privacy_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the PartyPrivacyProfile | 
 **party_privacy_profile** | [**PartyPrivacyProfileUpdate**](PartyPrivacyProfileUpdate.md)| The PartyPrivacyProfile to be updated | 

### Return type

[**PartyPrivacyProfile**](PartyPrivacyProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_party_privacy_profile**
> PartyPrivacyProfile retrieve_party_privacy_profile(id, fields=fields)

Retrieves a PartyPrivacyProfile by ID

This operation retrieves a PartyPrivacyProfile entity. Attribute selection is enabled for all first level attributes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyProfileApi()
id = 'id_example' # str | Identifier of the PartyPrivacyProfile
fields = 'fields_example' # str | Comma-separated properties to provide in response (optional)

try:
    # Retrieves a PartyPrivacyProfile by ID
    api_response = api_instance.retrieve_party_privacy_profile(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyProfileApi->retrieve_party_privacy_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the PartyPrivacyProfile | 
 **fields** | **str**| Comma-separated properties to provide in response | [optional] 

### Return type

[**PartyPrivacyProfile**](PartyPrivacyProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

