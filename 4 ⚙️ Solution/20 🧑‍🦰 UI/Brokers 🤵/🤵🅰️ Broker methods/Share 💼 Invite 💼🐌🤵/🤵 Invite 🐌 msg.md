<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

# 💼🐌🤵 Invite @ Broker

> Purpose
* Invites a [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) into a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

> Flow
* Part of the [`Invite` ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>) 
* followed by [`Invited@Helper`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>) message

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Invite@Broker

Body:
    Chat: <chat-uuid>
    Helper: any-helper.com
    Schema: any-authority.com/ANY-SCHEMA:1.0
    Hook: <hook-uuid>
    Parameters:
        Param1: Value1
        Param2: Value2
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`     | string  | Inviter [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>)  | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`To`       | string  | [Broker 🤵](<../../🤵🤲 Broker helper.md>) | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` | string | `Invite@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Helper`  | string  | Invitee [Helper 🤲](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) || [`Invited@`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>)
||`Schema`     | string  | Related [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) ||[`Invited@`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>)
||`Hook` | uuid    | Hook || [`Invited@`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>)
||`Parameters`| object   | Optional parameters ||[`Invited@`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>)
|