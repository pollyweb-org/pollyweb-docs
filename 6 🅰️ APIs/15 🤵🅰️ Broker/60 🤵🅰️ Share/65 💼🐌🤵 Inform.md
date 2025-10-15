# 💼🐌🤵 Inform @ Broker

> Part of the [Consumer Inform ⏩ flow](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/⏩ Consumer flows/💼⏩🧑‍🦰 Inform 📝.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-consumer.com
    To: any-broker.com
    Subject: Inform@Broker

Body:
    ChatID: <chat-uuid>
    Form: AnyForm
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Consumer 💼 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) name
||`To`       | string  | [Broker 🤵](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Hello@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/51 🤵🐌🤗 Hello@Host.md>)
||`Subject` | string | `Inform@Broker`
|Body|`ChatID`   | uuid    | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Hello@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/51 🤵🐌🤗 Hello@Host.md>)
||`Form` | string | Form key for [`Form@Graph`](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/50 🕸 Graphs/🕸🅰️ Graph methods/👥🚀🕸 Form.md>)
|