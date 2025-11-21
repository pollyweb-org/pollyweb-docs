
# 🔎🐌🤵 Presented @ Broker

<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

> Purpose

* The [Finder 🔎 domain][Finder] finished the introduction.

> Used by 

* [`Present` ⏩ flow](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/Present 🔎⏩🧑‍🦰/🔎 Present ⏩ flow.md>)


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
| Header |`From`|text| [Finder 🔎][Finder] | [`Present@`][Present@]
|        |`To`|text| [Broker 🤵][Broker]  | [`Present@`][Present@] |
|        | `Subject` |text| `Presented@Broker`
| Body   | `Chat`  | uuid   | [Chat 💬 ID][Chat] | [`Present@`][Present@]
|

[Present@]: <../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>
[Chat]: <../../../../35 💬 Chats/Chats 💬/💬 Chat.md>
[Finder]: <../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>
[Broker]: <../../🤵 Broker helper/🤵 Broker 🤲 helper.md>