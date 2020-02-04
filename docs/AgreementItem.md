# AgreementItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product** | [**list[ProductRef]**](ProductRef.md) | The list of products indirectly referred by this agreement item (since an agreement item refers primarily to product offerings) | [optional] 
**product_offering** | [**list[ProductOfferingRef]**](ProductOfferingRef.md) | The list of product offerings referred by this agreement item | [optional] 
**term_or_condition** | [**list[AgreementTermOrCondition]**](AgreementTermOrCondition.md) |  | [optional] 
**base_type** | **str** | When sub-classing, this defines the super-class | [optional] 
**schema_location** | **str** | A URI to a JSON-Schema file that defines additional attributes and relationships | [optional] 
**type** | **str** | When sub-classing, this defines the sub-class entity name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


