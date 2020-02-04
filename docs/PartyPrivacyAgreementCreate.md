# PartyPrivacyAgreementCreate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agreement_type** | **str** | The type of the agreement. For example commercial | 
**description** | **str** | Narrative that explains the agreement and details about the it , such as why the agreement is taking place. | [optional] 
**document_number** | **int** | A reference number assigned to an Agreement that follows a prescribed numbering system. | [optional] 
**initial_date** | **datetime** | Date at which the agreement was initialized | [optional] 
**name** | **str** | A human-readable name for the agreement | 
**statement_of_intent** | **str** | An overview and goals of the Agreement | [optional] 
**status** | **str** | The current status of the agreement. Typical values are: in process, approved and rejected | [optional] 
**version** | **str** | A string identifying the version of the agreement | [optional] 
**agreement_authorization** | [**list[AgreementAuthorization]**](AgreementAuthorization.md) |  | [optional] 
**agreement_item** | [**list[AgreementItem]**](AgreementItem.md) |  | 
**agreement_period** | [**TimePeriod**](TimePeriod.md) | The time period during which the Agreement is in effect. | [optional] 
**agreement_specification** | [**AgreementSpecificationRef**](AgreementSpecificationRef.md) |  | [optional] 
**associated_agreement** | [**list[AgreementRef]**](AgreementRef.md) |  | [optional] 
**characteristic** | [**list[Characteristic]**](Characteristic.md) |  | [optional] 
**completion_date** | [**TimePeriod**](TimePeriod.md) | Date at which the agreement is completed | [optional] 
**engaged_party_role** | [**list[RelatedParty]**](RelatedParty.md) |  | 
**party_privacy_profile** | [**list[PartyPrivacyProfileRef]**](PartyPrivacyProfileRef.md) | The privacy profiles that are the subject of the agreement | [optional] 
**party_privacy_profile_characteristic** | [**list[PartyPrivacyProfileCharacteristic]**](PartyPrivacyProfileCharacteristic.md) | A list of (typically) high criticality characteristics whose chosen privacy rules are included in the agreement | [optional] 
**base_type** | **str** | When sub-classing, this defines the super-class | [optional] 
**schema_location** | **str** | A URI to a JSON-Schema file that defines additional attributes and relationships | [optional] 
**type** | **str** | When sub-classing, this defines the sub-class entity name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


