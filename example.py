# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

import cheddar
import datetime
from decimal import Decimal

# client = cheddar.Cheddar(key="ARTF", secret="3d9209b97b0bc4acebc1f7b0616b04fd")
# client.sandbox(True)

cheddar_environment = cheddar.Environment(
    "development", "http://www.cheddar.test"
)
client = cheddar.Cheddar(
    cheddar.Configuration(
        # cheddar_environment, "ARTF", "3d9209b97b0bc4acebc1f7b0616b04fd"
        cheddar_environment,
        "SLAB",
        "12342a3cb967c8820a0e0b0812a2f691",
    )
)

print("Creating one-time payment...")

try:
    payment = client.payments.create(
        cheddar.Service.CARDPAY,
        {
            "currency": cheddar.Currency.EUR,
            "variable_symbol": "0000060827",
            "amount": Decimal(6.75),
            "description": "Objednavka na artforum.sk",
            "notification_url": "https://www.artforum.sk/api/v1/orders/listener",
            "payer_email": "pavol@sopko.sk",
            "payer_name": "Pavol Sopko",
            "return_url": "https://www.artforum.sk/nakup/spracuj/388d48ad-d9cd-40cc-8ac4-a0b0899df712",
        },
    )

    print(type(payment))
    print(payment.__class__)

    print(type(cheddar.Currency))
    print(type(cheddar.resources.currency.Currency))

    print("UUID: %s" % payment.uuid)
    print("Status: %s" % payment.status)
    print("Redirect URL: %s" % payment.redirect_url)
except cheddar.errors.CheddarError as e:
    print(e)

payment_uuid = payment.uuid

print("Updating one-time payment... (should end in error)")

try:
    payment = client.payments.update(payment_uuid, {"amount": 6})

    print(payment)
except cheddar.errors.CheddarError as e:
    print(e)

print("Creating periodical payment...")

try:
    payment = client.payments.create(
        cheddar.Service.COMFORTPAY,
        {
            "currency": cheddar.Currency.EUR,
            "variable_symbol": "0000060828",
            "amount": 6.75,
            "description": "Objednavka na artforum.sk",
            "notification_url": "https://www.artforum.sk/api/v1/orders/listener",
            "payer_email": "pavol@sopko.sk",
            "payer_name": "Pavol Sopko",
            "periodicity": 30,
            "return_url": "https://www.artforum.sk/nakup/spracuj/388d48ad-d9cd-40cc-8ac4-a0b0899df712",
        },
    )

    print("UUID: %s" % payment.uuid)
    print("Status: %s" % payment.status)
    print("Redirect URL: %s" % payment.redirect_url)
except cheddar.errors.CheddarError as e:
    print(e)

print("Updating periodical payment...")

payment_uuid = payment.uuid

try:
    resp = client.payments.update(
        payment_uuid,
        {"amount": 25.00, "charge_on": datetime.date(2019, 12, 1)},
    )

    print("UUID: %s" % resp.uuid)
    print("Status: %s" % resp.status)
    print("Amount: %s" % resp.amount)
    print("Charge on: %s" % resp.charge_on)
except cheddar.errors.APIError as e:
    print(e)

payment_id = "3e039d85-de8a-4682-8195-164ee85bb991"

try:
    client.messages.validate(
        payment_id, "73bf72ac29335cdcd9028655b41885bf1954dc1d"
    )

    print("")
except cheddar.errors.MessageIntegrityError as e:
    print(e)

print("Getting payment details for payment %s..." % payment_uuid)
resp = client.payments.details(payment_uuid)
print("UUID: %s" % resp.uuid)
print("Status: %s" % resp.status)
