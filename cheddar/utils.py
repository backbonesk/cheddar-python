# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import json

from datetime import datetime, date
from decimal import Decimal


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.date().isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            return super(JSONEncoder, self).default(obj)
