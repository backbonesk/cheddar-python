# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class CheddarError(Exception):
    def __init__(self, message=None, http_body=None, http_status=None):
        super(CheddarError, self).__init__(message)

        self.http_body = http_body
        self.http_status = http_status


class ConfigurationError(CheddarError):
    pass


class AuthenticationError(CheddarError):
    pass


class APIError(CheddarError):
    pass


class APIConnectionError(APIError):
    pass


class MessageIntegrityError(CheddarError):
    pass
