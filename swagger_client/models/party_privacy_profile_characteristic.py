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


class PartyPrivacyProfileCharacteristic(object):
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
        'id': 'str',
        'name': 'str',
        'privacy_usage_purpose': 'str',
        'value_type': 'str',
        'related_party': 'list[RelatedParty]',
        'value': 'Any',
        'base_type': 'str',
        'schema_location': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'privacy_usage_purpose': 'privacyUsagePurpose',
        'value_type': 'valueType',
        'related_party': 'relatedParty',
        'value': 'value',
        'base_type': '@baseType',
        'schema_location': '@schemaLocation',
        'type': '@type'
    }

    def __init__(self, id=None, name=None, privacy_usage_purpose=None, value_type=None, related_party=None, value=None, base_type=None, schema_location=None, type=None):  # noqa: E501
        """PartyPrivacyProfileCharacteristic - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._privacy_usage_purpose = None
        self._value_type = None
        self._related_party = None
        self._value = None
        self._base_type = None
        self._schema_location = None
        self._type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if privacy_usage_purpose is not None:
            self.privacy_usage_purpose = privacy_usage_purpose
        if value_type is not None:
            self.value_type = value_type
        if related_party is not None:
            self.related_party = related_party
        self.value = value
        if base_type is not None:
            self.base_type = base_type
        if schema_location is not None:
            self.schema_location = schema_location
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this PartyPrivacyProfileCharacteristic.  # noqa: E501


        :return: The id of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartyPrivacyProfileCharacteristic.


        :param id: The id of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PartyPrivacyProfileCharacteristic.  # noqa: E501

        Name of the characteristic  # noqa: E501

        :return: The name of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartyPrivacyProfileCharacteristic.

        Name of the characteristic  # noqa: E501

        :param name: The name of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def privacy_usage_purpose(self):
        """Gets the privacy_usage_purpose of this PartyPrivacyProfileCharacteristic.  # noqa: E501

        Defines the purpose authorized or refused for the characteristic (e.g. ADMIN, INFORMATION, MARKETING, RESEARCH, etc.  # noqa: E501

        :return: The privacy_usage_purpose of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :rtype: str
        """
        return self._privacy_usage_purpose

    @privacy_usage_purpose.setter
    def privacy_usage_purpose(self, privacy_usage_purpose):
        """Sets the privacy_usage_purpose of this PartyPrivacyProfileCharacteristic.

        Defines the purpose authorized or refused for the characteristic (e.g. ADMIN, INFORMATION, MARKETING, RESEARCH, etc.  # noqa: E501

        :param privacy_usage_purpose: The privacy_usage_purpose of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :type: str
        """

        self._privacy_usage_purpose = privacy_usage_purpose

    @property
    def value_type(self):
        """Gets the value_type of this PartyPrivacyProfileCharacteristic.  # noqa: E501

        Data type of the value of the characteristic  # noqa: E501

        :return: The value_type of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this PartyPrivacyProfileCharacteristic.

        Data type of the value of the characteristic  # noqa: E501

        :param value_type: The value_type of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :type: str
        """

        self._value_type = value_type

    @property
    def related_party(self):
        """Gets the related_party of this PartyPrivacyProfileCharacteristic.  # noqa: E501

        A list of parties to which the allowed use of the characteristic applies.  # noqa: E501

        :return: The related_party of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :rtype: list[RelatedParty]
        """
        return self._related_party

    @related_party.setter
    def related_party(self, related_party):
        """Sets the related_party of this PartyPrivacyProfileCharacteristic.

        A list of parties to which the allowed use of the characteristic applies.  # noqa: E501

        :param related_party: The related_party of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :type: list[RelatedParty]
        """

        self._related_party = related_party

    @property
    def value(self):
        """Gets the value of this PartyPrivacyProfileCharacteristic.  # noqa: E501

        The value of the characteristic  # noqa: E501

        :return: The value of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :rtype: Any
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PartyPrivacyProfileCharacteristic.

        The value of the characteristic  # noqa: E501

        :param value: The value of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :type: Any
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def base_type(self):
        """Gets the base_type of this PartyPrivacyProfileCharacteristic.  # noqa: E501

        When sub-classing, this defines the super-class  # noqa: E501

        :return: The base_type of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :rtype: str
        """
        return self._base_type

    @base_type.setter
    def base_type(self, base_type):
        """Sets the base_type of this PartyPrivacyProfileCharacteristic.

        When sub-classing, this defines the super-class  # noqa: E501

        :param base_type: The base_type of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :type: str
        """

        self._base_type = base_type

    @property
    def schema_location(self):
        """Gets the schema_location of this PartyPrivacyProfileCharacteristic.  # noqa: E501

        A URI to a JSON-Schema file that defines additional attributes and relationships  # noqa: E501

        :return: The schema_location of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :rtype: str
        """
        return self._schema_location

    @schema_location.setter
    def schema_location(self, schema_location):
        """Sets the schema_location of this PartyPrivacyProfileCharacteristic.

        A URI to a JSON-Schema file that defines additional attributes and relationships  # noqa: E501

        :param schema_location: The schema_location of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :type: str
        """

        self._schema_location = schema_location

    @property
    def type(self):
        """Gets the type of this PartyPrivacyProfileCharacteristic.  # noqa: E501

        When sub-classing, this defines the sub-class entity name  # noqa: E501

        :return: The type of this PartyPrivacyProfileCharacteristic.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartyPrivacyProfileCharacteristic.

        When sub-classing, this defines the sub-class entity name  # noqa: E501

        :param type: The type of this PartyPrivacyProfileCharacteristic.  # noqa: E501
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
        if issubclass(PartyPrivacyProfileCharacteristic, dict):
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
        if not isinstance(other, PartyPrivacyProfileCharacteristic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other