<!-- #TODO -->

<!-- Docs: https://quip.com/oSzpA7HRICjq#temp:C:DSD3f7309f961e24f0ebb5897e2f -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L93 -->


## About

- Flow [🧑‍🦰👉🗄️ Bind](<../../../5 ⏩ Flows/09 🗄️⏩ Vaults/01 🗄️⏩🧑‍🦰 Bind.md>)


## Async Message

|Property|Type|Description
|-|-|-

- Header:
  - From: `<wallet-uuid>`
  - To: `any-broker.org`
  - Subject: `Bind@Broker`
- Body:
  - ChatID: `<chat-uuid@vault>`
  - Codes [ ]:
    - Code: `<bindable>`
- Hash: `<hash>`
- Signature: `<signature>`
