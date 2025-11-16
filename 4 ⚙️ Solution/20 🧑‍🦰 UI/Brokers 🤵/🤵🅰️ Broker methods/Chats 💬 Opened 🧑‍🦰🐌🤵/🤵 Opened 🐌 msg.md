
# 🧑‍🦰🐌🤵 Opened @ Broker

<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

> Purpose

* The [Finder 🔎 domain](<../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) finished the introduction.

> Used by 

* [`Present` ⏩ flow](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/Present 🔎⏩🧑‍🦰/🔎 Present ⏩ flow.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-finder.dom
    To: any-broker.dom
    Subject: Presented@Broker

Body:
    Chat: <chat-uuid>
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
| Header |`From`|text| [Finder 🔎](<../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) | [`Present@`](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)
|        |`To`|text| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)  | [`Present@`](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>) |
|        | `Subject` |text| `Presented@Broker`
| Body   | `Chat`  | uuid   | [Chat 💬 ID](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Present@`](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>)
|