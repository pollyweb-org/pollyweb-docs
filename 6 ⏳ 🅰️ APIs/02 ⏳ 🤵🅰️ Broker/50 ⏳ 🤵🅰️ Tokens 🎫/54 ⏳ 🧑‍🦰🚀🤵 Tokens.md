#TODO

<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTa9a1f10023324c448a569fa05 -->
<!-- Code: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS.py#L199 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L10 -->


## Request

- Header:
  - From: `<wallet-uuid>`
  - To: `any-broker.org`
  - Subject: `Tokens@Broker`
- Body: {}
- Hash: `<hash>`
- Signature: `<signature>`


## Response

- Tokens []:
    - TokenID: `<token-uuid>`
    - Issuer: `any-issuer.com`
    - IssuerTranslation: `<translationOf(any-host.org)>`
    - Code: `any-authority.org/<code>`
    - CodeTranslation: `<translationOf(any-authority.org/<code>)>`
    - Issued: `2018-12-10T13:45:00.000Z`
    - Starts: `2018-12-10T13:45:00.000Z`
    - Expires: `2018-12-10T13:45:00.000Z`
    - Schema: `{...}`
    - Version: `1.0.0`
    - QR: `\U0001F91Dnlweb.org/...`
    - Path: `/storage/tf/creds/<issuer>/<token-uuid>`
