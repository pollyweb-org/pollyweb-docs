# 💼🐌🤵 Inform @ Broker

> Part of the [Consumer Inform ⏩ flow](<../../../5 ⏩ Flows/20 💼⏩ Consumers/02 💼⏩🧑‍🦰 Inform 📝.md>)

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
|Header|`From`     | string  | [Consumer 💼 domain](<../../../4 ⚙️ Solution/25 Data/27 💼 Consumers/04 💼🎭 Consumer role.md>) name
||`To`       | string  | [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) from [`Hello@Host`](<../../50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>)
||`Subject` | string | `Inform@Broker`
|Body|`ChatID`   | uuid    | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID from [`Hello@Host`](<../../50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>)
||`Form` | string | Form key for [`Form@Graph`](<../../45 🕸🅰️ Graph/01 👥🚀🕸 Form.md>)
|