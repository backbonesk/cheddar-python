# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from .resources.payment import Payment
from datetime import date


class Payments(object):
    def __init__(self, client):
        self.requestor = client.requestor
        self.configuration = client.configuration

    def details(self, uuid):
        status_code, response = self.requestor.request(
            "get", "/api/v1/payments/%s/" % (uuid)
        )

        return Payment(response)

    def create(self, service, metadata):
        data = {"service": service, "metadata": metadata}

        if "payer_ip_address" not in data["metadata"]:
            data["metadata"]["payer_ip_address"] = self.requestor.client_ip(
                self.configuration.os_environ
            )

        status_code, response = self.requestor.request(
            "post", "/api/v1/payments/", data
        )

        return Payment(response)

    def update(self, uuid, metadata):
        if "charge_on" in metadata and isinstance(metadata["charge_on"], date):
            metadata["charge_on"] = metadata["charge_on"].isoformat()

        data = {"metadata": metadata}

        status_code, response = self.requestor.request(
            "put", "/api/v1/payments/%s/" % uuid, data
        )

        return Payment(response)

    def refund(self, uuid, refund):
        data = {"refund": refund}

        status_code, response = self.requestor.request(
            "post", "/api/v1/payments/%s/refund" % uuid, data
        )

        return Payment(response)
