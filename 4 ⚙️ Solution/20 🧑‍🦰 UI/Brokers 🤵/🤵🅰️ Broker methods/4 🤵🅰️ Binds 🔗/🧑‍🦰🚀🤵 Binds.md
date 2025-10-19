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
  - Bind: <bind-uuid>
    Vault: any-vault.dom
    VaultTitle: AnyVault
    Schema: any-authority.org/ANY-SCHEMA
    SchemaTitle: Any Schema
```

| Object | Property | Type  | Description
|-|-|-|-
| Top      | `Binds`| list  | List of Bind objects
| Bind     | `Bind`   | uuid  | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID from [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)
|          | `Vault`    | string| [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>)  from [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/to Bind/🤵🐌🗄️ Bound.md>)
|          | `Vault$`| string| [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) title
|          | `Schema`     | string| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|          | `Schema$`| string| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) title
|



<br/>

## Handler

```yaml
# The the wallet item
- GET >> $wallet:
    Pool: Wallets@Broker
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg|$wallet.PublicKey

# Translate the vaults and the schemas
- SEND >> $translations:
    Subject: Translate@Graph
    Language: $wallet.Language
    Domains: $wallet.Vaults
    Schemas: $wallet.BindSchemas

# Add the vault titles
- MERGE >> $binds:
    Lists: 
        BINDS: $wallet.Binds
        DOMAINS: $translations.Domains
    Match: 
        BINDS.Vault: DOMAINS.Domain
    Output: 
        Bind: BINDS.Bind
        Vault: BINDS.Vault
        Vault$: DOMAINS.Translation
        Schema: BINDS.Schema
        
# Add the schema titles
- MERGE >> $binds:
    Lists: 
        BINDS: $binds
        SCHEMAS: $translations.Schemas
    Match: 
        BINDS.Schema: SCHEMAS.Schema
    Output: 
        :BINDS:
        Schema$: SCHEMAS.Translation

# Respond
- REEL:
    Binds: $binds
```

| [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| ⏬ [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) | Get the [Hook 🪝](<../../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 Hooks 🪝.md>) from [`Bindable@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)  
| 🔐 [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>) | Verify the  [Signature 🔏](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Signatures 🔏.md>) of the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| ⬇️ [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/EVAL ⬇️ flow.md>) | Format the items from the  [Chats 🪣 table](<../../🤵🪣 Broker tables/🤵🪣 Chats.md>)
| 🎣 [`REEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) | Respond to the [Synchronous Request 🚀](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Request Sync 🚀.md>)
|
