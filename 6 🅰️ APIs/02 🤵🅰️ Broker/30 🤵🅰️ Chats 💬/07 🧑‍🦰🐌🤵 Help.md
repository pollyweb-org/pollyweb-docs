# 🧑‍🦰🐌🤵 Help @ Broker

> Asks the Broker to join a Chat to help.

> Used in:
> <br/> * [🧑‍🦰👉🤵 Host Home](<../../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/20 👉💬 Chats/02 🧑‍🦰👉🤵 Host home.md>)
><br/> * [🧑‍🦰👉🤵 Abandon Chat](<../../../5 ⏩ Flows/02 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>)

<br/>

## Chat

| Service | Prompt | User
| - | - | - |
...
| 🤗 [Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Continue [Yes, No] 
| | | > Broker 🤵 |
| 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 What do you need? <br/> - [ Home ] menu  <br/> - [ Abandon ] Chat <br/> - [ Something else ] 
|

<br/>

# Async Message 🐌

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Help@Broker

Body:
    ChatID: <chat-uuid>
```