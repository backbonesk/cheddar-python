# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Currency(object):
    CZK = "CZK"
    DKK = "DKK"
    EUR = "EUR"
    GBP = "GBP"
    HUF = "HUF"
    CHF = "CHF"
    PLN = "PLN"
    USD = "USD"

    def __init__(self, name, alpha_code, numeric_code):
        self.name = name
        self.alpha_codde = alpha_code
        self.numeric_code = numeric_code
