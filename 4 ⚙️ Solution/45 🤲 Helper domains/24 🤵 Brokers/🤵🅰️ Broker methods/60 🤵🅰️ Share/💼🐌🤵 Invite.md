# 💼🐌🤵 Invite @ Broker

> Invites a [Host 🤗 domain](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) into a [Chat 💬](<../../../../35 Chats/💬 Chats/💬 Chat.md>).

> Part of the [🤗⏩🧑‍🦰 Invite @ Host](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Invite 🤲.md>) flow:
> <br/>• followed by [`Invited@Helper`](<../../../$ 🤲 Helpers/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>) message

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-consumer.com
    To: any-broker.com
    Subject: Invite@Broker

Body:
    ChatID: <chat-uuid>
    Helper: any-helper.com
    Code: any-authority.com/ANY-CODE:1.0
    ConsumerKey: <consumer-key-uuid>
    Parameters:
        Param1: Value1
        Param2: Value2
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | Inviter [Consumer 💼](<../../../../41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) name
||`To`       | string  | [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Hello@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`Subject` | string | `Invite@Broker`
|Body|`ChatID`   | uuid    | [Chat 💬](<../../../../35 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`Helper`  | string  | Invitee [Helper 🤲 domain](<../../../$ 🤲 Helpers/🤲👥 Helper domain.md>) name
||`Code`     | string  | Related [Schema Code 🧩](<../../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
||`ConsumerKey` | uuid    | Callback for [`Consume@Consumer`](<../../../../41 🎭 Domain Roles/27 💼 Consumers/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>)
||`Parameters`| object   | Optional parameters for the invite
|