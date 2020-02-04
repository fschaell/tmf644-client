# swagger_client.NotificationListenersClientSideApi

All URIs are relative to *https://serverRoot/tmf-api/privacyManagement/v4/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listen_to_party_privacy_agreement_attribute_value_change_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_agreement_attribute_value_change_event) | **POST** /listener/partyPrivacyAgreementAttributeValueChangeEvent | Client listener for entity PartyPrivacyAgreementAttributeValueChangeEvent
[**listen_to_party_privacy_agreement_create_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_agreement_create_event) | **POST** /listener/partyPrivacyAgreementCreateEvent | Client listener for entity PartyPrivacyAgreementCreateEvent
[**listen_to_party_privacy_agreement_delete_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_agreement_delete_event) | **POST** /listener/partyPrivacyAgreementDeleteEvent | Client listener for entity PartyPrivacyAgreementDeleteEvent
[**listen_to_party_privacy_agreement_status_change_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_agreement_status_change_event) | **POST** /listener/partyPrivacyAgreementStatusChangeEvent | Client listener for entity PartyPrivacyAgreementStatusChangeEvent
[**listen_to_party_privacy_profile_attribute_value_change_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_profile_attribute_value_change_event) | **POST** /listener/partyPrivacyProfileAttributeValueChangeEvent | Client listener for entity PartyPrivacyProfileAttributeValueChangeEvent
[**listen_to_party_privacy_profile_create_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_profile_create_event) | **POST** /listener/partyPrivacyProfileCreateEvent | Client listener for entity PartyPrivacyProfileCreateEvent
[**listen_to_party_privacy_profile_delete_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_profile_delete_event) | **POST** /listener/partyPrivacyProfileDeleteEvent | Client listener for entity PartyPrivacyProfileDeleteEvent
[**listen_to_party_privacy_profile_specification_attribute_value_change_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_profile_specification_attribute_value_change_event) | **POST** /listener/partyPrivacyProfileSpecificationAttributeValueChangeEvent | Client listener for entity PartyPrivacyProfileSpecificationAttributeValueChangeEvent
[**listen_to_party_privacy_profile_specification_create_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_profile_specification_create_event) | **POST** /listener/partyPrivacyProfileSpecificationCreateEvent | Client listener for entity PartyPrivacyProfileSpecificationCreateEvent
[**listen_to_party_privacy_profile_specification_delete_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_profile_specification_delete_event) | **POST** /listener/partyPrivacyProfileSpecificationDeleteEvent | Client listener for entity PartyPrivacyProfileSpecificationDeleteEvent
[**listen_to_party_privacy_profile_specification_status_change_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_profile_specification_status_change_event) | **POST** /listener/partyPrivacyProfileSpecificationStatusChangeEvent | Client listener for entity PartyPrivacyProfileSpecificationStatusChangeEvent
[**listen_to_party_privacy_profile_status_change_event**](NotificationListenersClientSideApi.md#listen_to_party_privacy_profile_status_change_event) | **POST** /listener/partyPrivacyProfileStatusChangeEvent | Client listener for entity PartyPrivacyProfileStatusChangeEvent


# **listen_to_party_privacy_agreement_attribute_value_change_event**
> EventSubscription listen_to_party_privacy_agreement_attribute_value_change_event(data)

Client listener for entity PartyPrivacyAgreementAttributeValueChangeEvent

Example of a client listener for receiving the notification PartyPrivacyAgreementAttributeValueChangeEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyAgreementAttributeValueChangeEvent() # PartyPrivacyAgreementAttributeValueChangeEvent | The event data

try:
    # Client listener for entity PartyPrivacyAgreementAttributeValueChangeEvent
    api_response = api_instance.listen_to_party_privacy_agreement_attribute_value_change_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_agreement_attribute_value_change_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyAgreementAttributeValueChangeEvent**](PartyPrivacyAgreementAttributeValueChangeEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_agreement_create_event**
> EventSubscription listen_to_party_privacy_agreement_create_event(data)

Client listener for entity PartyPrivacyAgreementCreateEvent

Example of a client listener for receiving the notification PartyPrivacyAgreementCreateEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyAgreementCreateEvent() # PartyPrivacyAgreementCreateEvent | The event data

try:
    # Client listener for entity PartyPrivacyAgreementCreateEvent
    api_response = api_instance.listen_to_party_privacy_agreement_create_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_agreement_create_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyAgreementCreateEvent**](PartyPrivacyAgreementCreateEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_agreement_delete_event**
> EventSubscription listen_to_party_privacy_agreement_delete_event(data)

Client listener for entity PartyPrivacyAgreementDeleteEvent

Example of a client listener for receiving the notification PartyPrivacyAgreementDeleteEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyAgreementDeleteEvent() # PartyPrivacyAgreementDeleteEvent | The event data

try:
    # Client listener for entity PartyPrivacyAgreementDeleteEvent
    api_response = api_instance.listen_to_party_privacy_agreement_delete_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_agreement_delete_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyAgreementDeleteEvent**](PartyPrivacyAgreementDeleteEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_agreement_status_change_event**
> EventSubscription listen_to_party_privacy_agreement_status_change_event(data)

Client listener for entity PartyPrivacyAgreementStatusChangeEvent

Example of a client listener for receiving the notification PartyPrivacyAgreementStatusChangeEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyAgreementStatusChangeEvent() # PartyPrivacyAgreementStatusChangeEvent | The event data

try:
    # Client listener for entity PartyPrivacyAgreementStatusChangeEvent
    api_response = api_instance.listen_to_party_privacy_agreement_status_change_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_agreement_status_change_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyAgreementStatusChangeEvent**](PartyPrivacyAgreementStatusChangeEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_profile_attribute_value_change_event**
> EventSubscription listen_to_party_privacy_profile_attribute_value_change_event(data)

Client listener for entity PartyPrivacyProfileAttributeValueChangeEvent

Example of a client listener for receiving the notification PartyPrivacyProfileAttributeValueChangeEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyProfileAttributeValueChangeEvent() # PartyPrivacyProfileAttributeValueChangeEvent | The event data

try:
    # Client listener for entity PartyPrivacyProfileAttributeValueChangeEvent
    api_response = api_instance.listen_to_party_privacy_profile_attribute_value_change_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_profile_attribute_value_change_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyProfileAttributeValueChangeEvent**](PartyPrivacyProfileAttributeValueChangeEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_profile_create_event**
> EventSubscription listen_to_party_privacy_profile_create_event(data)

Client listener for entity PartyPrivacyProfileCreateEvent

Example of a client listener for receiving the notification PartyPrivacyProfileCreateEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyProfileCreateEvent() # PartyPrivacyProfileCreateEvent | The event data

try:
    # Client listener for entity PartyPrivacyProfileCreateEvent
    api_response = api_instance.listen_to_party_privacy_profile_create_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_profile_create_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyProfileCreateEvent**](PartyPrivacyProfileCreateEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_profile_delete_event**
> EventSubscription listen_to_party_privacy_profile_delete_event(data)

Client listener for entity PartyPrivacyProfileDeleteEvent

Example of a client listener for receiving the notification PartyPrivacyProfileDeleteEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyProfileDeleteEvent() # PartyPrivacyProfileDeleteEvent | The event data

try:
    # Client listener for entity PartyPrivacyProfileDeleteEvent
    api_response = api_instance.listen_to_party_privacy_profile_delete_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_profile_delete_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyProfileDeleteEvent**](PartyPrivacyProfileDeleteEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_profile_specification_attribute_value_change_event**
> EventSubscription listen_to_party_privacy_profile_specification_attribute_value_change_event(data)

Client listener for entity PartyPrivacyProfileSpecificationAttributeValueChangeEvent

Example of a client listener for receiving the notification PartyPrivacyProfileSpecificationAttributeValueChangeEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyProfileSpecificationAttributeValueChangeEvent() # PartyPrivacyProfileSpecificationAttributeValueChangeEvent | The event data

try:
    # Client listener for entity PartyPrivacyProfileSpecificationAttributeValueChangeEvent
    api_response = api_instance.listen_to_party_privacy_profile_specification_attribute_value_change_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_profile_specification_attribute_value_change_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyProfileSpecificationAttributeValueChangeEvent**](PartyPrivacyProfileSpecificationAttributeValueChangeEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_profile_specification_create_event**
> EventSubscription listen_to_party_privacy_profile_specification_create_event(data)

Client listener for entity PartyPrivacyProfileSpecificationCreateEvent

Example of a client listener for receiving the notification PartyPrivacyProfileSpecificationCreateEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyProfileSpecificationCreateEvent() # PartyPrivacyProfileSpecificationCreateEvent | The event data

try:
    # Client listener for entity PartyPrivacyProfileSpecificationCreateEvent
    api_response = api_instance.listen_to_party_privacy_profile_specification_create_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_profile_specification_create_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyProfileSpecificationCreateEvent**](PartyPrivacyProfileSpecificationCreateEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_profile_specification_delete_event**
> EventSubscription listen_to_party_privacy_profile_specification_delete_event(data)

Client listener for entity PartyPrivacyProfileSpecificationDeleteEvent

Example of a client listener for receiving the notification PartyPrivacyProfileSpecificationDeleteEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyProfileSpecificationDeleteEvent() # PartyPrivacyProfileSpecificationDeleteEvent | The event data

try:
    # Client listener for entity PartyPrivacyProfileSpecificationDeleteEvent
    api_response = api_instance.listen_to_party_privacy_profile_specification_delete_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_profile_specification_delete_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyProfileSpecificationDeleteEvent**](PartyPrivacyProfileSpecificationDeleteEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_profile_specification_status_change_event**
> EventSubscription listen_to_party_privacy_profile_specification_status_change_event(data)

Client listener for entity PartyPrivacyProfileSpecificationStatusChangeEvent

Example of a client listener for receiving the notification PartyPrivacyProfileSpecificationStatusChangeEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyProfileSpecificationStatusChangeEvent() # PartyPrivacyProfileSpecificationStatusChangeEvent | The event data

try:
    # Client listener for entity PartyPrivacyProfileSpecificationStatusChangeEvent
    api_response = api_instance.listen_to_party_privacy_profile_specification_status_change_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_profile_specification_status_change_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyProfileSpecificationStatusChangeEvent**](PartyPrivacyProfileSpecificationStatusChangeEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_to_party_privacy_profile_status_change_event**
> EventSubscription listen_to_party_privacy_profile_status_change_event(data)

Client listener for entity PartyPrivacyProfileStatusChangeEvent

Example of a client listener for receiving the notification PartyPrivacyProfileStatusChangeEvent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotificationListenersClientSideApi()
data = swagger_client.PartyPrivacyProfileStatusChangeEvent() # PartyPrivacyProfileStatusChangeEvent | The event data

try:
    # Client listener for entity PartyPrivacyProfileStatusChangeEvent
    api_response = api_instance.listen_to_party_privacy_profile_status_change_event(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationListenersClientSideApi->listen_to_party_privacy_profile_status_change_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**PartyPrivacyProfileStatusChangeEvent**](PartyPrivacyProfileStatusChangeEvent.md)| The event data | 

### Return type

[**EventSubscription**](EventSubscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json;charset=utf-8
 - **Accept**: application/json;charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

