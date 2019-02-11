# coding: utf-8

"""
    hcOS Developer Experience

    hcOS Developer Experience API  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from hcos_client.models.gender import Gender  # noqa: F401,E501


class SearchDocument(object):
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
        'kamioka_updated_at': 'datetime',
        'patient_root': 'str',
        'patient_extension': 'str',
        'patient_cluster_id': 'str',
        'patient_last_name': 'str',
        'patient_first_name': 'str',
        'patient_middle_name': 'str',
        'patient_birthdate': 'date',
        'patient_age_at_document_date': 'int',
        'patient_gender': 'Gender',
        'document_root': 'str',
        'document_extension': 'str',
        'document_type_root': 'str',
        'document_type_extension': 'str',
        'facility_root': 'str',
        'facility_extension': 'str',
        'document_kind_of_document_root': 'str',
        'document_kind_of_document_extension': 'str',
        'document_type_of_service_root': 'str',
        'document_type_of_service_extension': 'str',
        'document_subject_matter_domain_root': 'str',
        'document_subject_matter_domain_extension': 'str',
        'modality': 'str',
        'body_location': 'str',
        'source_created_at': 'datetime',
        'source_updated_at': 'datetime'
    }

    attribute_map = {
        'kamioka_updated_at': 'kamioka_updated_at',
        'patient_root': 'patient_root',
        'patient_extension': 'patient_extension',
        'patient_cluster_id': 'patient_cluster_id',
        'patient_last_name': 'patient_last_name',
        'patient_first_name': 'patient_first_name',
        'patient_middle_name': 'patient_middle_name',
        'patient_birthdate': 'patient_birthdate',
        'patient_age_at_document_date': 'patient_age_at_document_date',
        'patient_gender': 'patient_gender',
        'document_root': 'document_root',
        'document_extension': 'document_extension',
        'document_type_root': 'document_type_root',
        'document_type_extension': 'document_type_extension',
        'facility_root': 'facility_root',
        'facility_extension': 'facility_extension',
        'document_kind_of_document_root': 'document_kind_of_document_root',
        'document_kind_of_document_extension': 'document_kind_of_document_extension',
        'document_type_of_service_root': 'document_type_of_service_root',
        'document_type_of_service_extension': 'document_type_of_service_extension',
        'document_subject_matter_domain_root': 'document_subject_matter_domain_root',
        'document_subject_matter_domain_extension': 'document_subject_matter_domain_extension',
        'modality': 'modality',
        'body_location': 'body_location',
        'source_created_at': 'source_created_at',
        'source_updated_at': 'source_updated_at'
    }

    def __init__(self, kamioka_updated_at=None, patient_root=None, patient_extension=None, patient_cluster_id=None, patient_last_name=None, patient_first_name=None, patient_middle_name=None, patient_birthdate=None, patient_age_at_document_date=None, patient_gender=None, document_root=None, document_extension=None, document_type_root=None, document_type_extension=None, facility_root=None, facility_extension=None, document_kind_of_document_root=None, document_kind_of_document_extension=None, document_type_of_service_root=None, document_type_of_service_extension=None, document_subject_matter_domain_root=None, document_subject_matter_domain_extension=None, modality=None, body_location=None, source_created_at=None, source_updated_at=None):  # noqa: E501
        """SearchDocument - a model defined in Swagger"""  # noqa: E501
        self._kamioka_updated_at = None
        self._patient_root = None
        self._patient_extension = None
        self._patient_cluster_id = None
        self._patient_last_name = None
        self._patient_first_name = None
        self._patient_middle_name = None
        self._patient_birthdate = None
        self._patient_age_at_document_date = None
        self._patient_gender = None
        self._document_root = None
        self._document_extension = None
        self._document_type_root = None
        self._document_type_extension = None
        self._facility_root = None
        self._facility_extension = None
        self._document_kind_of_document_root = None
        self._document_kind_of_document_extension = None
        self._document_type_of_service_root = None
        self._document_type_of_service_extension = None
        self._document_subject_matter_domain_root = None
        self._document_subject_matter_domain_extension = None
        self._modality = None
        self._body_location = None
        self._source_created_at = None
        self._source_updated_at = None
        self.discriminator = None
        if kamioka_updated_at is not None:
            self.kamioka_updated_at = kamioka_updated_at
        if patient_root is not None:
            self.patient_root = patient_root
        if patient_extension is not None:
            self.patient_extension = patient_extension
        if patient_cluster_id is not None:
            self.patient_cluster_id = patient_cluster_id
        if patient_last_name is not None:
            self.patient_last_name = patient_last_name
        if patient_first_name is not None:
            self.patient_first_name = patient_first_name
        if patient_middle_name is not None:
            self.patient_middle_name = patient_middle_name
        if patient_birthdate is not None:
            self.patient_birthdate = patient_birthdate
        if patient_age_at_document_date is not None:
            self.patient_age_at_document_date = patient_age_at_document_date
        if patient_gender is not None:
            self.patient_gender = patient_gender
        if document_root is not None:
            self.document_root = document_root
        if document_extension is not None:
            self.document_extension = document_extension
        if document_type_root is not None:
            self.document_type_root = document_type_root
        if document_type_extension is not None:
            self.document_type_extension = document_type_extension
        if facility_root is not None:
            self.facility_root = facility_root
        if facility_extension is not None:
            self.facility_extension = facility_extension
        if document_kind_of_document_root is not None:
            self.document_kind_of_document_root = document_kind_of_document_root
        if document_kind_of_document_extension is not None:
            self.document_kind_of_document_extension = document_kind_of_document_extension
        if document_type_of_service_root is not None:
            self.document_type_of_service_root = document_type_of_service_root
        if document_type_of_service_extension is not None:
            self.document_type_of_service_extension = document_type_of_service_extension
        if document_subject_matter_domain_root is not None:
            self.document_subject_matter_domain_root = document_subject_matter_domain_root
        if document_subject_matter_domain_extension is not None:
            self.document_subject_matter_domain_extension = document_subject_matter_domain_extension
        if modality is not None:
            self.modality = modality
        if body_location is not None:
            self.body_location = body_location
        if source_created_at is not None:
            self.source_created_at = source_created_at
        if source_updated_at is not None:
            self.source_updated_at = source_updated_at

    @property
    def kamioka_updated_at(self):
        """Gets the kamioka_updated_at of this SearchDocument.  # noqa: E501


        :return: The kamioka_updated_at of this SearchDocument.  # noqa: E501
        :rtype: datetime
        """
        return self._kamioka_updated_at

    @kamioka_updated_at.setter
    def kamioka_updated_at(self, kamioka_updated_at):
        """Sets the kamioka_updated_at of this SearchDocument.


        :param kamioka_updated_at: The kamioka_updated_at of this SearchDocument.  # noqa: E501
        :type: datetime
        """

        self._kamioka_updated_at = kamioka_updated_at

    @property
    def patient_root(self):
        """Gets the patient_root of this SearchDocument.  # noqa: E501


        :return: The patient_root of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._patient_root

    @patient_root.setter
    def patient_root(self, patient_root):
        """Sets the patient_root of this SearchDocument.


        :param patient_root: The patient_root of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._patient_root = patient_root

    @property
    def patient_extension(self):
        """Gets the patient_extension of this SearchDocument.  # noqa: E501


        :return: The patient_extension of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._patient_extension

    @patient_extension.setter
    def patient_extension(self, patient_extension):
        """Sets the patient_extension of this SearchDocument.


        :param patient_extension: The patient_extension of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._patient_extension = patient_extension

    @property
    def patient_cluster_id(self):
        """Gets the patient_cluster_id of this SearchDocument.  # noqa: E501


        :return: The patient_cluster_id of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._patient_cluster_id

    @patient_cluster_id.setter
    def patient_cluster_id(self, patient_cluster_id):
        """Sets the patient_cluster_id of this SearchDocument.


        :param patient_cluster_id: The patient_cluster_id of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._patient_cluster_id = patient_cluster_id

    @property
    def patient_last_name(self):
        """Gets the patient_last_name of this SearchDocument.  # noqa: E501


        :return: The patient_last_name of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._patient_last_name

    @patient_last_name.setter
    def patient_last_name(self, patient_last_name):
        """Sets the patient_last_name of this SearchDocument.


        :param patient_last_name: The patient_last_name of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._patient_last_name = patient_last_name

    @property
    def patient_first_name(self):
        """Gets the patient_first_name of this SearchDocument.  # noqa: E501


        :return: The patient_first_name of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._patient_first_name

    @patient_first_name.setter
    def patient_first_name(self, patient_first_name):
        """Sets the patient_first_name of this SearchDocument.


        :param patient_first_name: The patient_first_name of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._patient_first_name = patient_first_name

    @property
    def patient_middle_name(self):
        """Gets the patient_middle_name of this SearchDocument.  # noqa: E501


        :return: The patient_middle_name of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._patient_middle_name

    @patient_middle_name.setter
    def patient_middle_name(self, patient_middle_name):
        """Sets the patient_middle_name of this SearchDocument.


        :param patient_middle_name: The patient_middle_name of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._patient_middle_name = patient_middle_name

    @property
    def patient_birthdate(self):
        """Gets the patient_birthdate of this SearchDocument.  # noqa: E501


        :return: The patient_birthdate of this SearchDocument.  # noqa: E501
        :rtype: date
        """
        return self._patient_birthdate

    @patient_birthdate.setter
    def patient_birthdate(self, patient_birthdate):
        """Sets the patient_birthdate of this SearchDocument.


        :param patient_birthdate: The patient_birthdate of this SearchDocument.  # noqa: E501
        :type: date
        """

        self._patient_birthdate = patient_birthdate

    @property
    def patient_age_at_document_date(self):
        """Gets the patient_age_at_document_date of this SearchDocument.  # noqa: E501


        :return: The patient_age_at_document_date of this SearchDocument.  # noqa: E501
        :rtype: int
        """
        return self._patient_age_at_document_date

    @patient_age_at_document_date.setter
    def patient_age_at_document_date(self, patient_age_at_document_date):
        """Sets the patient_age_at_document_date of this SearchDocument.


        :param patient_age_at_document_date: The patient_age_at_document_date of this SearchDocument.  # noqa: E501
        :type: int
        """

        self._patient_age_at_document_date = patient_age_at_document_date

    @property
    def patient_gender(self):
        """Gets the patient_gender of this SearchDocument.  # noqa: E501


        :return: The patient_gender of this SearchDocument.  # noqa: E501
        :rtype: Gender
        """
        return self._patient_gender

    @patient_gender.setter
    def patient_gender(self, patient_gender):
        """Sets the patient_gender of this SearchDocument.


        :param patient_gender: The patient_gender of this SearchDocument.  # noqa: E501
        :type: Gender
        """

        self._patient_gender = patient_gender

    @property
    def document_root(self):
        """Gets the document_root of this SearchDocument.  # noqa: E501


        :return: The document_root of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_root

    @document_root.setter
    def document_root(self, document_root):
        """Sets the document_root of this SearchDocument.


        :param document_root: The document_root of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._document_root = document_root

    @property
    def document_extension(self):
        """Gets the document_extension of this SearchDocument.  # noqa: E501


        :return: The document_extension of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_extension

    @document_extension.setter
    def document_extension(self, document_extension):
        """Sets the document_extension of this SearchDocument.


        :param document_extension: The document_extension of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._document_extension = document_extension

    @property
    def document_type_root(self):
        """Gets the document_type_root of this SearchDocument.  # noqa: E501


        :return: The document_type_root of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_type_root

    @document_type_root.setter
    def document_type_root(self, document_type_root):
        """Sets the document_type_root of this SearchDocument.


        :param document_type_root: The document_type_root of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._document_type_root = document_type_root

    @property
    def document_type_extension(self):
        """Gets the document_type_extension of this SearchDocument.  # noqa: E501


        :return: The document_type_extension of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_type_extension

    @document_type_extension.setter
    def document_type_extension(self, document_type_extension):
        """Sets the document_type_extension of this SearchDocument.


        :param document_type_extension: The document_type_extension of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._document_type_extension = document_type_extension

    @property
    def facility_root(self):
        """Gets the facility_root of this SearchDocument.  # noqa: E501


        :return: The facility_root of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._facility_root

    @facility_root.setter
    def facility_root(self, facility_root):
        """Sets the facility_root of this SearchDocument.


        :param facility_root: The facility_root of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._facility_root = facility_root

    @property
    def facility_extension(self):
        """Gets the facility_extension of this SearchDocument.  # noqa: E501


        :return: The facility_extension of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._facility_extension

    @facility_extension.setter
    def facility_extension(self, facility_extension):
        """Sets the facility_extension of this SearchDocument.


        :param facility_extension: The facility_extension of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._facility_extension = facility_extension

    @property
    def document_kind_of_document_root(self):
        """Gets the document_kind_of_document_root of this SearchDocument.  # noqa: E501


        :return: The document_kind_of_document_root of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_kind_of_document_root

    @document_kind_of_document_root.setter
    def document_kind_of_document_root(self, document_kind_of_document_root):
        """Sets the document_kind_of_document_root of this SearchDocument.


        :param document_kind_of_document_root: The document_kind_of_document_root of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._document_kind_of_document_root = document_kind_of_document_root

    @property
    def document_kind_of_document_extension(self):
        """Gets the document_kind_of_document_extension of this SearchDocument.  # noqa: E501


        :return: The document_kind_of_document_extension of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_kind_of_document_extension

    @document_kind_of_document_extension.setter
    def document_kind_of_document_extension(self, document_kind_of_document_extension):
        """Sets the document_kind_of_document_extension of this SearchDocument.


        :param document_kind_of_document_extension: The document_kind_of_document_extension of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._document_kind_of_document_extension = document_kind_of_document_extension

    @property
    def document_type_of_service_root(self):
        """Gets the document_type_of_service_root of this SearchDocument.  # noqa: E501


        :return: The document_type_of_service_root of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_type_of_service_root

    @document_type_of_service_root.setter
    def document_type_of_service_root(self, document_type_of_service_root):
        """Sets the document_type_of_service_root of this SearchDocument.


        :param document_type_of_service_root: The document_type_of_service_root of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._document_type_of_service_root = document_type_of_service_root

    @property
    def document_type_of_service_extension(self):
        """Gets the document_type_of_service_extension of this SearchDocument.  # noqa: E501


        :return: The document_type_of_service_extension of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_type_of_service_extension

    @document_type_of_service_extension.setter
    def document_type_of_service_extension(self, document_type_of_service_extension):
        """Sets the document_type_of_service_extension of this SearchDocument.


        :param document_type_of_service_extension: The document_type_of_service_extension of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._document_type_of_service_extension = document_type_of_service_extension

    @property
    def document_subject_matter_domain_root(self):
        """Gets the document_subject_matter_domain_root of this SearchDocument.  # noqa: E501


        :return: The document_subject_matter_domain_root of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_subject_matter_domain_root

    @document_subject_matter_domain_root.setter
    def document_subject_matter_domain_root(self, document_subject_matter_domain_root):
        """Sets the document_subject_matter_domain_root of this SearchDocument.


        :param document_subject_matter_domain_root: The document_subject_matter_domain_root of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._document_subject_matter_domain_root = document_subject_matter_domain_root

    @property
    def document_subject_matter_domain_extension(self):
        """Gets the document_subject_matter_domain_extension of this SearchDocument.  # noqa: E501


        :return: The document_subject_matter_domain_extension of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_subject_matter_domain_extension

    @document_subject_matter_domain_extension.setter
    def document_subject_matter_domain_extension(self, document_subject_matter_domain_extension):
        """Sets the document_subject_matter_domain_extension of this SearchDocument.


        :param document_subject_matter_domain_extension: The document_subject_matter_domain_extension of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._document_subject_matter_domain_extension = document_subject_matter_domain_extension

    @property
    def modality(self):
        """Gets the modality of this SearchDocument.  # noqa: E501


        :return: The modality of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._modality

    @modality.setter
    def modality(self, modality):
        """Sets the modality of this SearchDocument.


        :param modality: The modality of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._modality = modality

    @property
    def body_location(self):
        """Gets the body_location of this SearchDocument.  # noqa: E501


        :return: The body_location of this SearchDocument.  # noqa: E501
        :rtype: str
        """
        return self._body_location

    @body_location.setter
    def body_location(self, body_location):
        """Sets the body_location of this SearchDocument.


        :param body_location: The body_location of this SearchDocument.  # noqa: E501
        :type: str
        """

        self._body_location = body_location

    @property
    def source_created_at(self):
        """Gets the source_created_at of this SearchDocument.  # noqa: E501


        :return: The source_created_at of this SearchDocument.  # noqa: E501
        :rtype: datetime
        """
        return self._source_created_at

    @source_created_at.setter
    def source_created_at(self, source_created_at):
        """Sets the source_created_at of this SearchDocument.


        :param source_created_at: The source_created_at of this SearchDocument.  # noqa: E501
        :type: datetime
        """

        self._source_created_at = source_created_at

    @property
    def source_updated_at(self):
        """Gets the source_updated_at of this SearchDocument.  # noqa: E501


        :return: The source_updated_at of this SearchDocument.  # noqa: E501
        :rtype: datetime
        """
        return self._source_updated_at

    @source_updated_at.setter
    def source_updated_at(self, source_updated_at):
        """Sets the source_updated_at of this SearchDocument.


        :param source_updated_at: The source_updated_at of this SearchDocument.  # noqa: E501
        :type: datetime
        """

        self._source_updated_at = source_updated_at

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
        if issubclass(SearchDocument, dict):
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
        if not isinstance(other, SearchDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
