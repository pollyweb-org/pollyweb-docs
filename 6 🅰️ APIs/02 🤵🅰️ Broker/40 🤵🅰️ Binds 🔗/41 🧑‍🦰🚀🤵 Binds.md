<!-- #TODO -->

<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L53 -->

# 🧑‍🦰🚀🤵 Binds @ Broker

> Lists the Binds of a Wallet app.

> Used in:
> <br/> • [🧑‍🦰👉🤵 Translate](<../../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/12 🧑‍🦰👉🤵 Translate.md>)
> <br/> • [🧑‍🦰👉🤵 List binds](<../../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/30 👉🔗 Binds/01 🧑‍🦰👉🤵 List binds.md>)
> <br/> • [🤵⏩🧑‍🦰 Update binds](<../../../5 ⏩ Flows/08 🤵⏩ Brokers/03 🤵⏩🧑‍🦰 Update binds.md>)

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.org
    Subject: Binds@Broker
Body: 
`````
|Property|Type|Description
|-|-|-
|

<br/>

## Synchronous Response 🚀


```yaml
Binds:
  - ID: <bind-uuid>
    Vault: any-vault.org
    VaultTitle: AnyVault
    Code: any-authority.org/ANY-CODE
    CodeTitle: Any Code
```

|Property|Type|Description
|-|-|-
|