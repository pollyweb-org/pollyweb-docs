# 🤵🐌🛠️ Invited @ Host

> Invests a [Host 🤗 domain](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) into a [Chat 💬](<../../../35 Chats/12 💬 Chats/💬 Chat.md>).

> Part of the [🤗⏩🧑‍🦰 Invite @ Host](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Invite 🤲.md>) flow.
><br/> • preceded by the [`Invite@Host`](<../../24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Invite.md>) message

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
|Header|`From`     | string  | [Broker 🤵](<../../24 🤵 Brokers/🤵🤲 Broker helper.md>) from [`Invite@Broker`](<../../24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`To`       | string  | [Helper 🤲](<../🤲👥 Helper domain.md>) from [`Invite@Broker`](<../../24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`Subject` | string | `Invited@Helper`
|Body|`ChatID`   | uuid    | [Chat 💬](<../../../35 Chats/12 💬 Chats/💬 Chat.md>) from [`Invite@Broker`](<../../24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`Inviter`  | string  | [Consumer 💼 ](<../../../41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) from [`Invite@Broker`](<../../24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`Code`     | string  | [Code 🧩](<../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) from [`Invite@Broker`](<../../24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`Callback` | uuid    | Callback from [`Invite@Broker`](<../../24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Invite.md>)
||`Parameters`| object   | Parameters from [`Invite@Broker`](<../../24 🤵 Brokers/🤵🅰️ Broker methods/60 🤵🅰️ Share/💼🐌🤵 Invite.md>)
|