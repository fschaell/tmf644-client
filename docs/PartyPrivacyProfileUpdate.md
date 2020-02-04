# PartyPrivacyProfileUpdate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the privacy profile | [optional] 
**name** | **str** | Name of the privacy profile | [optional] 
**status** | **str** | The status of this profile (such as agreed, created, terminated, etc.) | [optional] 
**agreed_by_party** | [**RelatedParty**](RelatedParty.md) | The party who agreed to the privacy profile. Not necessarily the party to whom the profile applies. | 
**agreement** | [**PartyPrivacyAgreementRef**](PartyPrivacyAgreementRef.md) | An agreement under which the privacy profile was produced. | [optional] 
**applicable_for_party** | [**RelatedParty**](RelatedParty.md) | The party to whom the privacy profile applies. Could be a minor where the agreeing party is a parent, an organization where the agreeing party is authorized to make such agreements, or some individual for whom the agreeing party has authorization (e.g. power of attorney). If empty, the agreeing party is the party to whom the profile applies. | [optional] 
**party_privacy_profile_characteristic** | [**list[PartyPrivacyProfileCharacteristic]**](PartyPrivacyProfileCharacteristic.md) | List of characteristics of the privacy profile | [optional] 
**party_privacy_profile_specification** | [**PartyPrivacyProfileSpecificationRef**](PartyPrivacyProfileSpecificationRef.md) | The specification from which this profile was instantiated | [optional] 
**valid_for** | [**TimePeriod**](TimePeriod.md) | The period of time for which this profile is valid, depending on regulations or business consideration the profile may expire and need to be renegotiated. | [optional] 
**base_type** | **str** | When sub-classing, this defines the super-class | [optional] 
**schema_location** | **str** | A URI to a JSON-Schema file that defines additional attributes and relationships | [optional] 
**type** | **str** | When sub-classing, this defines the sub-class entity name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


