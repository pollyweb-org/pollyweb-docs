<!-- Docs: -->
<!-- Code: -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L135 -->


## Async Message

* Header:
  * From: `<wallet-uuid>`
  * Subject: `Unbind@Broker`
* Body:
  * BindID: `<bind-uuid>`
* Hash: `<hash>`
* Signature: `<signature>`
