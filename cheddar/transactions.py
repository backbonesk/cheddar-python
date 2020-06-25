# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from .resources.transaction import Transaction, TransactionResponse


class Transactions(object):
    def __init__(self, client):
        self.requestor = client.requestor
        self.configuration = client.configuration

    def all(self, page=None, limit=None, before=None, after=None):
        filters = {}

        if page:
            filters['page'] = page

        if limit:
            filters['limit'] = limit

        if before:
            filters['created_before'] = before.isoformat()

        if after:
            filters['created_after'] = after.isoformat()

        status_code, response = self.requestor.request("get", "/api/v1/transactions/", query=filters)

        return TransactionResponse(
            list(map(Transaction, response.get('transactions', []))),
            response.get('metadata', {})
        )

    def detail(self, uuid):
        status_code, response = self.requestor.request("get", "/api/v1/transactions/%s" % uuid)
        return Transaction(response)
