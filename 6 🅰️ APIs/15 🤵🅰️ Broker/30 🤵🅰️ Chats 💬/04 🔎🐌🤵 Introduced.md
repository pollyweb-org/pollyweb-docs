<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->

# 🔎🐌🤵 Introduced @ Broker

> The [Finder 🔎 domain](<../../../4 ⚙️ Solution/30 🫥 Agents/40 🔎 Finders/02 🔎🫥 Finder vault.md>) finished the introduction.

> Used by [🔎⏩🧑‍🦰 Introduce ⓘ](<../../../5 ⏩ Flows/40 🔎⏩ Finders/01 🔎⏩🧑‍🦰 Introduce 🤗.md>)

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
| Header | `From`    | string | [Finder 🔎](<../../../4 ⚙️ Solution/30 🫥 Agents/40 🔎 Finders/02 🔎🫥 Finder vault.md>) from [`Introduce@Finder`](<../../40 🔎🅰️ Finder/01 🤵🐌🔎 Introduce.md>)
|        | `To`      | string | [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>)  from [`Introduce@Finder`](<../../40 🔎🅰️ Finder/01 🤵🐌🔎 Introduce.md>) |
|        | `Subject` | string | `Introduced@Broker`
| Body   | `ChatID`  | uuid   | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) from [`Introduce@Finder`](<../../40 🔎🅰️ Finder/01 🤵🐌🔎 Introduce.md>)
|