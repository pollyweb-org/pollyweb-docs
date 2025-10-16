# 💼🐌🤵 Invite @ Broker

> Invites a [Host 🤗 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) into a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>).

> Part of the [🤗⏩🧑‍🦰 Invite @ Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗⏩ Host flows/🤗⏩🧑‍🦰 Invite 🛠️.md>) flow:
> <br/>• followed by [`Invited@Helper`](<../../../4 ⚙️ Solution/45 🤲 Helper domains/$ 🤲 Helpers/🤲🅰️ Helper methods/🤵🐌🤲 Invited.md>) message

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
|Header|`From`     | string  | Inviter [Consumer 💼](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) name
||`To`       | string  | [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Hello@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`Subject` | string | `Invite@Broker`
|Body|`ChatID`   | uuid    | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Hello@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`Helper`  | string  | Invitee [Helper 🤲 domain](<../../../4 ⚙️ Solution/45 🤲 Helper domains/$ 🤲 Helpers/🤲👥 Helper domain.md>) name
||`Code`     | string  | Related [Schema Code 🧩](<../../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
||`ConsumerKey` | uuid    | Callback for [`Consume@Consumer`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/💼🅰️ Consumer methods/🗄️🐌💼 Consume.md>)
||`Parameters`| object   | Optional parameters for the invite
|