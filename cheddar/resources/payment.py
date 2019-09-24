# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from ..errors import CheddarError
from .currency import Currency


class Payment(object):
    def __str__(self):
        return str(self.__dict__)

    def __init__(self, data):
        try:
            self.status = data["status"]["status"]

            self.uuid = data["uuid"]
            self.service = data["service"]["handle"]
            self.amount = data["amount"]
            self.refunded_amount = data["refunded_amount"]
            self.service_fee_amount = data["service_fee_amount"]
            self.variable_symbol = data["variable_symbol"]
            self.constant_symbol = data["constant_symbol"]
            self.currency = Currency(
                data["currency"]["name"],
                data["currency"]["alpha_code"],
                data["currency"]["numeric_code"],
            )

            self.periodicity = (
                data["periodicity"] if "periodicity" in data else 0
            )
            self.periodicity_no = (
                data["periodicity_no"] if "periodicity_no" in data else None
            )
            self.charge_on = data["charge_on"] if "charge_on" in data else None

            self.card_no = data["card_no"] if "card_no" in data else None
            self.card_expire_on = (
                data["card_expire_on"] if "card_expire_on" in data else None
            )

            self.transaction_identifier = (
                data["transaction_identifier"]
                if "transaction_identifier" in data
                else None
            )

            self._redirect_url = (
                data["redirect_url"] if "redirect_url" in data else None
            )
        except (KeyError, TypeError) as e:
            raise CheddarError(
                "Payment cannot be instantiated due to incorrect key: %s" % e
            )

    @property
    def redirect_url(self):
        if self.status != "none":
            raise CheddarError(
                "Further processing is not possible due to unprocessable status %s (The only valid payment status for further processing is 'none')"
                % self.status
            )

        if not self._redirect_url or not self.uuid:
            raise CheddarError(
                "Further processing is not possible due to incomplete payment object."
            )

        return self._redirect_url
