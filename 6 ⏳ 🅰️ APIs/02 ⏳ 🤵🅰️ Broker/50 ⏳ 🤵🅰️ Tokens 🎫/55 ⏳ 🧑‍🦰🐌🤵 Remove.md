<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfT7c08473cd7254f24bedf5e873 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L172 -->


## Async Message

- Header:
  - From: `<wallet-uuid>`
  - To: `any-broker.org`
  - Subject: `Remove@Broker`
- Body:
  - TokenID: `<token-uuid>`
  - Issuer: `any-issuer.com`
- Hash: `<hash>`
- Signature: `<signature>`
