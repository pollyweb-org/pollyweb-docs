
# 🔎🐌🤵 Introduced @ Broker

<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

> Purpose

* The [Finder 🔎 domain](<../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) finished the introduction.

> Used by 

* [`Introduce` ⏩ flow](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/Introduce 🔎⏩🧑‍🦰/🔎 Introduce ⏩ flow.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-finder.dom
    To: any-broker.dom
    Subject: Introduced@Broker

Body:
    Chat: <chat-uuid>
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header |`From`|domain| [Finder 🔎](<../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | [`Introduce@`](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 🐌 msg.md>)
|        |`To`|domain| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)  | [`Introduce@`](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 🐌 msg.md>) |
|        | `Subject` | string | `Introduced@Broker`
| Body   | `Chat`  | uuid   | [Chat 💬 ID](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Introduce@`](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 🐌 msg.md>)
|