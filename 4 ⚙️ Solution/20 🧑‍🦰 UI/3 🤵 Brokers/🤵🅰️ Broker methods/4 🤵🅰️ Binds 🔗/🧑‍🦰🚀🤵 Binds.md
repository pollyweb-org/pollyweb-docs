<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L53 -->

# 🧑‍🦰🚀🤵 Binds @ Broker

> List the [Binds 🔗](<../../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) of a [Wallet 🧑‍🦰 app](<../../../1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>).

> Used in:
> <br/> • [🧑‍🦰👉🤵 Translate](<../../../1 🧑‍🦰 Wallets/🧑‍🦰👉 Wallet flows/10 👉🤵 Set-up/12 🧑‍🦰👉🤵 Translate.md>)
> <br/> • [🧑‍🦰👉🤵 List binds](<../../../1 🧑‍🦰 Wallets/🧑‍🦰👉 Wallet flows/30 👉🔗 Binds/01 🧑‍🦰👉🤵 List binds.md>)
> <br/> • [🤵⏩🧑‍🦰 Update Binds 🔗](<../../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Binds 🔗.md>)

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
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
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
| Bind     | `BindID`   | uuid  | [Bind 🔗](<../../../../30 🧩 Data/2 🔗 Binds/🔗 Bind.md>) ID
|          | `Vault`    | string| [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) name
|          | `VaultTitle`| string| [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) title
|          | `Code`     | string| [Schema Code 🧩](<../../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
|          | `CodeTitle`| string| [Schema Code 🧩](<../../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) title
|