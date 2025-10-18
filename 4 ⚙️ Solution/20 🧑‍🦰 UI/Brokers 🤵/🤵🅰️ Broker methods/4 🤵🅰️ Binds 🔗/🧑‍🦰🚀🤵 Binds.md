<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L53 -->

# 🧑‍🦰🚀🤵 Binds @ Broker

> List the [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) of a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

> Used in:
> <br/> • [🧑‍🦰👉🤵 Translate](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in App 🏠/💬🤵 Translate.md>)
> <br/> • [🧑‍🦰👉🤵 List binds](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in App 🏠/💬🤵 List Binds 🔗.md>)
> <br/> • [🤵⏩🧑‍🦰 Update Binds 🔗](<../../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Binds 🔗.md>)

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Binds@Broker
Body: 
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `Subject`| string|  `Binds@Broker`
|

<br/>

## Synchronous Response 🚀


```yaml
Binds:
  - Bind:  <bind-uuid>
    Vault: any-vault.dom
    VaultTitle: AnyVault
    Code: any-authority.org/ANY-CODE
    CodeTitle: Any Code
```

| Object | Property | Type  | Description
|-|-|-|-
| Top      | `Binds`| list  | List of Bind objects
| Bind     | `Bind`   | uuid  | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID from [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)
|          | `Vault`    | string| [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)  from [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)
|          | `VaultTitle`| string| [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) title
|          | `Code`     | string| [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|          | `CodeTitle`| string| [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) title
|