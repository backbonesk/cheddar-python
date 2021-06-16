# Changelog

## v0.6.2 & v0.6.3: 16/06/2021

Maintenance release – previous version have been yanked and tags removed due to a security issue and
this is basically a rerelease of previous version with the problem fixed.

## v0.6.1: 11/02/2021

Added support for new (sia.eu) Poštová banka's iTerminal service sandbox and production environments
(available as `PBIterminal2` driver / `ITERMINAL2` service).

## v0.6.0: 25/06/2020

Added missing keyword support for ComfortPay service.

## v0.5.0: 24/09/2019

Renamed package to `cheddarpayments`, open sourced at GitHub and released to PyPI.

## v0.4.0: 06/09/2019

Rearchitecting API to be a bit more Pythonic with Python 3.4+ compatibility. Code formatting is covered by Black and
various small fixes to make everything better and easier including first test.

## v0.3.1: 24/08/2016

Added the ability to set `X-Real-IP` header with user's 'IP address. The IP should be set as `ip_address` property on
`cheddar` class.

## v0.3.0: 08/05/2016

Added support for Poštová banka's iTerminal and a note in the documentation about changing the endpoint URL to either
sandbox or completely different Cheddar instance. Production URL for the service has also changed to
[cheddarpayments.com](https://www.cheddarpayments.com).

## v0.2.4: 07/09/2015

Added support for Global Payments Europe GP webpay service.

## v0.2.3: 24/08/2015

Added support for PayPal's Buy Now buttons and IPN.

## v0.2.2: 02/07/2015

Added support for VÚB eCard service.

## v0.2.1: 23/01/2015

Bugfix release with minor changes to ComfortPay service handling.

## v0.2.0: 21/01/2015

Added public method to be able to update amount and date of charge on a periodical payment.

## v0.1.0: 06/12/2014

General public method for validating signature of a given message.

## v0.0.4: 12/11/2014

Don't verify integrity of SSL certificate.

## v0.0.3: 02/11/2014

Using HTTPS in production to add at least some security.

## v0.0.2: 19/10/2014

Initial version with support for creating payments and checking their details afterwards.

## v0.0.1: 16/10/2014

Initial version with support for creating payments and checking their details afterwards.
