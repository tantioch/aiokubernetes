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

from aiokubernetes.models.v1beta1_custom_resource_subresource_scale import V1beta1CustomResourceSubresourceScale  # noqa: F401,E501


class V1beta1CustomResourceSubresources(object):
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
        'scale': 'V1beta1CustomResourceSubresourceScale',
        'status': 'object'
    }

    attribute_map = {
        'scale': 'scale',
        'status': 'status'
    }

    def __init__(self, scale=None, status=None):  # noqa: E501
        """V1beta1CustomResourceSubresources - a model defined in Swagger"""  # noqa: E501

        self._scale = None
        self._status = None
        self.discriminator = None

        if scale is not None:
            self.scale = scale
        if status is not None:
            self.status = status

    @property
    def scale(self):
        """Gets the scale of this V1beta1CustomResourceSubresources.  # noqa: E501

        Scale denotes the scale subresource for CustomResources  # noqa: E501

        :return: The scale of this V1beta1CustomResourceSubresources.  # noqa: E501
        :rtype: V1beta1CustomResourceSubresourceScale
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this V1beta1CustomResourceSubresources.

        Scale denotes the scale subresource for CustomResources  # noqa: E501

        :param scale: The scale of this V1beta1CustomResourceSubresources.  # noqa: E501
        :type: V1beta1CustomResourceSubresourceScale
        """

        self._scale = scale

    @property
    def status(self):
        """Gets the status of this V1beta1CustomResourceSubresources.  # noqa: E501

        Status denotes the status subresource for CustomResources  # noqa: E501

        :return: The status of this V1beta1CustomResourceSubresources.  # noqa: E501
        :rtype: object
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this V1beta1CustomResourceSubresources.

        Status denotes the status subresource for CustomResources  # noqa: E501

        :param status: The status of this V1beta1CustomResourceSubresources.  # noqa: E501
        :type: object
        """

        self._status = status

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
        if not isinstance(other, V1beta1CustomResourceSubresources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
