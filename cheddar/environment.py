# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function
from .errors import ConfigurationError


class Environment(object):
    def __init__(self, name, api_base_url):
        self.name = name
        self.api_base_url = api_base_url

    @staticmethod
    def parse(environment=None):
        if isinstance(environment, Environment) or environment is None:
            return environment
        else:
            raise ConfigurationError("Unable to process supplied environment")

    def __str__(self):
        return self.name


Environment.Sandbox = Environment(
    "sandbox", "https://sandbox.cheddarpayments.com"
)
Environment.Production = Environment(
    "production", "https://www.cheddarpayments.com"
)
