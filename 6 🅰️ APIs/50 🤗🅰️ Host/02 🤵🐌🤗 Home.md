<!-- #TODO -->

# 🧑‍🦰🐌🤗 Home @ Host

> Shows the Host's main menu.

> Used by:
> <br/>* [🧑‍🦰👉🤵 Abandon session](<../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>)
> <br/>* [🧑‍🦰👉🤵 Host home](<../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/20 👉💬 Chats/02 🧑‍🦰👉🤵 Host home.md>)

<br/>

## Chat

| Service | Prompt | User
| - | - | - |
| 🤗 [Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What do you need? <br/> - [ Something ] <br> - [ Something else ]  | 
||

<br/>

# Async Message

```yaml
Header:
    From: any-broker.com
    To: any-host.com
    Subject: Home@Host

Body:
    ChatID: <chat-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`To`|string| [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) name
||`Subject`|string|`Home@Host`
|Body  |`ChatID`   |UUID  | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID on the [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
|