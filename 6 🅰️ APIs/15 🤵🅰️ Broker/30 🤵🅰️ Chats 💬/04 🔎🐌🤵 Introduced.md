<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->

# 🔎🐌🤵 Introduced @ Broker

> The [Finder 🔎 domain](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) finished the introduction.

> Used by [🔎⏩🧑‍🦰 Introduce ⓘ](<../../../5 ⏩ Flows/40 🔎⏩ Finders/01 🔎⏩🧑‍🦰 Introduce.md>)

<br/>

## 🐌 Async Message

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
| Header | `From`    | string | [Finder 🔎 domain](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) 
|        | `To`      | string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) |
|        | `Subject` | string | `Introduced@Broker`
| Body   | `ChatID`  | uuid   | ID of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) 
|