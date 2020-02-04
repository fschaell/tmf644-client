# PartyPrivacyProfileCharacteristic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | Name of the characteristic | 
**privacy_usage_purpose** | **str** | Defines the purpose authorized or refused for the characteristic (e.g. ADMIN, INFORMATION, MARKETING, RESEARCH, etc. | [optional] 
**value_type** | **str** | Data type of the value of the characteristic | [optional] 
**related_party** | [**list[RelatedParty]**](RelatedParty.md) | A list of parties to which the allowed use of the characteristic applies. | [optional] 
**value** | [**Any**](Any.md) | The value of the characteristic | 
**base_type** | **str** | When sub-classing, this defines the super-class | [optional] 
**schema_location** | **str** | A URI to a JSON-Schema file that defines additional attributes and relationships | [optional] 
**type** | **str** | When sub-classing, this defines the sub-class entity name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


