# 🤵🪣 Wallets @ Broker table

> About
* Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* [Itemized 🪣 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) that stores [Wallet 🧑‍🦰 apps](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)

<br/>

## Data access

Flow | Actor | [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) |Purpose
|-|-|:-:|:-:|-|
|| [`Onboard@Broker` 📃](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 📃 handler.md>) | | X | Registers a [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|[`Localize`](<../🪣🧱 20 Localize ⏩ flow/🤵 Broker.Wallets.Localize ⏩ flow.md>)| [`Pop@Broker` 📃](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 handler.md>) | X | X | Opens a [Broker 🤵](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) 
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

Here's the [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) definition.

```yaml
Parents: 
    Notifier # Registerer of the Wallet
```
References the [`Broker.Notifiers` 🪣 table](<../../Notifiers 📣 table/🪣 Notifiers/🤵 Broker.Notifiers 🪣 table.md>)

<br/>

Here's the [Item 🛢 Children](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) definition.

```yaml
Children: 
    - Chats     # Wallet chats
    - Binds     # Wallet binds
    - Tokens    # Wallet tokens
    - Domains   # Domains of chats, binds, and tokens
    - Schemas   # Domains of binds and tokens
```
References: [`Binds`](<../../Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>) [`Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Schemas`](<../../Schemas 🧩 table/🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>) [`Tokens`](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)

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

Here's the [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition.

```yaml
Handlers:
    ALTERED >> OnWalletAltered:    # Updates Broker.Frontend
    UPDATED >> OnWalletLocalized:  # Localizes Binds, Chats, etc.
        Assert: New.Language
```
Handlers: [`OnWalletAltered`](<../🪣🧱 00 Altered 🔔 event/🤵 OnWalletAltered 🔔 handler.md>) [`OnWalletLocalized`](<../🪣🧱 21 Localized 🔔/🤵 OnWalletLocalized 🔔 handler.md>)

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From Onboard@
ID: <wallet-uuid>
PublicKey: <public-key>
Notifier: any-notifier.dom

# Localization from Onboard@ and Pop@
Language: en-us
Region: United States

# Agents from Onboard@ and Pop@
Curator: any-curator.dom
Finder: any-finder.dom
Persona: any-persona.dom
Reviewer: any-reviewer.dom
```