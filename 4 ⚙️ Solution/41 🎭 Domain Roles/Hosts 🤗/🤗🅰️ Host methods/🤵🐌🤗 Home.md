# 🧑‍🦰🐌🤗 Home @ Host

> Shows the main menu of the [Host 🤗 domain](<../🤗🎭 Host role.md>).

> Used by:
> <br/>• [🧑‍🦰👉🗄️ Unbind](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Vaults 🗄️/🧑‍🦰💬🤵 Unbind 🗄️.md>) flow
> <br/>• [🧑‍🦰👉🤵 Remove Token](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Tokens 🎫/🧑‍🦰💬🤵 Remove 🎫.md>) flow
> <br/>• [🧑‍🦰👉🤵 Host home](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Chats 💬/🧑‍🦰💬🤵 Host home.md>) flow

<br/>

## 💬 Chat

Consider the following [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) as an example.

| [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
| - | - | - |
| 🤗 [Host](<../🤗🎭 Host role.md>) | 😃 What do you need? <br/> - [ Something ] <br> - [ Something else ]  | 
||


<br/>

## 😃 Talker 

The associated [Talker 😃](<../../../35 💬 Chats/😃 Talkers/😃 Talker.md>) would be the following.

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
|Header|`From`|string | [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) name
||`To`|string| [Host 🤗 domain](<../🤗🎭 Host role.md>) name
||`Subject`|string|`Home@Host`
|Body  |`ChatID`   |uuid  | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<🤵🐌🤗 Hello.md>)
|