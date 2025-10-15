# 🤵🐌🛠️ Invited @ Host

> Invests a [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) into a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

> Part of the [🤗⏩🧑‍🦰 Invite @ Host](<../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>) flow.
><br/> • preceded by the [`Invite@Host`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>) message

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.com
    To: any-invited.com
    Subject: Invited@Helper

Body:
    ChatID: <chat-uuid>
    Inviter: any-consumer.com
    Code: any-authority.com/ANY-CODE:1.0
    Callback: <callback-uuid>
    Parameters:
        Param1: Value1
        Param2: Value2
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) from [`Invite@Broker`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)
||`To`       | string  | [Helper 🛠️](<../../4 ⚙️ Solution/45 🛠️ Helper domains/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) from [`Invite@Broker`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)
||`Subject` | string | `Invited@Helper`
|Body|`ChatID`   | uuid    | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) from [`Invite@Broker`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)
||`Inviter`  | string  | [Consumer 💼 ](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/04 💼🎭 Consumer role.md>) from [`Invite@Broker`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)
||`Code`     | string  | [Code 🧩](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) from [`Invite@Broker`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)
||`Callback` | uuid    | Callback from [`Invite@Broker`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)
||`Parameters`| object   | Parameters from [`Invite@Broker`](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)
|