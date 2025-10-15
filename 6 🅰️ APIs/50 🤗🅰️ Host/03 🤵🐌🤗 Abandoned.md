# 🤵🐌🤗 Abandoned @ Host


> Part of the [Abandon session 🧑‍🦰👉🤗](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/03 🧑‍🦰👉🤵 Abandon chat.md>) flow.

Tells all [Host 🤗 domains](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) in [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) that the user abandoned it.

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
| Header    | `From`        | string    | [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Help@Broker`](<../15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/07 🧑‍🦰🐌🤵 Help.md>)
|           | `To`          | string    | [Host 🤗 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) from:<br/>- [`Hello@Host`](<01 🤵🐌🤗 Hello.md>) <br/>- [`Invited@Helper`](<../49 🛠️🅰️ Helper/11 🤵🐌🛠️ Invited.md>) <br/>-  [`Disclose@Vault`](<../95 🗄️🅰️ Vault/03 🤵🐌🗄️ Disclose.md>)
|           | `Subject`     | string    | `Abandoned@Host`
| Body      | `ChatID`      | uuid      | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Hello@Host`](<01 🤵🐌🤗 Hello.md>)
|

<br/>


