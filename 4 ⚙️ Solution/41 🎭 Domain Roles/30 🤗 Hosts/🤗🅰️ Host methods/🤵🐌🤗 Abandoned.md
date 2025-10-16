# 🤵🐌🤗 Abandoned @ Host


> Part of the [Abandon session 🧑‍🦰👉🤗](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>) flow.

Tells all [Host 🤗 domains](<../🤗🎭 Host role.md>) in [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>) that the user abandoned it.

<br/>


## Async Message 🐌


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
| Header    | `From`        | string    | [Broker 🤵](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) from [`Help@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Help.md>)
|           | `To`          | string    | [Host 🤗 domain](<../🤗🎭 Host role.md>) from:<br/>- [`Hello@Host`](<🤵🐌🤗 Hello.md>) <br/>- [`Invited@Helper`](<../../../45 🤲 Helper domains/$ 🤲 Helpers/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>) <br/>-  [`Disclose@Vault`](<../../80 🗄️ Vaults/🗄️🅰️ Vault methods/🤵🐌🗄️ Disclose.md>)
|           | `Subject`     | string    | `Abandoned@Host`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../../35 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<🤵🐌🤗 Hello.md>)
|

<br/>


