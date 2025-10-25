# 💼🐌🤵 Invite @ Broker

> Invites a [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) into a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>).

> Part of the [🤗⏩🧑‍🦰 Invite @ Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/🤗⏩🧑‍🦰 Invite 🤲.md>) flow:
> <br/>• followed by [`Invited@Helper`](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>) message

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

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | Inviter [Consumer 💼](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) name
||`To`       | string  | [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`Subject` | string | `Invite@Broker`
|Body|`Chat`   | uuid    | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`Helper`  | string  | Invitee [Helper 🤲 domain](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) name
||`Schema`     | string  | Related [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
||`Hook` | uuid    | Hook for [`Consume@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>)
||`Parameters`| object   | Optional parameters for the invite
|