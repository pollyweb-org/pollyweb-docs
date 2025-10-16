# 🧑‍🦰🐌🤗 Home @ Host

> Shows the main menu of the [Host 🤗 domain](<../🤗🎭 Host role.md>).

> Used by:
> <br/>• [🧑‍🦰👉🗄️ Unbind](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/03 🧑‍🦰👉🗄️ Unbind.md>) flow
> <br/>• [🧑‍🦰👉🤵 Remove Token](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/03 🧑‍🦰👉🤵 Remove token.md>) flow
> <br/>• [🧑‍🦰👉🤵 Host home](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/02 🧑‍🦰👉🤵 Host home.md>) flow

<br/>

## 💬 Chat

Consider the following [Chat 💬](<../../../35 Chats/12 💬 Chats/💬 Chat.md>) as an example.

| [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 Chats/20 🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
| - | - | - |
| 🤗 [Host](<../🤗🎭 Host role.md>) | 😃 What do you need? <br/> - [ Something ] <br> - [ Something else ]  | 
||


<br/>

## 😃 Talker 

The associated [Talker 😃](<../../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>) would be the following.

```yaml
💬 Something:
- INFO|This is something.

💬 Something else:
- INFO|But this is something else!
```

<br/>

## Async Message 🐌

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
|Header|`From`|string | [Broker 🤵 domain](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) name
||`To`|string| [Host 🤗 domain](<../🤗🎭 Host role.md>) name
||`Subject`|string|`Home@Host`
|Body  |`ChatID`   |uuid  | [Chat 💬](<../../../35 Chats/12 💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<🤵🐌🤗 Hello.md>)
|