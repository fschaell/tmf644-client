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


class PartyPrivacyAgreementCreate(object):
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
        'agreement_type': 'str',
        'description': 'str',
        'document_number': 'int',
        'initial_date': 'datetime',
        'name': 'str',
        'statement_of_intent': 'str',
        'status': 'str',
        'version': 'str',
        'agreement_authorization': 'list[AgreementAuthorization]',
        'agreement_item': 'list[AgreementItem]',
        'agreement_period': 'TimePeriod',
        'agreement_specification': 'AgreementSpecificationRef',
        'associated_agreement': 'list[AgreementRef]',
        'characteristic': 'list[Characteristic]',
        'completion_date': 'TimePeriod',
        'engaged_party_role': 'list[RelatedParty]',
        'party_privacy_profile': 'list[PartyPrivacyProfileRef]',
        'party_privacy_profile_characteristic': 'list[PartyPrivacyProfileCharacteristic]',
        'base_type': 'str',
        'schema_location': 'str',
        'type': 'str'
    }

    attribute_map = {
        'agreement_type': 'agreementType',
        'description': 'description',
        'document_number': 'documentNumber',
        'initial_date': 'initialDate',
        'name': 'name',
        'statement_of_intent': 'statementOfIntent',
        'status': 'status',
        'version': 'version',
        'agreement_authorization': 'agreementAuthorization',
        'agreement_item': 'agreementItem',
        'agreement_period': 'agreementPeriod',
        'agreement_specification': 'agreementSpecification',
        'associated_agreement': 'associatedAgreement',
        'characteristic': 'characteristic',
        'completion_date': 'completionDate',
        'engaged_party_role': 'engagedPartyRole',
        'party_privacy_profile': 'partyPrivacyProfile',
        'party_privacy_profile_characteristic': 'partyPrivacyProfileCharacteristic',
        'base_type': '@baseType',
        'schema_location': '@schemaLocation',
        'type': '@type'
    }

    def __init__(self, agreement_type=None, description=None, document_number=None, initial_date=None, name=None, statement_of_intent=None, status=None, version=None, agreement_authorization=None, agreement_item=None, agreement_period=None, agreement_specification=None, associated_agreement=None, characteristic=None, completion_date=None, engaged_party_role=None, party_privacy_profile=None, party_privacy_profile_characteristic=None, base_type=None, schema_location=None, type=None):  # noqa: E501
        """PartyPrivacyAgreementCreate - a model defined in Swagger"""  # noqa: E501

        self._agreement_type = None
        self._description = None
        self._document_number = None
        self._initial_date = None
        self._name = None
        self._statement_of_intent = None
        self._status = None
        self._version = None
        self._agreement_authorization = None
        self._agreement_item = None
        self._agreement_period = None
        self._agreement_specification = None
        self._associated_agreement = None
        self._characteristic = None
        self._completion_date = None
        self._engaged_party_role = None
        self._party_privacy_profile = None
        self._party_privacy_profile_characteristic = None
        self._base_type = None
        self._schema_location = None
        self._type = None
        self.discriminator = None

        self.agreement_type = agreement_type
        if description is not None:
            self.description = description
        if document_number is not None:
            self.document_number = document_number
        if initial_date is not None:
            self.initial_date = initial_date
        self.name = name
        if statement_of_intent is not None:
            self.statement_of_intent = statement_of_intent
        if status is not None:
            self.status = status
        if version is not None:
            self.version = version
        if agreement_authorization is not None:
            self.agreement_authorization = agreement_authorization
        self.agreement_item = agreement_item
        if agreement_period is not None:
            self.agreement_period = agreement_period
        if agreement_specification is not None:
            self.agreement_specification = agreement_specification
        if associated_agreement is not None:
            self.associated_agreement = associated_agreement
        if characteristic is not None:
            self.characteristic = characteristic
        if completion_date is not None:
            self.completion_date = completion_date
        self.engaged_party_role = engaged_party_role
        if party_privacy_profile is not None:
            self.party_privacy_profile = party_privacy_profile
        if party_privacy_profile_characteristic is not None:
            self.party_privacy_profile_characteristic = party_privacy_profile_characteristic
        if base_type is not None:
            self.base_type = base_type
        if schema_location is not None:
            self.schema_location = schema_location
        if type is not None:
            self.type = type

    @property
    def agreement_type(self):
        """Gets the agreement_type of this PartyPrivacyAgreementCreate.  # noqa: E501

        The type of the agreement. For example commercial  # noqa: E501

        :return: The agreement_type of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: str
        """
        return self._agreement_type

    @agreement_type.setter
    def agreement_type(self, agreement_type):
        """Sets the agreement_type of this PartyPrivacyAgreementCreate.

        The type of the agreement. For example commercial  # noqa: E501

        :param agreement_type: The agreement_type of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: str
        """
        if agreement_type is None:
            raise ValueError("Invalid value for `agreement_type`, must not be `None`")  # noqa: E501

        self._agreement_type = agreement_type

    @property
    def description(self):
        """Gets the description of this PartyPrivacyAgreementCreate.  # noqa: E501

        Narrative that explains the agreement and details about the it , such as why the agreement is taking place.  # noqa: E501

        :return: The description of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PartyPrivacyAgreementCreate.

        Narrative that explains the agreement and details about the it , such as why the agreement is taking place.  # noqa: E501

        :param description: The description of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def document_number(self):
        """Gets the document_number of this PartyPrivacyAgreementCreate.  # noqa: E501

        A reference number assigned to an Agreement that follows a prescribed numbering system.  # noqa: E501

        :return: The document_number of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: int
        """
        return self._document_number

    @document_number.setter
    def document_number(self, document_number):
        """Sets the document_number of this PartyPrivacyAgreementCreate.

        A reference number assigned to an Agreement that follows a prescribed numbering system.  # noqa: E501

        :param document_number: The document_number of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: int
        """

        self._document_number = document_number

    @property
    def initial_date(self):
        """Gets the initial_date of this PartyPrivacyAgreementCreate.  # noqa: E501

        Date at which the agreement was initialized  # noqa: E501

        :return: The initial_date of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: datetime
        """
        return self._initial_date

    @initial_date.setter
    def initial_date(self, initial_date):
        """Sets the initial_date of this PartyPrivacyAgreementCreate.

        Date at which the agreement was initialized  # noqa: E501

        :param initial_date: The initial_date of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: datetime
        """

        self._initial_date = initial_date

    @property
    def name(self):
        """Gets the name of this PartyPrivacyAgreementCreate.  # noqa: E501

        A human-readable name for the agreement  # noqa: E501

        :return: The name of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartyPrivacyAgreementCreate.

        A human-readable name for the agreement  # noqa: E501

        :param name: The name of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def statement_of_intent(self):
        """Gets the statement_of_intent of this PartyPrivacyAgreementCreate.  # noqa: E501

        An overview and goals of the Agreement  # noqa: E501

        :return: The statement_of_intent of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: str
        """
        return self._statement_of_intent

    @statement_of_intent.setter
    def statement_of_intent(self, statement_of_intent):
        """Sets the statement_of_intent of this PartyPrivacyAgreementCreate.

        An overview and goals of the Agreement  # noqa: E501

        :param statement_of_intent: The statement_of_intent of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: str
        """

        self._statement_of_intent = statement_of_intent

    @property
    def status(self):
        """Gets the status of this PartyPrivacyAgreementCreate.  # noqa: E501

        The current status of the agreement. Typical values are: in process, approved and rejected  # noqa: E501

        :return: The status of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PartyPrivacyAgreementCreate.

        The current status of the agreement. Typical values are: in process, approved and rejected  # noqa: E501

        :param status: The status of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def version(self):
        """Gets the version of this PartyPrivacyAgreementCreate.  # noqa: E501

        A string identifying the version of the agreement  # noqa: E501

        :return: The version of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PartyPrivacyAgreementCreate.

        A string identifying the version of the agreement  # noqa: E501

        :param version: The version of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def agreement_authorization(self):
        """Gets the agreement_authorization of this PartyPrivacyAgreementCreate.  # noqa: E501


        :return: The agreement_authorization of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: list[AgreementAuthorization]
        """
        return self._agreement_authorization

    @agreement_authorization.setter
    def agreement_authorization(self, agreement_authorization):
        """Sets the agreement_authorization of this PartyPrivacyAgreementCreate.


        :param agreement_authorization: The agreement_authorization of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: list[AgreementAuthorization]
        """

        self._agreement_authorization = agreement_authorization

    @property
    def agreement_item(self):
        """Gets the agreement_item of this PartyPrivacyAgreementCreate.  # noqa: E501


        :return: The agreement_item of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: list[AgreementItem]
        """
        return self._agreement_item

    @agreement_item.setter
    def agreement_item(self, agreement_item):
        """Sets the agreement_item of this PartyPrivacyAgreementCreate.


        :param agreement_item: The agreement_item of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: list[AgreementItem]
        """
        if agreement_item is None:
            raise ValueError("Invalid value for `agreement_item`, must not be `None`")  # noqa: E501

        self._agreement_item = agreement_item

    @property
    def agreement_period(self):
        """Gets the agreement_period of this PartyPrivacyAgreementCreate.  # noqa: E501

        The time period during which the Agreement is in effect.  # noqa: E501

        :return: The agreement_period of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: TimePeriod
        """
        return self._agreement_period

    @agreement_period.setter
    def agreement_period(self, agreement_period):
        """Sets the agreement_period of this PartyPrivacyAgreementCreate.

        The time period during which the Agreement is in effect.  # noqa: E501

        :param agreement_period: The agreement_period of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: TimePeriod
        """

        self._agreement_period = agreement_period

    @property
    def agreement_specification(self):
        """Gets the agreement_specification of this PartyPrivacyAgreementCreate.  # noqa: E501


        :return: The agreement_specification of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: AgreementSpecificationRef
        """
        return self._agreement_specification

    @agreement_specification.setter
    def agreement_specification(self, agreement_specification):
        """Sets the agreement_specification of this PartyPrivacyAgreementCreate.


        :param agreement_specification: The agreement_specification of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: AgreementSpecificationRef
        """

        self._agreement_specification = agreement_specification

    @property
    def associated_agreement(self):
        """Gets the associated_agreement of this PartyPrivacyAgreementCreate.  # noqa: E501


        :return: The associated_agreement of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: list[AgreementRef]
        """
        return self._associated_agreement

    @associated_agreement.setter
    def associated_agreement(self, associated_agreement):
        """Sets the associated_agreement of this PartyPrivacyAgreementCreate.


        :param associated_agreement: The associated_agreement of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: list[AgreementRef]
        """

        self._associated_agreement = associated_agreement

    @property
    def characteristic(self):
        """Gets the characteristic of this PartyPrivacyAgreementCreate.  # noqa: E501


        :return: The characteristic of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: list[Characteristic]
        """
        return self._characteristic

    @characteristic.setter
    def characteristic(self, characteristic):
        """Sets the characteristic of this PartyPrivacyAgreementCreate.


        :param characteristic: The characteristic of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: list[Characteristic]
        """

        self._characteristic = characteristic

    @property
    def completion_date(self):
        """Gets the completion_date of this PartyPrivacyAgreementCreate.  # noqa: E501

        Date at which the agreement is completed  # noqa: E501

        :return: The completion_date of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: TimePeriod
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this PartyPrivacyAgreementCreate.

        Date at which the agreement is completed  # noqa: E501

        :param completion_date: The completion_date of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: TimePeriod
        """

        self._completion_date = completion_date

    @property
    def engaged_party_role(self):
        """Gets the engaged_party_role of this PartyPrivacyAgreementCreate.  # noqa: E501


        :return: The engaged_party_role of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: list[RelatedParty]
        """
        return self._engaged_party_role

    @engaged_party_role.setter
    def engaged_party_role(self, engaged_party_role):
        """Sets the engaged_party_role of this PartyPrivacyAgreementCreate.


        :param engaged_party_role: The engaged_party_role of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: list[RelatedParty]
        """
        if engaged_party_role is None:
            raise ValueError("Invalid value for `engaged_party_role`, must not be `None`")  # noqa: E501

        self._engaged_party_role = engaged_party_role

    @property
    def party_privacy_profile(self):
        """Gets the party_privacy_profile of this PartyPrivacyAgreementCreate.  # noqa: E501

        The privacy profiles that are the subject of the agreement  # noqa: E501

        :return: The party_privacy_profile of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: list[PartyPrivacyProfileRef]
        """
        return self._party_privacy_profile

    @party_privacy_profile.setter
    def party_privacy_profile(self, party_privacy_profile):
        """Sets the party_privacy_profile of this PartyPrivacyAgreementCreate.

        The privacy profiles that are the subject of the agreement  # noqa: E501

        :param party_privacy_profile: The party_privacy_profile of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: list[PartyPrivacyProfileRef]
        """

        self._party_privacy_profile = party_privacy_profile

    @property
    def party_privacy_profile_characteristic(self):
        """Gets the party_privacy_profile_characteristic of this PartyPrivacyAgreementCreate.  # noqa: E501

        A list of (typically) high criticality characteristics whose chosen privacy rules are included in the agreement  # noqa: E501

        :return: The party_privacy_profile_characteristic of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: list[PartyPrivacyProfileCharacteristic]
        """
        return self._party_privacy_profile_characteristic

    @party_privacy_profile_characteristic.setter
    def party_privacy_profile_characteristic(self, party_privacy_profile_characteristic):
        """Sets the party_privacy_profile_characteristic of this PartyPrivacyAgreementCreate.

        A list of (typically) high criticality characteristics whose chosen privacy rules are included in the agreement  # noqa: E501

        :param party_privacy_profile_characteristic: The party_privacy_profile_characteristic of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: list[PartyPrivacyProfileCharacteristic]
        """

        self._party_privacy_profile_characteristic = party_privacy_profile_characteristic

    @property
    def base_type(self):
        """Gets the base_type of this PartyPrivacyAgreementCreate.  # noqa: E501

        When sub-classing, this defines the super-class  # noqa: E501

        :return: The base_type of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: str
        """
        return self._base_type

    @base_type.setter
    def base_type(self, base_type):
        """Sets the base_type of this PartyPrivacyAgreementCreate.

        When sub-classing, this defines the super-class  # noqa: E501

        :param base_type: The base_type of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: str
        """

        self._base_type = base_type

    @property
    def schema_location(self):
        """Gets the schema_location of this PartyPrivacyAgreementCreate.  # noqa: E501

        A URI to a JSON-Schema file that defines additional attributes and relationships  # noqa: E501

        :return: The schema_location of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: str
        """
        return self._schema_location

    @schema_location.setter
    def schema_location(self, schema_location):
        """Sets the schema_location of this PartyPrivacyAgreementCreate.

        A URI to a JSON-Schema file that defines additional attributes and relationships  # noqa: E501

        :param schema_location: The schema_location of this PartyPrivacyAgreementCreate.  # noqa: E501
        :type: str
        """

        self._schema_location = schema_location

    @property
    def type(self):
        """Gets the type of this PartyPrivacyAgreementCreate.  # noqa: E501

        When sub-classing, this defines the sub-class entity name  # noqa: E501

        :return: The type of this PartyPrivacyAgreementCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartyPrivacyAgreementCreate.

        When sub-classing, this defines the sub-class entity name  # noqa: E501

        :param type: The type of this PartyPrivacyAgreementCreate.  # noqa: E501
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
        if issubclass(PartyPrivacyAgreementCreate, dict):
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
        if not isinstance(other, PartyPrivacyAgreementCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
