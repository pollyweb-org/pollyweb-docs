<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->

# 🔎🐌🤵 Introduced @ Broker

> The [Finder 🔎 domain](<../../../4 ⚙️ Solution/50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>) finished the introduction.

> Used by [🔎⏩🧑‍🦰 Introduce ⓘ](<../../../4 ⚙️ Solution/50 🫥 Agent domains/40 🔎 Finders/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-finder.com
    To: any-broker.com
    Subject: Introduced@Broker

Body:
    ChatID: <chat-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header | `From`    | string | [Finder 🔎](<../../../4 ⚙️ Solution/50 🫥 Agent domains/40 🔎 Finders/🔎🫥 Finder agent.md>) from [`Introduce@Finder`](<../../../4 ⚙️ Solution/50 🫥 Agent domains/40 🔎 Finders/🔎🅰️ Finder methods/🤵🐌🔎 Introduce.md>)
|        | `To`      | string | [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>)  from [`Introduce@Finder`](<../../../4 ⚙️ Solution/50 🫥 Agent domains/40 🔎 Finders/🔎🅰️ Finder methods/🤵🐌🔎 Introduce.md>) |
|        | `Subject` | string | `Introduced@Broker`
| Body   | `ChatID`  | uuid   | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) from [`Introduce@Finder`](<../../../4 ⚙️ Solution/50 🫥 Agent domains/40 🔎 Finders/🔎🅰️ Finder methods/🤵🐌🔎 Introduce.md>)
|