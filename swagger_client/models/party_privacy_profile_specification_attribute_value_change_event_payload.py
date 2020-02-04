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


class PartyPrivacyProfileSpecificationAttributeValueChangeEventPayload(object):
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
        'party_privacy_profile_specification': 'PartyPrivacyProfileSpecification'
    }

    attribute_map = {
        'party_privacy_profile_specification': 'partyPrivacyProfileSpecification'
    }

    def __init__(self, party_privacy_profile_specification=None):  # noqa: E501
        """PartyPrivacyProfileSpecificationAttributeValueChangeEventPayload - a model defined in Swagger"""  # noqa: E501

        self._party_privacy_profile_specification = None
        self.discriminator = None

        if party_privacy_profile_specification is not None:
            self.party_privacy_profile_specification = party_privacy_profile_specification

    @property
    def party_privacy_profile_specification(self):
        """Gets the party_privacy_profile_specification of this PartyPrivacyProfileSpecificationAttributeValueChangeEventPayload.  # noqa: E501

        The involved resource data for the event  # noqa: E501

        :return: The party_privacy_profile_specification of this PartyPrivacyProfileSpecificationAttributeValueChangeEventPayload.  # noqa: E501
        :rtype: PartyPrivacyProfileSpecification
        """
        return self._party_privacy_profile_specification

    @party_privacy_profile_specification.setter
    def party_privacy_profile_specification(self, party_privacy_profile_specification):
        """Sets the party_privacy_profile_specification of this PartyPrivacyProfileSpecificationAttributeValueChangeEventPayload.

        The involved resource data for the event  # noqa: E501

        :param party_privacy_profile_specification: The party_privacy_profile_specification of this PartyPrivacyProfileSpecificationAttributeValueChangeEventPayload.  # noqa: E501
        :type: PartyPrivacyProfileSpecification
        """

        self._party_privacy_profile_specification = party_privacy_profile_specification

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
        if issubclass(PartyPrivacyProfileSpecificationAttributeValueChangeEventPayload, dict):
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
        if not isinstance(other, PartyPrivacyProfileSpecificationAttributeValueChangeEventPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
