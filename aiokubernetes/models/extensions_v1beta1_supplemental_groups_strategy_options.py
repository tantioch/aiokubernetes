# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from aiokubernetes.models.extensions_v1beta1_id_range import ExtensionsV1beta1IDRange  # noqa: F401,E501


class ExtensionsV1beta1SupplementalGroupsStrategyOptions(object):
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
        'ranges': 'list[ExtensionsV1beta1IDRange]',
        'rule': 'str'
    }

    attribute_map = {
        'ranges': 'ranges',
        'rule': 'rule'
    }

    def __init__(self, ranges=None, rule=None):  # noqa: E501
        """ExtensionsV1beta1SupplementalGroupsStrategyOptions - a model defined in Swagger"""  # noqa: E501

        self._ranges = None
        self._rule = None
        self.discriminator = None

        if ranges is not None:
            self.ranges = ranges
        if rule is not None:
            self.rule = rule

    @property
    def ranges(self):
        """Gets the ranges of this ExtensionsV1beta1SupplementalGroupsStrategyOptions.  # noqa: E501

        Ranges are the allowed ranges of supplemental groups.  If you would like to force a single supplemental group then supply a single range with the same start and end.  # noqa: E501

        :return: The ranges of this ExtensionsV1beta1SupplementalGroupsStrategyOptions.  # noqa: E501
        :rtype: list[ExtensionsV1beta1IDRange]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """Sets the ranges of this ExtensionsV1beta1SupplementalGroupsStrategyOptions.

        Ranges are the allowed ranges of supplemental groups.  If you would like to force a single supplemental group then supply a single range with the same start and end.  # noqa: E501

        :param ranges: The ranges of this ExtensionsV1beta1SupplementalGroupsStrategyOptions.  # noqa: E501
        :type: list[ExtensionsV1beta1IDRange]
        """

        self._ranges = ranges

    @property
    def rule(self):
        """Gets the rule of this ExtensionsV1beta1SupplementalGroupsStrategyOptions.  # noqa: E501

        Rule is the strategy that will dictate what supplemental groups is used in the SecurityContext.  # noqa: E501

        :return: The rule of this ExtensionsV1beta1SupplementalGroupsStrategyOptions.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this ExtensionsV1beta1SupplementalGroupsStrategyOptions.

        Rule is the strategy that will dictate what supplemental groups is used in the SecurityContext.  # noqa: E501

        :param rule: The rule of this ExtensionsV1beta1SupplementalGroupsStrategyOptions.  # noqa: E501
        :type: str
        """

        self._rule = rule

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExtensionsV1beta1SupplementalGroupsStrategyOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
