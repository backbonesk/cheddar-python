# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from .configuration import Configuration
from .errors import ConfigurationError
from .messages import Messages
from .payments import Payments
from .transactions import Transactions
from .requestor import Requestor
from .version import VERSION


class Cheddar(object):
    def __init__(self, configuration=None, **kwargs):
        if isinstance(configuration, Configuration):
            self.configuration = configuration
        else:
            raise ConfigurationError("Missing configuration object")

        self.version = VERSION
        self.requestor = Requestor(self)
        self.payments = Payments(self)
        self.messages = Messages(self)
        self.transactions = Transactions(self)

    def identifier(self):
        return "cheddar-python/%s" % self.version
