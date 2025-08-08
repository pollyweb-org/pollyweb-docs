#TODO

<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfTe327e788ccd54eefbe5f7e844 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L88 -->


## Async Message

- Header:
  - From: `<wallet-uuid>`
  - Subject: `Accepted@Broker`
- Body:
  - ChatID: `<session-uuid>`
  - TokenID: `<offer-uuid>`
  - Issuer: `any-host.org`
  - Path: `/storage/tf/creds/<issuer>/<token-uuid>`
- Hash: `<hash>`
- Signature: `<signature>`
