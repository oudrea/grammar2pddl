# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from g2lserver.models.base_model_ import Model
from g2lserver import util


class PipelineFeedbackResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, valid_pipelines: List[str]=None, invalid_pipelines: List[str]=None):  # noqa: E501
        """PipelineFeedbackResults - a model defined in Swagger

        :param valid_pipelines: The valid_pipelines of this PipelineFeedbackResults.  # noqa: E501
        :type valid_pipelines: List[str]
        :param invalid_pipelines: The invalid_pipelines of this PipelineFeedbackResults.  # noqa: E501
        :type invalid_pipelines: List[str]
        """
        self.swagger_types = {
            'valid_pipelines': List[str],
            'invalid_pipelines': List[str]
        }

        self.attribute_map = {
            'valid_pipelines': 'validPipelines',
            'invalid_pipelines': 'invalidPipelines'
        }

        self._valid_pipelines = valid_pipelines
        self._invalid_pipelines = invalid_pipelines

    @classmethod
    def from_dict(cls, dikt) -> 'PipelineFeedbackResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PipelineFeedbackResults of this PipelineFeedbackResults.  # noqa: E501
        :rtype: PipelineFeedbackResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def valid_pipelines(self) -> List[str]:
        """Gets the valid_pipelines of this PipelineFeedbackResults.


        :return: The valid_pipelines of this PipelineFeedbackResults.
        :rtype: List[str]
        """
        return self._valid_pipelines

    @valid_pipelines.setter
    def valid_pipelines(self, valid_pipelines: List[str]):
        """Sets the valid_pipelines of this PipelineFeedbackResults.


        :param valid_pipelines: The valid_pipelines of this PipelineFeedbackResults.
        :type valid_pipelines: List[str]
        """

        self._valid_pipelines = valid_pipelines

    @property
    def invalid_pipelines(self) -> List[str]:
        """Gets the invalid_pipelines of this PipelineFeedbackResults.


        :return: The invalid_pipelines of this PipelineFeedbackResults.
        :rtype: List[str]
        """
        return self._invalid_pipelines

    @invalid_pipelines.setter
    def invalid_pipelines(self, invalid_pipelines: List[str]):
        """Sets the invalid_pipelines of this PipelineFeedbackResults.


        :param invalid_pipelines: The invalid_pipelines of this PipelineFeedbackResults.
        :type invalid_pipelines: List[str]
        """

        self._invalid_pipelines = invalid_pipelines
