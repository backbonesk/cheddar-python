# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import json
import hmac
import sys

import requests

from hashlib import sha1
from .errors import APIConnectionError, APIError
from .utils import JSONEncoder

if sys.version_info[0] < 3:
    from urllib import urlencode
else:
    from urllib.parse import urlencode


class Requestor:
    def __init__(self, client):
        self.client = client
        self.configuration = self.client.configuration

    def request(self, method, endpoint_url, raw=None, query=None):
        if not raw:
            raw = {}

        data = json.dumps(raw, cls=JSONEncoder)
        headers = {
            "User-Agent": self.client.identifier(),
            "Content-Type": "application/json",
            "X-Key": self.configuration.key,
        }

        if query:
            headers["X-Signature"] = self.sign("%s;%s" % (endpoint_url + "?" + urlencode(query), data))
        else:
            headers["X-Signature"] = self.sign("%s;%s" % (endpoint_url, data))
        try:
            response = requests.request(
                method=method,
                url=self.configuration.environment.api_base_url + endpoint_url,
                headers=headers,
                data=data,
                timeout=self.configuration.timeout,
                params=query
            )
        except Exception as e:
            self._handle_request_error(e)

        if not (200 <= response.status_code < 300):
            try:
                data = response.json()
            except ValueError as e:
                raise APIError(
                    "Invalid JSON response from API: %s (%s)"
                    % (str(e), response.text),
                    response.text,
                    response.status_code,
                )

            try:
                error_message = data["error"]
            except (KeyError, TypeError):
                raise APIError(
                    "Invalid response object from API: %s (HTTP response code "
                    "was %d)" % (response.text, response.status_code),
                    response.text,
                    response.status_code,
                )

            raise APIError(
                "%s (%s)" % (error_message, data["developer_message"]),
                response.text,
                response.status_code,
            )

        try:
            data = response.json()
        except ValueError as e:
            raise APIError(
                "Invalid JSON response from API: %s (%s)"
                % (str(e), response.text),
                response.text,
                response.status_code,
            )

        return response.status_code, data

    def client_ip(self, environ):
        try:
            return environ["HTTP_X_FORWARDED_FOR"].split(",")[0].strip()
        except (KeyError, IndexError):
            pass

        try:
            return environ["HTTP_X_REAL_IP"]
        except KeyError:
            pass

        return environ.get("REMOTE_ADDR")

    def sign(self, data):
        return hmac.new(
            self.configuration.secret.encode("utf-8"),
            data.encode("utf-8"),
            sha1,
        ).hexdigest()

    def _handle_request_error(self, e):
        if isinstance(e, requests.exceptions.RequestException):
            err = "%s: %s" % (type(e).__name__, str(e))
        else:
            err = "A %s was raised" % (type(e).__name__,)

            if str(e):
                err += " with error message %s" % (str(e),)
            else:
                err += " with no error message"

        msg = "Network error: %s" % (err,)

        raise APIConnectionError(msg)
