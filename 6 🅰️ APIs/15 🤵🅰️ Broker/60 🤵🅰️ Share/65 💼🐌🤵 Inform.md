# 💼🐌🤵 Inform @ Broker

> Part of the [Consumer Inform ⏩ flow](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/02 💼⏩🧑‍🦰 Inform 📝.md>)

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
|Header|`From`     | string  | [Consumer 💼 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) name
||`To`       | string  | [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Hello@Host`](<../../50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>)
||`Subject` | string | `Inform@Broker`
|Body|`ChatID`   | uuid    | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID from [`Hello@Host`](<../../50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>)
||`Form` | string | Form key for [`Form@Graph`](<../../45 🕸🅰️ Graph/01 👥🚀🕸 Form.md>)
|