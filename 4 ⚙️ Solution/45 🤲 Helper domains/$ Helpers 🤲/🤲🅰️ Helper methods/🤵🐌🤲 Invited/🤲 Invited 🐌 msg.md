# 🤵🐌🤲 Invited @ Helper

> Purpose
* Invests a [Host 🤗 domain][Host] into a [Chat 💬][Chat].

> Flow
* Part of the [`Invite` ⏩ flow][Invite flow].
* preceded by the [`Invite@Host`][Invite@] message

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-invited.dom
    Subject: Invited@Helper

Body:
    Chat: <chat-uuid>
    Inviter: any-consumer.dom
    Schema: any-authority.dom/ANY-SCHEMA:1.0
    Hook: <Hook-uuid>
    Inputs:
        Input1: Value1
        Input2: Value2
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|text| [Broker 🤵][Broker] | [`Invite@`][Invite@]
||`To`|string  | [Helper 🤲][Helper] | [`Invite@`][Invite@]
||`Subject` |text| `Invited@Helper`
|Body|`Chat`   | uuid    | [Chat 💬][Chat] | [`Invite@`][Invite@]
||`Inviter`  | string  | [Consumer 💼 ][Consumer] | [`Invite@`][Invite@]
||`Schema`     | string  | [Schema 🧩][Schema] | [`Invite@`][Invite@]
||`Hook` | uuid    | Hook | [`Invite@`][Invite@]|[`Collect@`][Collect@]
||`Inputs`| [map][map]   | Inputs | [`Invite@`][Invite@]
|

[Invite@]: <../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Share 💼 Invite 💼🐌🤵/🤵 Invite 🐌 msg.md>
[Helper]: <../../🤲👥 Helper domain.md>
[Chat]: <../../../../35 💬 Chats/Chats 💬/💬 Chat.md>
[Consumer]: <../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>
[Schema]: <../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>
[Collect@]: <../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>
[map]: <../../../../37 Scripts 📃/📃 Holders 🧠/🧠 Input holders/Map holders.md>
[Host]: <../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>
[Invite flow]: <../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>
[Broker]: <../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>