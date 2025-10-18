# 🤵🐌🤗 Abandoned @ Host


> Part of the [Abandon session 🧑‍🦰👉🤗](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Chats 💬/💬🤵 Abandon 💬.md>) flow.

Tells all [Host 🤗 domains](<../🤗🎭 Host role.md>) in [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) that the user abandoned it.

<br/>


## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-host.dom
    Subject: Abandoned@Host

Body: 
    Chat: <chat-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`        | string    | [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) from [`Join@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Join.md>)
|           | `To`          | string    | [Host 🤗 domain](<../🤗🎭 Host role.md>) from:<br/>- [`Hello@Host`](<🤵🐌🤗 Hello.md>) <br/>- [`Invited@Helper`](<../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>) <br/>-  [`Disclose@Vault`](<../../Vaults 🗄️/🗄️🅰️ Vault methods/to Share/🤵🐌🗄️ Disclose.md>)
|           | `Subject`     | string    | `Abandoned@Host`
| Body      | `Chat`      | uuid      | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<🤵🐌🤗 Hello.md>)
|

<br/>


