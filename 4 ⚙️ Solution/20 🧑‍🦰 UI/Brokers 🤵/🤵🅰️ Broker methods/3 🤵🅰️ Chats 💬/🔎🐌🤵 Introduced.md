<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->

# 🔎🐌🤵 Introduced @ Broker

> The [Finder 🔎 domain](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) finished the introduction.

> Used by [🔎⏩🧑‍🦰 Introduce ⓘ](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>)

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

|Object|Property|Type|Description
|-|-|-|-
| Header | `From`    | string | [Finder 🔎](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>) from [`Introduce@Finder`](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/🤵🐌🔎 Introduce.md>)
|        | `To`      | string | [Broker 🤵](<../../🤵🤲 Broker helper.md>)  from [`Introduce@Finder`](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/🤵🐌🔎 Introduce.md>) |
|        | `Subject` | string | `Introduced@Broker`
| Body   | `Chat`  | uuid   | [Chat 💬 ID](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) from [`Introduce@Finder`](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/🤵🐌🔎 Introduce.md>)
|