# 💼🐌🤵 Invite @ Broker

> About
* Invites a [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) into a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).
* Part of the [`Invite` ⏩ flow](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>) 
* followed by [`Help@Helper`](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Help 🐌 msg.md>) message
* Implemented by the [`Invite@Broker` 📃 handler](<🤵 Invite 📃 handler.md>)

<br/>

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
    Invite: <invite-uuid>
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|[text](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| Inviter [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>)  | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`To`|[text](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)  | [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>) | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject` |[text](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| `Invite@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Helper`  | [text](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)  | Invitee [Helper 🤲](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) || [`Help@Helper`](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Help 🐌 msg.md>)
||`Schema`     | [text](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)  | Related [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) ||[`Help@Helper`](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Help 🐌 msg.md>)
||`Invite` | uuid    | [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) Invite || [`Help@Helper`](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/🤵🐌🤲 Invited/🤲 Help 🐌 msg.md>)
|