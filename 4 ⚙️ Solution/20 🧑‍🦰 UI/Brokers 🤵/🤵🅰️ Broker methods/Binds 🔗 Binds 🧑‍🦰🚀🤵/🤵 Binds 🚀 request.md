<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L53 -->

# 🧑‍🦰🚀🤵 Binds @ Broker

> List the [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) of a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

> Implemented by [`Binds` 📃 script](<🤵 Binds 📃 handler.md>)

> Used in:
* [`Translate` 💬 chat](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Set Language 💬🤵/🧑‍🦰 Set Language ⏩ flow.md>)
* [`List binds` 💬 chat](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/List Binds 💬🔗🤵 /🧑‍🦰 List Binds ⏩ flow.md>)
* [`Update Binds` ⏩ flow](<../../🤵⏩ Broker flows/Update Binds 🤵⏩🔗/🤵 Update Binds ⏩ flow.md>)

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Binds@Broker
```

| Object | Property | Type  | Description | Origin
|-|-|-|-|-
| Header    |`From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|           |`To`|domain| [Broker 🤵](<../../🤵 Broker helper/Broker 🤵 helper 🤲.md>) | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|           | `Subject`| string|  `Binds@Broker`
|

<br/>

## Synchronous Response 🚀

```yaml
Binds:
  - Bind: <bind-uuid>
    Vault: any-vault.dom
    Vault$: AnyVault
    Schema: any-authority.org/ANY-SCHEMA
    Schema$: Any Schema
```

| Object | Property | Type  | Description
|-|-|-|-
| Top      | `Binds`| list  | List of Bind objects
| Bind     | `Bind`   | uuid  | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID from [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|          | `Vault`    | string| [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)  from [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|          | `Vault$`| string| [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) title
|          | `Schema`     | string| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|          | `Schema$`| string| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) title
|
