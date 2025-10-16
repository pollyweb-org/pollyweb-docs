<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L53 -->

# 🧑‍🦰🚀🤵 Binds @ Broker

> List the [Binds 🔗](<../../../../30 Data/20 🔗 Binds/🔗 Bind.md>) of a [Wallet 🧑‍🦰 app](<../../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).

> Used in:
> <br/> • [🧑‍🦰👉🤵 Translate](<../../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/12 🧑‍🦰👉🤵 Translate.md>)
> <br/> • [🧑‍🦰👉🤵 List binds](<../../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/01 🧑‍🦰👉🤵 List binds.md>)
> <br/> • [🤵⏩🧑‍🦰 Update Binds 🔗](<../../🤵⏩ Broker flows/06 🤵⏩🧑‍🦰 Update Binds 🔗.md>)

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Binds@Broker
Body: 
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `Subject`| string|  `Binds@Broker`
|

<br/>

## Synchronous Response 🚀


```yaml
Binds:
  - BindID: <bind-uuid>
    Vault: any-vault.org
    VaultTitle: AnyVault
    Code: any-authority.org/ANY-CODE
    CodeTitle: Any Code
```

| Object | Property | Type  | Description
|-|-|-|-
| Top      | `Binds`| list  | List of Bind objects
| Bind     | `BindID`   | uuid  | [Bind 🔗](<../../../../30 Data/20 🔗 Binds/🔗 Bind.md>) ID
|          | `Vault`    | string| [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) name
|          | `VaultTitle`| string| [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) title
|          | `Code`     | string| [Schema Code 🧩](<../../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
|          | `CodeTitle`| string| [Schema Code 🧩](<../../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) title
|