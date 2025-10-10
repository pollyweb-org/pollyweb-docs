# 🤵🐌🤗 Abandoned @ Host


> Part of the [Abandon session 🧑‍🦰👉🤗](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>) flow.

Tells all [Host 🤗 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) in [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) that the user abandoned it.
* These [Host 🤗 domains](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) were added by:
    * [`Hello@Host`](<01 🤵🐌🤗 Hello.md>)
    * [`Invited@Helper`](<11 🤵🐌🤗 Invited.md>)

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
|           | `To`          | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) name
|           | `Subject`     | string    | `Abandoned@Host`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID from [`Hello@Host`](<01 🤵🐌🤗 Hello.md>)
|

<br/>


