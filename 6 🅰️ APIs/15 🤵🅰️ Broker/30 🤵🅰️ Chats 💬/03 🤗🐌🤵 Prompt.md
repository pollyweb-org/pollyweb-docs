<!-- Docs: https://quip.com/FNbzAVSVu9z6#temp:C:RCPf6c15c5e6e2d47c294917a750 -->

# 🤗🐌🤵 Prompt @ Broker

> The [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) forwards the [Prompt 🤔](<../../../9 😃 Talkers/10 📘 Talker specs/2 🤔 Prompt.md>) to the [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>).

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt 🤔.md>) flow.

<br/>

## 🐌 Async Message

```yaml
Header:
  From: any-host.com
  To: any-broker.com
  Subject: Prompt@Broker
Body:
  ChatID: <chat-uuid>
  PromptID: <prompt-uuid>
  TTL: 2023-04-01T05:00:30.001000Z
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>)
||`To`       | string  | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
||`Subject` | string | `Prompt@Broker`
|Body|`ChatID`   | uuid    | ID of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) on the [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
||`PromptID` | uuid    | Callback to [`Prompted@Host`](<../../50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>)
||`TTL`| timestamp | Expiration of [`Prompted@Host`](<../../50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) cache
|