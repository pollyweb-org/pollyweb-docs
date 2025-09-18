<!-- #TODO -->

<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfT7b35acc03fa342b9bc6e581e0 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L48 -->


## Async Message

|Property|Type|Description
|-|-|-

- Header:
  - From: `any-issuer.com`
  - To: `any-broker.org`
  - Subject: `Offer@Broker`
- Body:
  - ChatID: `<session-uuid>`
  - Token:
    - Issuer: `any-issuer.com`
    - TokenID: `<token-uuid>`
    - Code: `any-authority/<offer>`
    - Issued: `2018-12-10T13:45:00.000Z`
    - Starts: `2018-12-10T13:45:00.000Z`
    - Expires: `2018-12-10T13:45:00.000Z`
    - Version: `1.0.0`
    - QR: `<qr>`
- Hash: `<hash>`
- Signature: `<signature>`


