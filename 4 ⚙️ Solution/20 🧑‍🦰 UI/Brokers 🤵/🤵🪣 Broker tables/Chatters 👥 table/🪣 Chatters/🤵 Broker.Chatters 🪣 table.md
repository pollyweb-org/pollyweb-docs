# 🤵🪣 Chatters @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants

<br/>

## Usage

| [Role 🎭](<../../../../../40 👥 Domains/👥 Domain/👥🎭 Domain Role.md>) | [Broker 🤵](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [domain 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | Details
|-|-|-|-
| [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | [`Locate@Broker`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | [`Hello@Host`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)| Done
| [Finder 🔎](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | [`Locate@Broker`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | [`Present@Finder`](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>) | Done
| [Helper 🤲](<../../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | [`Invite@Broker`](<../../../🤵🅰️ Broker methods/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) | [`Invited@Helper`](<../../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>) | Done
| [Vault 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | [`Query@Broker`](<../../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Disclose@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>) | Missing 🚨
|

<!-- TODO: Add missing Disclosure@Vault above -->

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Chats.yaml
Prefix: Broker
Table: Chatters
Item: Chatter
Key: Chat, Domain

Parents:
    Chat: { Chats.ID: Chatter.Chat }
    Domain: { Domains.Name: Chatter.Domain }

Handlers:
    OnFinder: FINDER
    OnBroker: BROKER
    OnHost: HOST
    OnHelper: HELPER
```

| Link | Table | Contains
|-|-|-
| Parents   | [`Chats` 🪣](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) | [Chats 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
|           | [`Domains` 🪣](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) | [domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
|

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
Chat: <chat-uuid>
Domain: any-host.dom
Role: HOST # one of HOST, VAULT, HELPER

# Locator info
Key: ANY-LOCATOR
Parameters: {A:1, B:2}

# Shared binds (if any)
Binds:
  - Title: 🔗 Any Bind, by Any Vault
    Bind: <bind-A-uuid>

# Shared tokens (if any)
Tokens:
  - Title: 🎟️ Any Token, by Any Issuer
    Token: <token-A-uuid>
  - Title: 🪪 Another Token, by Another Issuer
    Token: <Token-B-uuid>
```


Property|Type|Details|Origin|Purpose
|-|-|-|-|-
|`Role`|text|Role in [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)|-|[`Chat@`](<../../../🤵🅰️ Broker methods/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>) [`Prompt@`](<../../../🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
| ||- `HOST` role | [`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | -
| ||- `HELPER` role | [`Invite@`](<../../../🤵🅰️ Broker methods/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) | -
| ||- `VAULT` role | [`Query@`](<../../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) |-
|`Chat`|uuid|[Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | -|[`Chat@`](<../../../🤵🅰️ Broker methods/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>)
|`Domain`|text|[domain 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name|-|[`Chat@`](<../../../🤵🅰️ Broker methods/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>)
|`Key`| text | [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) key |-| [`Chat@`](<../../../🤵🅰️ Broker methods/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>) |
|`Parameters` | map | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) parameters |-| [`Chat@`](<../../../🤵🅰️ Broker methods/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>)
|`Binds`|list| [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) shared | - | [`Chat@`](<../../../🤵🅰️ Broker methods/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>)
|`Tokens` | list | [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) shared |- | [`Presented@`](<../../../🤵🅰️ Broker methods/Chats 💬 Presented 🔎🐌🤵/🤵 Presented 🐌 msg.md>)
|