# 🤵🐌🤗 Invited @ Host

> Invests a Host domain into a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/05 💬 Chats/01 💬 Chat.md>).

> Part of the [🤗⏩🧑‍🦰 Invite @ Host](<../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite.md>) flow.

<br/>

## 🐌 Async Message

```yaml
Header:
    From: any-broker.com
    To: any-invited.com
    Subject: Invited@Host
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
|Header|`From`     | string  | [Broker 🤵 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`To`       | string  | Invitee [Host 🤗 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/05 💬 Chats/04 🤗🎭 Host role.md>) name
||`Subject` | string | `Invited@Host`
|Body|`ChatID`   | uuid    | ID of the [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/05 💬 Chats/01 💬 Chat.md>) 
||`Inviter`  | string  | Inviter [Consumer 💼 domain](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
||`Code`     | string  | Related [Schema Code 🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
||`Callback` | uuid    | Callback from [Invite@Broker](<../15 🤵🅰️ Broker/60 🤵🅰️ Share/64 💼🐌🤵 Invite.md>)
||`Parameters`| object   | Optional parameters for the invite
|