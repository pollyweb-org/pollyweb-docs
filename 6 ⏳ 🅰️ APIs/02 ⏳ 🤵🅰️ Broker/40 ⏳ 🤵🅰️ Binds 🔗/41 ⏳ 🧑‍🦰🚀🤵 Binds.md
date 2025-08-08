<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L53 -->


## Request

- Header:
  - From: `<wallet-uuid>`
  - To: `any-broker.org`
  - Subject: `Binds@Broker`
- Body: {}
- Hash: `<hash>`
- Signature: `<signature>`


## Response

- Binds [ ]:
  - ID: `<bind-uuid>`
  - Vault: `any-vault.org`
  - VaultTitle: `<nameOf(an-vault.com)>`
  - Code: `any-authority.org/<code>`
  - CodeTitle: `<nameOf(code)>`