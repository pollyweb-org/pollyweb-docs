# 🤵🪣 Wallets @ Broker table

> Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Purpose

* [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) that stores [Wallet 🧑‍🦰 apps](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)

> Usage

* Inserted by [`Onboard@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 🚀 request.md>)
* Updated by [`Language@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Language 🧑‍🦰🐌🤵/🤵 Language 🐌 msg.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Wallets.yaml

Prefix: Broker
Table: Wallets
Key: ID

Parents:
    Notifier: { Notifiers.Name: Wallets.Notifier }

Children:
    Chats: { Chats.Wallet: Wallets.ID }
    Binds: { Binds.Wallet: Wallet.ID }
    Tokens: { Tokens.Active.Wallet: Wallet.ID }
    Offers: { Tokens.Offers.Wallet: Wallet.ID }

Distincts: 
    Hosts: Chats.Host
    Vaults: Binds.Vault
    Issuers: Tokens.Issuer
    BindSchemas: Binds.Schema
    TokenSchemas: Tokens.Schema
```

| Link | Table | Contains
|-|-|-
| Parent | [`Notifiers` 🪣](<../Notifiers 📣 table/🤵 Broker.Notifiers 🪣 table.md>) | [Notifier 📣 domain](<../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>)
| Children | [`Chats` 🪣](<../Chats 💬 table/🤵 Broker.Chats 🪣 table.md>) | [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
| | [`Binds` 🪣](<../Binds 🔗 table/🤵 Broker.Binds 🪣 table.md>) | [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| | [`Tokens` 🪣](<../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) | [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|

<br/>

## Example

Here's the [`READ` command](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|BrokerWallets|<wallet-uuid>

ID: <wallet-uuid>
PublicKey: <public-key>
Notifier: any-notifier.dom
Language: en-us

# Agents
Curator: any-curator.dom
Finder: any-finder.dom
Persona: any-persona.dom
Reviewer: any-reviewer.dom
```