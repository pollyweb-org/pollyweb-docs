# 🤵🐌🤗 Abandoned @ Host

> Tells the [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) that a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) was abandoned by the user.


> Part of the [Abandon session 🧑‍🦰👉🤗](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>) flow.

<br/>


## 🐌 Async Message


```yaml
Header:
    From: any-broker.com
    To: any-host.com
    Subject: Abandoned@Host

Body: 
    ChatID: <chat-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
|           | `To`          | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) name
|           | `Subject`     | string    | `Abandoned@Host`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
|

<br/>


