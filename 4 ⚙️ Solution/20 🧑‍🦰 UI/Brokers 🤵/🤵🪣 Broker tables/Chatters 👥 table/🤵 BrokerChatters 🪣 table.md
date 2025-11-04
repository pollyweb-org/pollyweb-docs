# 🤵🪣 Chatters @ Broker table

> Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants

<br/>

## Usage

| [Role 🎭](<../../../../40 👥 Domains/👥 Domain/👥🎭 Domain Role.md>) | [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | Details
|-|-|-|-
| [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | [`Assess@Broker`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)| Done
| [Finder 🔎](<../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | [`Assess@Broker`](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | [`Introduce@Finder`](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 🐌 msg.md>) | Done
| [Helper 🤲](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | [`Invite@Broker`](<../../🤵🅰️ Broker methods/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) | [`Invited@Helper`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>) | Done
| [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | [`Query@Broker`](<../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Disclose@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>) | Missing 🚨
|

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Chats.yaml
Prefix: Broker
Table: Chatters
Key: Chat, Domain
Parents:
    Chat: { Chats.ID: Chatters.Chat }
    Domain: { Domains.Name: Chatters.Domain }
```

| Link | Table | Contains
|-|-|-
| Parents   | [`Chats` 🪣](<../Chats 💬 table/🤵 BrokerChats 🪣 table.md>) | [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
|           | [`Domains` 🪣](<../Domains 👥 table/🤵 BrokerDomains 🪣 table.md>) | [domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|

<br/>

## Example

Here's the [`READ` command](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
Chat: <chat-uuid>
Domain: any-host.dom
Role: HOST # one of HOST, VAULT, HELPER
```