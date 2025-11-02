# 🤵🪣 Chats @ Broker table

> Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)

> Inserted by [`Converse` 📃 script](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/scripts/🤵 Call Converse 📃 script.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Chats.yaml
Prefix: Broker
Table: Chats
Key: Chat
Parents:
    Wallet: { Wallets.Wallet: Chats.Wallet }
    Host: { Domains.Domain: Chats.Host }
Children:
    Chatters: { Chatters.Chat: Chats.Chat }
```

| Link | Table | Contains
|-|-|-
| Parents   | [`Wallets` 🪣](<../Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>) | [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|           | [`Domains` 🪣](<../Domains 👥 table/🤵 BrokerDomains 🪣 table.md>) | [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
| Children | [`Chatters` 🪣](<../Chatters 👥 table/🤵 BrokerChatters 🪣 table.md>) | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants
|

<br/>

## Example

Here's the [`GET` command](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) result.

```yaml
# GET|Chats|<chat-id>

ID: <chat-uuid>
Wallet: <wallet-uuid>

# Host info
Host: any-host.dom
Host$: Any Host
Emoji: 😃

# Locator info
Key: ANY-LOCATOR
Parameters: {A:1, B:2}

# For Wallets to sign messages
PrivateKey: <PrivateKey>

# For domains to verify Wallet messages
PublicKey: <PublicKey>
```