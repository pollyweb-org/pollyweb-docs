# 💼🐌🤵 Invite @ Broker

> Invites a [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/05 💬 Chats/04 🤗🎭 Host role.md>) into a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/05 💬 Chats/01 💬 Chat.md>).

> Part of the [🤗⏩🧑‍🦰 Invite @ Host](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite.md>) flow.

<br/>

## 🐌 Async Message

```yaml
Header:
    From: any-consumer.com
    To: any-broker.com
    Subject: Invite@Broker
Body:
    ChatID: <chat-uuid>
    Invitee: any-host.com
    Code: any-authority.com/ANY-CODE:1.0
    ConsumerKey: <consumer-key-uuid>
    Parameters:
        Param1: Value1
        Param2: Value2
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | Inviter [Consumer 💼 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
||`To`       | string  | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`Subject` | string | `Invite@Broker`
|Body|`ChatID`   | uuid    | ID of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/05 💬 Chats/01 💬 Chat.md>) 
||`Invitee`  | string  | Invitee [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/05 💬 Chats/04 🤗🎭 Host role.md>) name
||`Code`     | string  | Related [Schema Code 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
||`ConsumerKey` | uuid    | Callback for [Consume @ Consumer](<../../30 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>)
||`Parameters`| object   | Optional parameters for the invite
|