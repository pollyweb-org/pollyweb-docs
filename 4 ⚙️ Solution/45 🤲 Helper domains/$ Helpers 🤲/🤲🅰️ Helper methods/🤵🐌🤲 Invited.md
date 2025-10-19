# 🤵🐌🛠️ Invited @ Host

> Invests a [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) into a [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>).

> Part of the [🤗⏩🧑‍🦰 Invite @ Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Invite 🤲.md>) flow.
><br/> • preceded by the [`Invite@Host`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>) message

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-invited.com
    Subject: Invited@Helper

Body:
    Chat: <chat-uuid>
    Inviter: any-consumer.dom
    Schema: any-authority.com/ANY-SCHEMA:1.0
    Callback: <callback-uuid>
    Parameters:
        Param1: Value1
        Param2: Value2
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) from [`Invite@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`To`       | string  | [Helper 🤲](<../🤲👥 Helper domain.md>) from [`Invite@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`Subject` | string | `Invited@Helper`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) from [`Invite@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`Inviter`  | string  | [Consumer 💼 ](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) from [`Invite@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`Schema`     | string  | [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) from [`Invite@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`Callback` | uuid    | Callback from [`Invite@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`Parameters`| object   | Parameters from [`Invite@Broker`](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Invite.md>)
|