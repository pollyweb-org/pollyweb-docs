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
Key: Wallet

Parents:
    Notifier: { Notifiers.Notifier: Wallets.Notifier }

Children:
    Chats: { Chats.Wallet: Wallets.Wallet }
    Binds: { Binds.Wallet: Wallet.Wallet }
    Tokens: { Tokens.Wallet: Wallet.Wallet }

Distincts: 
    Hosts: Chats.Host
    Vaults: Binds.Vault
    Issuers: Tokens.Issuer
    BindSchemas: Binds.Schema
    TokenSchemas: Tokens.Schema
```

| Link | Table | Contains
|-|-|-
| Parent | [`Notifiers` 🪣](<../Notifiers 📣 table/🤵 BrokerNotifiers 🪣 table.md>) | [Notifier 📣 domain](<../../../Notifiers 📣/📣 Notifier domain/📣 Notifier 👥 domain.md>)
| Children | [`Chats` 🪣](<../Chats 💬 table/🤵 BrokerChats 🪣 table.md>) | [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
| | [`Binds` 🪣](<../Binds 🔗 table/🤵 BrokerBinds 🪣 table.md>) | [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
| | [`Tokens` 🪣](<../Tokens 🎫 table/🤵 Tokens 🪣 table.md>) | [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|

<br/>

## Example

Here's the [`GET` command](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) result.

```yaml
# GET|BrokerWallets|<wallet-uuid>

Wallet: <wallet-uuid>
PublicKey: <public-key>
Notifier: any-notifier.dom
Language: en-us

# Agents
Curator: any-curator.dom
Finder: any-finder.dom
Persona: any-persona.dom
Reviewer: any-reviewer.dom
```