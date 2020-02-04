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


class PartyPrivacyAgreementRef(object):
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
        'href': 'str',
        'name': 'str',
        'base_type': 'str',
        'schema_location': 'str',
        'type': 'str',
        'referred_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'href': 'href',
        'name': 'name',
        'base_type': '@baseType',
        'schema_location': '@schemaLocation',
        'type': '@type',
        'referred_type': '@referredType'
    }

    def __init__(self, id=None, href=None, name=None, base_type=None, schema_location=None, type=None, referred_type=None):  # noqa: E501
        """PartyPrivacyAgreementRef - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._href = None
        self._name = None
        self._base_type = None
        self._schema_location = None
        self._type = None
        self._referred_type = None
        self.discriminator = None

        self.id = id
        if href is not None:
            self.href = href
        if name is not None:
            self.name = name
        if base_type is not None:
            self.base_type = base_type
        if schema_location is not None:
            self.schema_location = schema_location
        if type is not None:
            self.type = type
        if referred_type is not None:
            self.referred_type = referred_type

    @property
    def id(self):
        """Gets the id of this PartyPrivacyAgreementRef.  # noqa: E501

        Unique identifier of a related entity.  # noqa: E501

        :return: The id of this PartyPrivacyAgreementRef.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PartyPrivacyAgreementRef.

        Unique identifier of a related entity.  # noqa: E501

        :param id: The id of this PartyPrivacyAgreementRef.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def href(self):
        """Gets the href of this PartyPrivacyAgreementRef.  # noqa: E501

        Reference of the related entity.  # noqa: E501

        :return: The href of this PartyPrivacyAgreementRef.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this PartyPrivacyAgreementRef.

        Reference of the related entity.  # noqa: E501

        :param href: The href of this PartyPrivacyAgreementRef.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def name(self):
        """Gets the name of this PartyPrivacyAgreementRef.  # noqa: E501

        Name of the related entity.  # noqa: E501

        :return: The name of this PartyPrivacyAgreementRef.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartyPrivacyAgreementRef.

        Name of the related entity.  # noqa: E501

        :param name: The name of this PartyPrivacyAgreementRef.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def base_type(self):
        """Gets the base_type of this PartyPrivacyAgreementRef.  # noqa: E501

        When sub-classing, this defines the super-class  # noqa: E501

        :return: The base_type of this PartyPrivacyAgreementRef.  # noqa: E501
        :rtype: str
        """
        return self._base_type

    @base_type.setter
    def base_type(self, base_type):
        """Sets the base_type of this PartyPrivacyAgreementRef.

        When sub-classing, this defines the super-class  # noqa: E501

        :param base_type: The base_type of this PartyPrivacyAgreementRef.  # noqa: E501
        :type: str
        """

        self._base_type = base_type

    @property
    def schema_location(self):
        """Gets the schema_location of this PartyPrivacyAgreementRef.  # noqa: E501

        A URI to a JSON-Schema file that defines additional attributes and relationships  # noqa: E501

        :return: The schema_location of this PartyPrivacyAgreementRef.  # noqa: E501
        :rtype: str
        """
        return self._schema_location

    @schema_location.setter
    def schema_location(self, schema_location):
        """Sets the schema_location of this PartyPrivacyAgreementRef.

        A URI to a JSON-Schema file that defines additional attributes and relationships  # noqa: E501

        :param schema_location: The schema_location of this PartyPrivacyAgreementRef.  # noqa: E501
        :type: str
        """

        self._schema_location = schema_location

    @property
    def type(self):
        """Gets the type of this PartyPrivacyAgreementRef.  # noqa: E501

        When sub-classing, this defines the sub-class entity name  # noqa: E501

        :return: The type of this PartyPrivacyAgreementRef.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartyPrivacyAgreementRef.

        When sub-classing, this defines the sub-class entity name  # noqa: E501

        :param type: The type of this PartyPrivacyAgreementRef.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def referred_type(self):
        """Gets the referred_type of this PartyPrivacyAgreementRef.  # noqa: E501

        The actual type of the target instance when needed for disambiguation.  # noqa: E501

        :return: The referred_type of this PartyPrivacyAgreementRef.  # noqa: E501
        :rtype: str
        """
        return self._referred_type

    @referred_type.setter
    def referred_type(self, referred_type):
        """Sets the referred_type of this PartyPrivacyAgreementRef.

        The actual type of the target instance when needed for disambiguation.  # noqa: E501

        :param referred_type: The referred_type of this PartyPrivacyAgreementRef.  # noqa: E501
        :type: str
        """

        self._referred_type = referred_type

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
        if issubclass(PartyPrivacyAgreementRef, dict):
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
        if not isinstance(other, PartyPrivacyAgreementRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
