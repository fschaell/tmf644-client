# swagger_client.PartyPrivacyAgreementApi

All URIs are relative to *https://serverRoot/tmf-api/privacyManagement/v4/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_party_privacy_agreement**](PartyPrivacyAgreementApi.md#create_party_privacy_agreement) | **POST** /partyPrivacyAgreement | Creates a PartyPrivacyAgreement
[**delete_party_privacy_agreement**](PartyPrivacyAgreementApi.md#delete_party_privacy_agreement) | **DELETE** /partyPrivacyAgreement/{id} | Deletes a PartyPrivacyAgreement
[**list_party_privacy_agreement**](PartyPrivacyAgreementApi.md#list_party_privacy_agreement) | **GET** /partyPrivacyAgreement | List or find PartyPrivacyAgreement objects
[**patch_party_privacy_agreement**](PartyPrivacyAgreementApi.md#patch_party_privacy_agreement) | **PATCH** /partyPrivacyAgreement/{id} | Updates partially a PartyPrivacyAgreement
[**retrieve_party_privacy_agreement**](PartyPrivacyAgreementApi.md#retrieve_party_privacy_agreement) | **GET** /partyPrivacyAgreement/{id} | Retrieves a PartyPrivacyAgreement by ID


# **create_party_privacy_agreement**
> PartyPrivacyAgreement create_party_privacy_agreement(party_privacy_agreement)

Creates a PartyPrivacyAgreement

This operation creates a PartyPrivacyAgreement entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyAgreementApi()
party_privacy_agreement = swagger_client.PartyPrivacyAgreementCreate() # PartyPrivacyAgreementCreate | The PartyPrivacyAgreement to be created

try:
    # Creates a PartyPrivacyAgreement
    api_response = api_instance.create_party_privacy_agreement(party_privacy_agreement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyAgreementApi->create_party_privacy_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **party_privacy_agreement** | [**PartyPrivacyAgreementCreate**](PartyPrivacyAgreementCreate.md)| The PartyPrivacyAgreement to be created | 

### Return type

[**PartyPrivacyAgreement**](PartyPrivacyAgreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_party_privacy_agreement**
> delete_party_privacy_agreement(id)

Deletes a PartyPrivacyAgreement

This operation deletes a PartyPrivacyAgreement entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyAgreementApi()
id = 'id_example' # str | Identifier of the PartyPrivacyAgreement

try:
    # Deletes a PartyPrivacyAgreement
    api_instance.delete_party_privacy_agreement(id)
except ApiException as e:
    print("Exception when calling PartyPrivacyAgreementApi->delete_party_privacy_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the PartyPrivacyAgreement | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_party_privacy_agreement**
> list[PartyPrivacyAgreement] list_party_privacy_agreement(fields=fields, offset=offset, limit=limit)

List or find PartyPrivacyAgreement objects

This operation list or find PartyPrivacyAgreement entities

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyAgreementApi()
fields = 'fields_example' # str | Comma-separated properties to be provided in response (optional)
offset = 56 # int | Requested index for start of resources to be provided in response (optional)
limit = 56 # int | Requested number of resources to be provided in response (optional)

try:
    # List or find PartyPrivacyAgreement objects
    api_response = api_instance.list_party_privacy_agreement(fields=fields, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyAgreementApi->list_party_privacy_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | **str**| Comma-separated properties to be provided in response | [optional] 
 **offset** | **int**| Requested index for start of resources to be provided in response | [optional] 
 **limit** | **int**| Requested number of resources to be provided in response | [optional] 

### Return type

[**list[PartyPrivacyAgreement]**](PartyPrivacyAgreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_party_privacy_agreement**
> PartyPrivacyAgreement patch_party_privacy_agreement(id, party_privacy_agreement)

Updates partially a PartyPrivacyAgreement

This operation updates partially a PartyPrivacyAgreement entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyAgreementApi()
id = 'id_example' # str | Identifier of the PartyPrivacyAgreement
party_privacy_agreement = swagger_client.PartyPrivacyAgreementUpdate() # PartyPrivacyAgreementUpdate | The PartyPrivacyAgreement to be updated

try:
    # Updates partially a PartyPrivacyAgreement
    api_response = api_instance.patch_party_privacy_agreement(id, party_privacy_agreement)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyAgreementApi->patch_party_privacy_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the PartyPrivacyAgreement | 
 **party_privacy_agreement** | [**PartyPrivacyAgreementUpdate**](PartyPrivacyAgreementUpdate.md)| The PartyPrivacyAgreement to be updated | 

### Return type

[**PartyPrivacyAgreement**](PartyPrivacyAgreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_party_privacy_agreement**
> PartyPrivacyAgreement retrieve_party_privacy_agreement(id, fields=fields)

Retrieves a PartyPrivacyAgreement by ID

This operation retrieves a PartyPrivacyAgreement entity. Attribute selection is enabled for all first level attributes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PartyPrivacyAgreementApi()
id = 'id_example' # str | Identifier of the PartyPrivacyAgreement
fields = 'fields_example' # str | Comma-separated properties to provide in response (optional)

try:
    # Retrieves a PartyPrivacyAgreement by ID
    api_response = api_instance.retrieve_party_privacy_agreement(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PartyPrivacyAgreementApi->retrieve_party_privacy_agreement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the PartyPrivacyAgreement | 
 **fields** | **str**| Comma-separated properties to provide in response | [optional] 

### Return type

[**PartyPrivacyAgreement**](PartyPrivacyAgreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

