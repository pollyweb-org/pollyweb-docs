# 🤵 Broker.Chatters 🪣 table

> About
* Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* Stores [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants

<br/>

## Usage

| [Role 🎭](<../../../../../40 👥 Domains/👥 Domain/👥🎭 Domain Role.md>) | [Broker 🤵](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [domain 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | Details
|-|-|-|-
| [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | [`Locate@Broker`](<../../../🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | [`Hello@Host`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)| Done
| [Finder 🔎](<../../../../../50 🫥 Agent domains/Finders 🔎/$/🔎 Finder 🫥 agent.md>) | [`Locate@Broker`](<../../../🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | [`Present@Finder`](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎😃 Finder Talkers/Present/🔎 Present 🐌 msg.md>) | Done
| [Helper 🤲](<../../../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) | [`Invite@Broker`](<../../../🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) | [`Help@Helper`](<../../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Help 🐌 msg.md>) | Done
| [Vault 🗄️](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | [`Query@Broker`](<../../../🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) | [`Disclose@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Disclose 🤵🐌🗄️/🗄️ Disclose 🐌 msg.md>) | Missing 🚨
|

<!-- TODO: Add missing Disclosure@Vault above -->



<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Chatters
Item: Chatter
Key: Chat, Domain
```

<br/>

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

```yaml
Parents:
    
    Chat: # Chat where the domain participates

    Domain: # Domain referenced
        Domains.Name: Chatter.Domain, 
        Domains.Wallet: Chatter.Chat.Wallet
```

<br/>

The [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) are:  [`OnBroker`](<../../../🤵😃 Broker talkers/Welcome 💬 talker/🤵 Welcome 😃 handler.md>) [`OnHost`](<../🪣🧱 23 Host 🔔 event/🤵 OnChatterHost 🔔 handler.md>) [`OnHelper`](<../🪣🧱 34 Helper 🔔 event/🤵 OnChatterHelper 🔔 handler.md>)

```yaml
Handlers:
    BROKER >> OnBroker:   # Calls Prompt@Notifier
    HOST   >> OnHost:     # Calls Hello@Host
    HELPER >> OnHelper:   # Calls Help@Helper
```

<br/>

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Asserts:

    # Group assertions
    AllOf: Wallet, Chat, Domain, Role
    UUIDs: Wallet, Chat, Invite
    
    # State machine
    .State.IsIn: FINDER, BROKER, HOST

    # Field assertions
    Schema.IsSchema:
    Domain.IsDomain: 
    Role.IsIn: 
        - HOST    # From Hello@Host
        - HELPER  # From Invite@Broker
        - VAULT   # From Query@Broker
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
Chat: <chat-uuid>
Domain: any-host.dom
Role: HOST 
```

[Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) info

```yaml
Key: ANY-LOCATOR
Parameters: {A:1, B:2}
```

Shared [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) (if any)

```yaml
Binds:
  - Title: 🔗 Any Bind, by Any Vault
    Bind: <bind-uuid>
    Vault: <vault-uuid>
```

Shared [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) (if any)

```yaml
Tokens:
  - Title: 🎟️ Any Token, by Any Issuer
    Token: <token-uuid>
    Issuer: <issuer-uuid>
```

From the [`Invite@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) 

```yaml 
Invite: <invite-uuid>
```

<br/>

## Fields

Field|Type|Details|Origin|Purpose
|-|-|-|-|-
|`Role`|text|Role in [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)||[`Chat@`](<../../../🤵📨 Broker msgs/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>) [`Prompt@`](<../../../🤵📨 Broker msgs/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
| ||`HOST` role | [`Locate@`](<../../../🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | 
| ||`HELPER` role | [`Invite@`](<../../../🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) | 
| ||`VAULT` role | [`Query@`](<../../../🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) |
|`Chat`|uuid|[Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | |[`Chat@`](<../../../🤵📨 Broker msgs/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>)
|`Domain`|text|[domain 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name||[`Chat@`](<../../../🤵📨 Broker msgs/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>)
|`Key`| text | [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) key || [`Chat@`](<../../../🤵📨 Broker msgs/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>) |
|`Parameters` | map | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) parameters || [`Chat@`](<../../../🤵📨 Broker msgs/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>)
|`Binds`|list| [Binds 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) shared |  | [`Chat@`](<../../../🤵📨 Broker msgs/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>)
|`Tokens` | list | [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) shared || [`Chat@`](<../../../🤵📨 Broker msgs/Chats 💬 Chat 🤗🚀🤵/🤵 Chat 📃 handler.md>)
|