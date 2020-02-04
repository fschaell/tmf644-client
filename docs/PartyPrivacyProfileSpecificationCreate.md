# PartyPrivacyProfileSpecificationCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the specification | [optional] 
**last_update** | **datetime** | Date and time when the specification was last updated | [optional] 
**name** | **str** | Name of the specification | [optional] 
**status** | **str** | Lifecycle status of the specification (e.g. In Design, Active, Rejected, Retired) | [optional] 
**version** | **str** | The version of the specification, in case it is desired to maintain multiple versions of profile specifications | [optional] 
**applicable_role** | [**list[PartyPrivacyRoleSpecification]**](PartyPrivacyRoleSpecification.md) | A list of roles to which this specification can apply. For example: Shop Agent, Call Center Agent. | [optional] 
**party_privacy_profile_spec_characteristic** | [**list[PartyPrivacyProfileSpecificationCharacteristic]**](PartyPrivacyProfileSpecificationCharacteristic.md) | List of characteristics of the specification, whose values would typically be supplied when the profile is instantiated | 
**product_offering** | [**list[ProductOfferingRef]**](ProductOfferingRef.md) |  | [optional] 
**related_party** | [**list[RelatedParty]**](RelatedParty.md) | List of parties or party roles involved in the definition or management of the specification | [optional] 
**valid_for** | [**TimePeriod**](TimePeriod.md) | The period of time for which the specification is valid | [optional] 
**base_type** | **str** | When sub-classing, this defines the super-class | [optional] 
**schema_location** | **str** | A URI to a JSON-Schema file that defines additional attributes and relationships | [optional] 
**type** | **str** | When sub-classing, this defines the sub-class entity name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


