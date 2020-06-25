# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function


class Transaction(object):
    def __init__(self, data):
        self.uuid = data['uuid']
        self.type = data['type']
        self.payment_uuid = data['payment']
        self.bank_identifier = data['bank_identifier']

        self.variable_symbol = data['variable_symbol'] if 'variable_symbol' in data else None
        self.constant_symbol = data['constant_symbol'] if 'constant_symbol' in data else None
        self.specific_symbol = data['specific_symbol'] if 'specific_symbol' in data else None

        self.amount = data['amount']
        self.currency = data["currency"]

        self.iban = data['iban'] if 'iban' in data else None
        self.notes = data['notes'] if 'notes' in data else None
        self.description = data['description'] if 'description' in data else None

        self.booked_at = data['booked_at'] if 'booked_at' in data else None
        self.created_at = data['created_at'] if 'created_at' in data else None

    def __str__(self):
        return str(self.__dict__)


class TransactionResponse(object):
    class Metadata(object):
        def __init__(self, data):
            self.page = data.get('page')
            self.pages = data.get('pages')
            self.total = data.get('total')

    def __init__(self, transactions, metadata):
        self.transactions = transactions
        self.metadata = self.Metadata(metadata)
