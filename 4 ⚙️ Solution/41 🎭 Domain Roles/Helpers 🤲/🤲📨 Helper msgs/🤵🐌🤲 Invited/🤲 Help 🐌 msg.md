# 🤵🐌🤲 Help @ Helper

> Purpose
* Invests a [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) into a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

> Flow
* Part of the [`Invite` ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>).
* preceded by the [`Invite@Host`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>) message

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-helper.dom
    Subject: Help@Helper

Body:
    Chat: <chat-uuid>
    Consumer: any-consumer.dom
    Schema: any-authority.dom/ANY-SCHEMA:1.0
    Invite: <invite-uuid>
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) name | [`Invite@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
||`To`|string  | [Helper 🤲](<../../🤲 Helper/🤲🎭 Helper role.md>) name | [`Invite@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
||`Subject` |text| `Help@Helper`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Invite@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
||`Consumer`  | string  | [Consumer 💼 ](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) name | [`Invite@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
||`Schema`     | string  | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) code | [`Invite@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)
||`Invite` | uuid    | [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) invite | [`Invite@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>)|[`Collect@`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>)
|