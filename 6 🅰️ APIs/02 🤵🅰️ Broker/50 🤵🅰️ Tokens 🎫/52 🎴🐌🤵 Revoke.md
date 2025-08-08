#TODO

<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfT9e264d13fa7b4030920efe49d -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L136 -->


## Async Message

- Header:
  - From: `any-issuer.com`
  - Subject: `Revoke@Broker`
- Body:
  - ChatID: `<session-uuid>`
  - TokenID: `<token-uuid>`
- Hash: `<hash>`
- Signature: `<signature>`
