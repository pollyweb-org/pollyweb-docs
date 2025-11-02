# 🤵🪣 Chatters @ Broker table

> Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants

<br/>

## Usage

| {{Role}} | [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [domain 👥](<../../../../40 👥 Domains/👥 Domain.md>)
|-|-|-
| [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | [`Assess@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | [`Hello@Host` 🅰️ method](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| [Helper 🤲 domain](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | [`Invite@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) | [`Invited@Helper` 🅰️ method](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>)
| [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | [`Query@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Disclose@Vault` 🅰️ method](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Chats.yaml
Prefix: Broker
Table: Chatters
Key: Chat, Domain
Parents:
    Chat: { Chats.Chat: Chatters.Chat }
    Domain: { Domains.Domain: Chatters.Domain }
```

| Link | Table | Contains
|-|-|-
| Parents   | [`Chats` 🪣](<../Chats 💬 table/🤵 BrokerChats 🪣 table.md>) | [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
|           | [`Domains` 🪣](<../Domains 👥 table/🤵 BrokerDomains 🪣 table.md>) | [domains 👥](<../../../../40 👥 Domains/👥 Domain.md>)
|

<br/>

## Example

Here's the [`GET` command](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) result.

```yaml
Chat: <chat-uuid>
Domain: any-host.dom
Role: HOST # one of HOST, VAULT, HELPER
```