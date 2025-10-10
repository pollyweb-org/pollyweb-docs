
# Introduce @ [Finder](<../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>)


> Used by [👉 Introduce](<../../5 ⏩ Flows/40 🔎⏩ Finders/01 🔎⏩🧑‍🦰 Introduce 🤗.md>)


> Ask for a [Finder 🔎 domain](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) to introduce a Host to the user.

<br/>

## 🐌 Async Message

```yaml
Header:
    From: any-broker.com
    To: any-finder.com
    Subject: Introduce@Broker

Body:
    ChatID: <chat-uuid>
    Host: any-host.com
```

|Object|Property|Type|Description
|-|-|-|-
| Header | `From`    | string | [Finder 🔎](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) from [`Introduce@Finder`](<../../40 🔎🅰️ Finder/01 🤵🐌🔎 Introduce.md>)
|        | `To`      | string | [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)  from [`Introduce@Finder`](<../../40 🔎🅰️ Finder/01 🤵🐌🔎 Introduce.md>) |
|        | `Subject` | string | `Introduced@Broker`
| Body   | `ChatID`  | uuid   | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) from [`Introduce@Finder`](<../../40 🔎🅰️ Finder/01 🤵🐌🔎 Introduce.md>)
|       | `Host`| string | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) to introduce
|