# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from .errors import MessageIntegrityError


class Messages(object):
    def __init__(self, client):
        self.requestor = client.requestor

    def validate(self, uuid, signature):
        if signature == self.requestor.sign(uuid):
            return True

        raise MessageIntegrityError(
            "Signature %s for UUID %s is incorrect. Message is not to be trusted"
            % (signature, uuid)
        )
