# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.source_data import SourceData  # noqa: F401,E501
from swagger_server import util


class School(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, coverage_start_date: date=None, coverage_end_date: date=None, coverage_geographic_area: str=None, service_involvement: str=None, school_name: str=None, admission_type: str=None, contact_name: str=None, contact_number: str=None):  # noqa: E501
        """School - a model defined in Swagger

        :param coverage_start_date: The coverage_start_date of this School.  # noqa: E501
        :type coverage_start_date: date
        :param coverage_end_date: The coverage_end_date of this School.  # noqa: E501
        :type coverage_end_date: date
        :param coverage_geographic_area: The coverage_geographic_area of this School.  # noqa: E501
        :type coverage_geographic_area: str
        :param service_involvement: The service_involvement of this School.  # noqa: E501
        :type service_involvement: str
        :param school_name: The school_name of this School.  # noqa: E501
        :type school_name: str
        :param admission_type: The admission_type of this School.  # noqa: E501
        :type admission_type: str
        :param contact_name: The contact_name of this School.  # noqa: E501
        :type contact_name: str
        :param contact_number: The contact_number of this School.  # noqa: E501
        :type contact_number: str
        """
        self.swagger_types = {
            'coverage_start_date': date,
            'coverage_end_date': date,
            'coverage_geographic_area': str,
            'service_involvement': str,
            'school_name': str,
            'admission_type': str,
            'contact_name': str,
            'contact_number': str
        }

        self.attribute_map = {
            'coverage_start_date': 'coverageStartDate',
            'coverage_end_date': 'coverageEndDate',
            'coverage_geographic_area': 'coverageGeographicArea',
            'service_involvement': 'serviceInvolvement',
            'school_name': 'schoolName',
            'admission_type': 'admissionType',
            'contact_name': 'contactName',
            'contact_number': 'contactNumber'
        }
        self._coverage_start_date = coverage_start_date
        self._coverage_end_date = coverage_end_date
        self._coverage_geographic_area = coverage_geographic_area
        self._service_involvement = service_involvement
        self._school_name = school_name
        self._admission_type = admission_type
        self._contact_name = contact_name
        self._contact_number = contact_number

    @classmethod
    def from_dict(cls, dikt) -> 'School':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The School of this School.  # noqa: E501
        :rtype: School
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coverage_start_date(self) -> date:
        """Gets the coverage_start_date of this School.


        :return: The coverage_start_date of this School.
        :rtype: date
        """
        return self._coverage_start_date

    @coverage_start_date.setter
    def coverage_start_date(self, coverage_start_date: date):
        """Sets the coverage_start_date of this School.


        :param coverage_start_date: The coverage_start_date of this School.
        :type coverage_start_date: date
        """

        self._coverage_start_date = coverage_start_date

    @property
    def coverage_end_date(self) -> date:
        """Gets the coverage_end_date of this School.


        :return: The coverage_end_date of this School.
        :rtype: date
        """
        return self._coverage_end_date

    @coverage_end_date.setter
    def coverage_end_date(self, coverage_end_date: date):
        """Sets the coverage_end_date of this School.


        :param coverage_end_date: The coverage_end_date of this School.
        :type coverage_end_date: date
        """

        self._coverage_end_date = coverage_end_date

    @property
    def coverage_geographic_area(self) -> str:
        """Gets the coverage_geographic_area of this School.


        :return: The coverage_geographic_area of this School.
        :rtype: str
        """
        return self._coverage_geographic_area

    @coverage_geographic_area.setter
    def coverage_geographic_area(self, coverage_geographic_area: str):
        """Sets the coverage_geographic_area of this School.


        :param coverage_geographic_area: The coverage_geographic_area of this School.
        :type coverage_geographic_area: str
        """

        self._coverage_geographic_area = coverage_geographic_area

    @property
    def service_involvement(self) -> str:
        """Gets the service_involvement of this School.


        :return: The service_involvement of this School.
        :rtype: str
        """
        return self._service_involvement

    @service_involvement.setter
    def service_involvement(self, service_involvement: str):
        """Sets the service_involvement of this School.


        :param service_involvement: The service_involvement of this School.
        :type service_involvement: str
        """

        self._service_involvement = service_involvement

    @property
    def school_name(self) -> str:
        """Gets the school_name of this School.


        :return: The school_name of this School.
        :rtype: str
        """
        return self._school_name

    @school_name.setter
    def school_name(self, school_name: str):
        """Sets the school_name of this School.


        :param school_name: The school_name of this School.
        :type school_name: str
        """

        self._school_name = school_name

    @property
    def admission_type(self) -> str:
        """Gets the admission_type of this School.


        :return: The admission_type of this School.
        :rtype: str
        """
        return self._admission_type

    @admission_type.setter
    def admission_type(self, admission_type: str):
        """Sets the admission_type of this School.


        :param admission_type: The admission_type of this School.
        :type admission_type: str
        """

        self._admission_type = admission_type

    @property
    def contact_name(self) -> str:
        """Gets the contact_name of this School.


        :return: The contact_name of this School.
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name: str):
        """Sets the contact_name of this School.


        :param contact_name: The contact_name of this School.
        :type contact_name: str
        """

        self._contact_name = contact_name

    @property
    def contact_number(self) -> str:
        """Gets the contact_number of this School.


        :return: The contact_number of this School.
        :rtype: str
        """
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number: str):
        """Sets the contact_number of this School.


        :param contact_number: The contact_number of this School.
        :type contact_number: str
        """

        self._contact_number = contact_number