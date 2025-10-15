# 🤵🐌🤗 Abandoned @ Host


> Part of the [Abandon session 🧑‍🦰👉🤗](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>) flow.

Tells all [Host 🤗 domains](<$ 🤗🎭 Host role.md>) in [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) that the user abandoned it.

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
| Header    | `From`        | string    | [Broker 🤵](<../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Help@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/07 🧑‍🦰🐌🤵 Help.md>)
|           | `To`          | string    | [Host 🤗 domain](<$ 🤗🎭 Host role.md>) from:<br/>- [`Hello@Host`](<51 🤵🐌🤗 Hello@Host.md>) <br/>- [`Invited@Helper`](<../../../6 🅰️ APIs/49 🛠️🅰️ Helper/11 🤵🐌🛠️ Invited.md>) <br/>-  [`Disclose@Vault`](<../80 🗄️ Vaults/🗄️🅰️ Vault Methods/🤵🐌🗄️ Disclose.md>)
|           | `Subject`     | string    | `Abandoned@Host`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Hello@Host`](<51 🤵🐌🤗 Hello@Host.md>)
|

<br/>


