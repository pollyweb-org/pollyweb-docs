# 🤵🪣 Chats @ Broker table

> Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)


<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Chats.yaml
Prefix: Broker
Table: Chats
Key: ID
Parents:
    Wallet: { Wallets.ID: Chats.Wallet }
    Host: { Domains.Name: Chats.Host }
Children:
    Chatters: { Chatters.Chat: Chats.ID }
```

| Link | Table | Contains
|-|-|-
| Parents   | [`Wallets` 🪣](<../Wallets 🧑‍🦰 table/🤵 BrokerWallets 🪣 table.md>) | [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|           | [`Domains` 🪣](<../Domains 👥 table/🤵 BrokerDomains 🪣 table.md>) | [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
| Children | [`Chatters` 🪣](<../Chatters 👥 table/🤵 BrokerChatters 🪣 table.md>) | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants
|

<br/>

## Example

Here's the [`READ` command](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Chats|<chat-id>

ID: <chat-uuid>
Wallet: <wallet-uuid>

# Host info
Host: any-host.dom
Host$: Any Host
Emoji: 😃

# For Wallets to sign messages
PrivateKey: <PrivateKey>

# For domains to verify Wallet messages
PublicKey: <PublicKey>

# Origin chat (if any)
Origin: <origin-chat-uuid>
```

Property|Type|Details|Origin|Purpose
|-|-|-|-|-
|`ID`|uuid | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID |[`Assess@`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chats@`](<../../🤵🅰️ Broker methods/Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>)
|`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) ID | [`Assess@`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | [`Chats@`](<../../🤵🅰️ Broker methods/Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>)
|`Host` | text | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name |[`Assess@`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chats@`](<../../🤵🅰️ Broker methods/Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>)
|`Host$`|text | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) title |[`Assess@`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chats@`](<../../🤵🅰️ Broker methods/Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>)
|`Emoji`|text | [Manifest 📜](<../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) emoji |[`Assess@`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chats@`](<../../🤵🅰️ Broker methods/Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>)
|`Key`| text | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) key |[`Assess@`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chat@`](<../../🤵🅰️ Broker methods/Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>)
|`Parameters` | pairs | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) parameters |[`Assess@`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chat@`](<../../🤵🅰️ Broker methods/Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>)
|`PublicKey` | text | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) verification |[`Assess@`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)| [`Chat@`](<../../🤵🅰️ Broker methods/Chats 💬 Chats 🧑‍🦰🚀🤵/🤵 Chats 🚀 request.md>)
|`Origin` | uuid | Parent [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) |[`Assess@`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | [`Introduced@`](<../../🤵🅰️ Broker methods/Chats 💬 Introduced 🔎🐌🤵/🤵 Introduced 🐌 msg.md>)
|`Tokens` | list | [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) shared |[`Assess@`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | [`Introduced@`](<../../🤵🅰️ Broker methods/Chats 💬 Introduced 🔎🐌🤵/🤵 Introduced 🐌 msg.md>)
|