# 🤵🪣 Chatters @ Broker table

> Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵🤲 Broker helper.md>)

> Stores [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants

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
Role: HOST # one of HOST, AGENT, HELPER
```