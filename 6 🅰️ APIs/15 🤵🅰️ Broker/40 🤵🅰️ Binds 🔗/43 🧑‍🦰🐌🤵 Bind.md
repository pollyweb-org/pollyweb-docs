<!-- #TODO -->

<!-- Docs: https://quip.com/oSzpA7HRICjq#temp:C:DSD3f7309f961e24f0ebb5897e2f -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L93 -->

# 🧑‍🦰🐌🤵 Bind@Broker


> Used by the [🧑‍🦰👉🗄️ Bind Vault @ Wallet](<../../../5 ⏩ Flows/09 🗄️⏩ Vaults/01 🗄️⏩🧑‍🦰 Bind.md>).

<br/>

## Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.org
    Subject: Bind@Broker

Body:
    ChatID: <chat-uuid@vault>
    Codes:
      - Code: any-authority.org/ANY-CODE
```


| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`|   | 
|           | `To`  | string| [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
|           | `Subject`| string|  `Bind@Broker`
|