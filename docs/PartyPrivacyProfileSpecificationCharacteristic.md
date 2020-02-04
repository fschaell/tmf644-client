# PartyPrivacyProfileSpecificationCharacteristic

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**criticality_level** | **str** | Level of criticality for this characteristic of personal identifiable information (e.g. in terms of the damage if this item was breached), such as low, medium, high. | [optional] 
**description** | **str** | Description of the characteristic | [optional] 
**name** | **str** | Name of the characteristic | [optional] 
**privacy_type** | **str** | Type of privacy (e.g. Internal Purpose, External Purpose, Internal Retention, External Retention) | [optional] 
**privacy_usage_purpose** | **str** | Defines the purpose authorized or refused for the characteristic (e.g. ADMIN, INFORMATION, MARKETING, RESEARCH). | [optional] 
**allowed_role** | [**list[RoleSpecification]**](RoleSpecification.md) | A list of roles in the organization who are allowed access to this characteristic | [optional] 
**party_privacy_profile_spec_characteristic_value** | [**list[SpecificationCharacteristicValue]**](SpecificationCharacteristicValue.md) | List of values that can be assigned to this characteristic at runtime | [optional] 
**valid_for** | [**TimePeriod**](TimePeriod.md) | The period of time for which this characteristic specification is valid. | [optional] 
**base_type** | **str** | When sub-classing, this defines the super-class | [optional] 
**schema_location** | **str** | A URI to a JSON-Schema file that defines additional attributes and relationships | [optional] 
**type** | **str** | When sub-classing, this defines the sub-class entity name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


