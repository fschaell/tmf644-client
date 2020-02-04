# SpecificationCharacteristicValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** | If true, the Boolean Indicates if the value is the default value for a characteristic | [optional] 
**range_interval** | **str** | An indicator that specifies the inclusion or exclusion of the valueFrom and valueTo attributes. If applicable, possible values are \&quot;open\&quot;, \&quot;closed\&quot;, \&quot;closedBottom\&quot; and \&quot;closedTop\&quot;. | [optional] 
**regex** | **str** | A regular expression constraint for given value | [optional] 
**unit_of_measure** | **str** | unit of measure for the valueCould be minutes, GB, etc | [optional] 
**value_from** | **int** | The low range value that a characteristic can take on | [optional] 
**value_to** | **int** | The upper range value that a characteristic can take on | [optional] 
**value_type** | **str** | A kind of value that the characteristic value can take on, such as numeric, text and so forth | [optional] 
**valid_for** | [**TimePeriod**](TimePeriod.md) | The period for which this object is valid | [optional] 
**value** | [**Any**](Any.md) | the  value that the characteristic can take on. | [optional] 
**base_type** | **str** | When sub-classing, this defines the super-class | [optional] 
**schema_location** | **str** | A URI to a JSON-Schema file that defines additional attributes and relationships | [optional] 
**type** | **str** | When sub-classing, this defines the sub-class entity name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


