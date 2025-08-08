<!-- Docs: https://quip.com/a167Ak79FKlt#temp:C:TMB24db6408284b4de5a52bcdfec -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/issuer/ISSUER_TESTS.py#L16 -->


# 🚀 Token

> Allows for a token to be downloaded from the issuer into the wallet.


## Request

* Header:
  * From: `any-broker.org`
  * To: `any-issuer.com`
  * Subject: `Token@Issuer`
* Body:
  * ChatID: `<chat-uuid>`
  * TokenID: `<token-uuid>`


## Response

* QR: `<qr>`
