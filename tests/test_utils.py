# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import cheddar
import json

from datetime import datetime, date
from decimal import Decimal


class TestJSONEncoder(object):
    def test_encoding_decimal(self):
        data = {"amount": Decimal("2.27")}
        output = json.dumps(data, cls=cheddar.utils.JSONEncoder)
        assert output == '{"amount": "2.27"}'

    def test_encoding_date(self):
        data = {"charge_on": date(2019, 5, 9)}
        output = json.dumps(data, cls=cheddar.utils.JSONEncoder)
        assert output == '{"charge_on": "2019-05-09"}'

    def test_encoding_datetime_as_date(self):
        data = {"charge_on": datetime(2019, 5, 9, 19, 32, 46)}
        output = json.dumps(data, cls=cheddar.utils.JSONEncoder)
        assert output == '{"charge_on": "2019-05-09"}'
