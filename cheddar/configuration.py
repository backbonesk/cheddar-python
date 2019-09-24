# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import os

from .environment import Environment
from .errors import ConfigurationError


class Configuration(object):
    def __init__(self, environment, key, secret, *args, **kwargs):
        self.environment = Environment.parse(environment)

        if key == "":
            raise ConfigurationError("Missing public key")
        else:
            self.key = key

        if secret == "":
            raise ConfigurationError("Missing secret")
        else:
            self.secret = secret

        self.timeout = kwargs.get("timeout", 30)
        self.os_environ = kwargs.get("os_environ", os.environ)
