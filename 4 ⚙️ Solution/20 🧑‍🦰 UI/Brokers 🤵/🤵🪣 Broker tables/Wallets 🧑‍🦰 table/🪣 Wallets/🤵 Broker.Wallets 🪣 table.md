# 🤵🪣 Wallets @ Broker table

> About
* Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* [Itemized 🪣 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) that stores [Wallet 🧑‍🦰 apps](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)

<br/>

## Data access

Flow | Actor | [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) |Purpose
|-|-|:-:|:-:|-|
|| [`Onboard@Broker` 📃](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 📃 handler.md>) | | X | Registers a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|[`Localize`](<../🪣🧱 20 Localize ⏩ flow/🤵 Broker.Wallets.Localize ⏩ flow.md>)| [`Pop@Broker` 📃](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 handler.md>) | X | X | Opens a [Broker 🤵](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) 
|

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Wallets
Item: Wallet
```

<br/>

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Broker.Notifiers`](<../../Notifiers 📣 table/🪣 Notifiers/🤵 Broker.Notifiers 🪣 table.md>)


```yaml
Parents: 
    Notifier # Registerer of the Wallet
```

<br/>

The [Item 🛢 Children](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) are: [`Binds`](<../../Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>) [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Schemas`](<../../Schemas 🧩 table/🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>) [`Tokens`](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

```yaml
Children: 
    - Chats     # Wallet chats
    - Binds     # Wallet binds
    - Tokens    # Wallet tokens
    - Domains   # Domains of chats, binds, and tokens
    - Schemas   # Domains of binds and tokens
```


<br/>

Here's the [Item 🛢 Distincts](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Distincts.md>) definition.

```yaml
Distincts: 
    Hosts: Chats.Host
    Vaults: Binds.Vault
    Issuers: Tokens.Issuer
    BindSchemas: Binds.Schema
    TokenSchemas: Tokens.Schema
```

<br/>

The [Item 🛢 Views](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Views.md>) use: [`Broker.Binds`](<../../Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>) [`Broker.Tokens`](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

```yaml
Views:
    QueryBinds: Binds.QUERY
    QueryTokens: Tokens.QUERY
```


<br/>

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are: [`OnAltered`](<../🪣🧱 00 Altered 🔔 event/🤵 OnWalletAltered 🔔 handler.md>) [`OnLocalized`](<../🪣🧱 21 Localized 🔔/🤵 OnWalletLocalized 🔔 handler.md>)

```yaml
Handlers:
    ALTERED >> OnWalletAltered:    # Updates Broker.Frontend
    UPDATED >> OnWalletLocalized:  # Localizes Binds, Chats, etc.
        Assert: New.Language
```

<br/>

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
    AllOf: PublicKey, Notifier, Language
    Texts: PublicKey, Region
    Notifier.IsDomain:
    Language.IsLanguage:    
```
Uses: [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsLanguage`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsLanguage ⓕ.md>)

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <wallet-uuid>
```

From [`Onboard@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 📃 handler.md>)

```yaml
PublicKey: <public-key>
Notifier: any-notifier.dom
```

```yaml
# Localization from Onboard@ and Pop@
Language: en-us
Region: United States
```

```yaml
# Agents from Onboard@ and Pop@
Curator: any-curator.dom
Finder: any-finder.dom
Persona: any-persona.dom
Reviewer: any-reviewer.dom
```