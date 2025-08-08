<!-- #TODO -->

<!-- Docs: https://quip.com/oSzpA7HRICjq/-Broker-Binds#temp:C:DSD2aa2718d92bf4941ac7bb41e9 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L10 -->


## Async Message 

- Header:
  - From: `any-host.org`
  - To: `any-broker.org`
  - Subject: `Bindable@Broker`
- Body:
  - SessionID: `<session-uuid>`
  - Codes [ ]:
    - Code: `any-authority.org/<code>`
