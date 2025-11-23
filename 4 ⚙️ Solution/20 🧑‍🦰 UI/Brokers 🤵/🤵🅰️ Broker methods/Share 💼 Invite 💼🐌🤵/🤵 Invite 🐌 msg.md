<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

# 💼🐌🤵 Invite @ Broker

> Purpose
* Invites a [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) into a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

> Flow
* Part of the [`Invite` ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>) 
* followed by [`Invited@Helper`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>) message

## Async Message 🐌

```yaml
Header:
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Invite@Broker

Body:
    Chat: <chat-uuid>
    Helper: any-helper.dom
    Schema: any-authority.dom/ANY-SCHEMA:1.0
    Hook: <hook-uuid>
    Inputs:
        Input1: Value1
        Input2: Value2
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|[text](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| Inviter [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>)  | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`To`|[text](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)  | [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` |[text](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| `Invite@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Helper`  | [text](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)  | Invitee [Helper 🤲](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) || [`Invited@`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>)
||`Schema`     | [text](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)  | Related [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) ||[`Invited@`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>)
||`Hook` | uuid    | Hook || [`Invited@`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>)
||`Inputs`| [map](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)   | Optional inputs ||[`Invited@`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited/🤲 Invited 🐌 msg.md>)
|