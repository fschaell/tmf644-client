# coding: utf-8

"""
    Privacy

    **TMF API Reference : TMF - 644 Privacy**  **Release : 19.0 - June 2019**  The Privacy Management API provides standardized mechanism for privacy profile specification, privacy profiles and privacy agreements such as creation, update, retrieval, deletion and notification of events.Privacy management API manages the following data resources:  **Privacy Profile specification** Privacy profile specification represents a description for privacy profiles.Main privacy profile specification attributes are its identifier, name, description, version, last update, lifecycle status, validity period, characteristics and their values, related parties, applicable roles.  **Privacy Profile** Privacy profile represents the set of Privacy settings defined for a Party.Main privacy profile attributes are its identifier, name, description, date of creation, status, validity period, privacy profile specification, characteristics values, agreement, the party who has agreed and the party which the privacy is applicable for, typically the same party represents both the aggreged by and applicable for. In case of minor privacy the applicable for party is the minor and the agreed party is the parent.  **Privacy Agreement** Privacy agreement represents the approval made by the Party about a Party Privacy Profile.Main privacy agreement attributes are its identifier, name, description, agreement period, initial date, completion date, document number, statement of intent, status, type, version, agreement specification, agreement items, engaged party, agreement authorization, characteristics, associated agreements, privacy profile and privacy profile characteristic values. Privacy management API performs the following operations on privacy profile specification, privacy profiles and privacy agreements: -Retrieval of a privacy profile specification, a privacy profile or a privacy agreement, or of a collection of them depending on filter criteria -Partial update of a privacy profile specification, a privacy profile or a privacy agreement -Creation of a privacy profile specification, a privacy profile or a privacy agreement -Deletion of a privacy profile specification, a privacy profile or a privacy agreement (for administration purposes)  **Notification of events:** -privacy profile specification create -privacy profile specification update -privacy profile specification delete -privacy profile create -privacy profile update -privacy profile delete -privacy agreement create -privacy agreement update   Copyright © TM Forum 2019. All Rights Reserved     # noqa: E501

    OpenAPI spec version: 4.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SpecificationCharacteristicValue(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_default': 'bool',
        'range_interval': 'str',
        'regex': 'str',
        'unit_of_measure': 'str',
        'value_from': 'int',
        'value_to': 'int',
        'value_type': 'str',
        'valid_for': 'TimePeriod',
        'value': 'Any',
        'base_type': 'str',
        'schema_location': 'str',
        'type': 'str'
    }

    attribute_map = {
        'is_default': 'isDefault',
        'range_interval': 'rangeInterval',
        'regex': 'regex',
        'unit_of_measure': 'unitOfMeasure',
        'value_from': 'valueFrom',
        'value_to': 'valueTo',
        'value_type': 'valueType',
        'valid_for': 'validFor',
        'value': 'value',
        'base_type': '@baseType',
        'schema_location': '@schemaLocation',
        'type': '@type'
    }

    def __init__(self, is_default=None, range_interval=None, regex=None, unit_of_measure=None, value_from=None, value_to=None, value_type=None, valid_for=None, value=None, base_type=None, schema_location=None, type=None):  # noqa: E501
        """SpecificationCharacteristicValue - a model defined in Swagger"""  # noqa: E501

        self._is_default = None
        self._range_interval = None
        self._regex = None
        self._unit_of_measure = None
        self._value_from = None
        self._value_to = None
        self._value_type = None
        self._valid_for = None
        self._value = None
        self._base_type = None
        self._schema_location = None
        self._type = None
        self.discriminator = None

        if is_default is not None:
            self.is_default = is_default
        if range_interval is not None:
            self.range_interval = range_interval
        if regex is not None:
            self.regex = regex
        if unit_of_measure is not None:
            self.unit_of_measure = unit_of_measure
        if value_from is not None:
            self.value_from = value_from
        if value_to is not None:
            self.value_to = value_to
        if value_type is not None:
            self.value_type = value_type
        if valid_for is not None:
            self.valid_for = valid_for
        if value is not None:
            self.value = value
        if base_type is not None:
            self.base_type = base_type
        if schema_location is not None:
            self.schema_location = schema_location
        if type is not None:
            self.type = type

    @property
    def is_default(self):
        """Gets the is_default of this SpecificationCharacteristicValue.  # noqa: E501

        If true, the Boolean Indicates if the value is the default value for a characteristic  # noqa: E501

        :return: The is_default of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this SpecificationCharacteristicValue.

        If true, the Boolean Indicates if the value is the default value for a characteristic  # noqa: E501

        :param is_default: The is_default of this SpecificationCharacteristicValue.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def range_interval(self):
        """Gets the range_interval of this SpecificationCharacteristicValue.  # noqa: E501

        An indicator that specifies the inclusion or exclusion of the valueFrom and valueTo attributes. If applicable, possible values are \"open\", \"closed\", \"closedBottom\" and \"closedTop\".  # noqa: E501

        :return: The range_interval of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: str
        """
        return self._range_interval

    @range_interval.setter
    def range_interval(self, range_interval):
        """Sets the range_interval of this SpecificationCharacteristicValue.

        An indicator that specifies the inclusion or exclusion of the valueFrom and valueTo attributes. If applicable, possible values are \"open\", \"closed\", \"closedBottom\" and \"closedTop\".  # noqa: E501

        :param range_interval: The range_interval of this SpecificationCharacteristicValue.  # noqa: E501
        :type: str
        """

        self._range_interval = range_interval

    @property
    def regex(self):
        """Gets the regex of this SpecificationCharacteristicValue.  # noqa: E501

        A regular expression constraint for given value  # noqa: E501

        :return: The regex of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this SpecificationCharacteristicValue.

        A regular expression constraint for given value  # noqa: E501

        :param regex: The regex of this SpecificationCharacteristicValue.  # noqa: E501
        :type: str
        """

        self._regex = regex

    @property
    def unit_of_measure(self):
        """Gets the unit_of_measure of this SpecificationCharacteristicValue.  # noqa: E501

        unit of measure for the valueCould be minutes, GB, etc  # noqa: E501

        :return: The unit_of_measure of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """Sets the unit_of_measure of this SpecificationCharacteristicValue.

        unit of measure for the valueCould be minutes, GB, etc  # noqa: E501

        :param unit_of_measure: The unit_of_measure of this SpecificationCharacteristicValue.  # noqa: E501
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def value_from(self):
        """Gets the value_from of this SpecificationCharacteristicValue.  # noqa: E501

        The low range value that a characteristic can take on  # noqa: E501

        :return: The value_from of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: int
        """
        return self._value_from

    @value_from.setter
    def value_from(self, value_from):
        """Sets the value_from of this SpecificationCharacteristicValue.

        The low range value that a characteristic can take on  # noqa: E501

        :param value_from: The value_from of this SpecificationCharacteristicValue.  # noqa: E501
        :type: int
        """

        self._value_from = value_from

    @property
    def value_to(self):
        """Gets the value_to of this SpecificationCharacteristicValue.  # noqa: E501

        The upper range value that a characteristic can take on  # noqa: E501

        :return: The value_to of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: int
        """
        return self._value_to

    @value_to.setter
    def value_to(self, value_to):
        """Sets the value_to of this SpecificationCharacteristicValue.

        The upper range value that a characteristic can take on  # noqa: E501

        :param value_to: The value_to of this SpecificationCharacteristicValue.  # noqa: E501
        :type: int
        """

        self._value_to = value_to

    @property
    def value_type(self):
        """Gets the value_type of this SpecificationCharacteristicValue.  # noqa: E501

        A kind of value that the characteristic value can take on, such as numeric, text and so forth  # noqa: E501

        :return: The value_type of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this SpecificationCharacteristicValue.

        A kind of value that the characteristic value can take on, such as numeric, text and so forth  # noqa: E501

        :param value_type: The value_type of this SpecificationCharacteristicValue.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

    @property
    def valid_for(self):
        """Gets the valid_for of this SpecificationCharacteristicValue.  # noqa: E501

        The period for which this object is valid  # noqa: E501

        :return: The valid_for of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: TimePeriod
        """
        return self._valid_for

    @valid_for.setter
    def valid_for(self, valid_for):
        """Sets the valid_for of this SpecificationCharacteristicValue.

        The period for which this object is valid  # noqa: E501

        :param valid_for: The valid_for of this SpecificationCharacteristicValue.  # noqa: E501
        :type: TimePeriod
        """

        self._valid_for = valid_for

    @property
    def value(self):
        """Gets the value of this SpecificationCharacteristicValue.  # noqa: E501

        the  value that the characteristic can take on.  # noqa: E501

        :return: The value of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: Any
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SpecificationCharacteristicValue.

        the  value that the characteristic can take on.  # noqa: E501

        :param value: The value of this SpecificationCharacteristicValue.  # noqa: E501
        :type: Any
        """

        self._value = value

    @property
    def base_type(self):
        """Gets the base_type of this SpecificationCharacteristicValue.  # noqa: E501

        When sub-classing, this defines the super-class  # noqa: E501

        :return: The base_type of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: str
        """
        return self._base_type

    @base_type.setter
    def base_type(self, base_type):
        """Sets the base_type of this SpecificationCharacteristicValue.

        When sub-classing, this defines the super-class  # noqa: E501

        :param base_type: The base_type of this SpecificationCharacteristicValue.  # noqa: E501
        :type: str
        """

        self._base_type = base_type

    @property
    def schema_location(self):
        """Gets the schema_location of this SpecificationCharacteristicValue.  # noqa: E501

        A URI to a JSON-Schema file that defines additional attributes and relationships  # noqa: E501

        :return: The schema_location of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: str
        """
        return self._schema_location

    @schema_location.setter
    def schema_location(self, schema_location):
        """Sets the schema_location of this SpecificationCharacteristicValue.

        A URI to a JSON-Schema file that defines additional attributes and relationships  # noqa: E501

        :param schema_location: The schema_location of this SpecificationCharacteristicValue.  # noqa: E501
        :type: str
        """

        self._schema_location = schema_location

    @property
    def type(self):
        """Gets the type of this SpecificationCharacteristicValue.  # noqa: E501

        When sub-classing, this defines the sub-class entity name  # noqa: E501

        :return: The type of this SpecificationCharacteristicValue.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SpecificationCharacteristicValue.

        When sub-classing, this defines the sub-class entity name  # noqa: E501

        :param type: The type of this SpecificationCharacteristicValue.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SpecificationCharacteristicValue, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SpecificationCharacteristicValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other