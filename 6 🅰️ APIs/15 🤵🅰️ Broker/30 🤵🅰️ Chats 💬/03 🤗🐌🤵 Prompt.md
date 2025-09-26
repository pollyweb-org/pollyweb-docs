<!-- Docs: https://quip.com/FNbzAVSVu9z6#temp:C:RCPf6c15c5e6e2d47c294917a750 -->

# 🤗🐌🤵 Prompt @ Broker

> The [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) forwards the [Prompt 🤔](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/02 🤔 Prompt.md>) to the [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/02 📣 Notifier domain.md>).

> Used by [🤗⏩🧑‍🦰 Prompt @ Host](<../../../5 ⏩ Flows/39 🤗⏩ Hosts/01 🤗⏩🧑‍🦰 Prompt.md>).

<br/>

## Async Message 🐌

```yaml
Header:
  From: any-host.org
  To: any-broker.org
  Subject: Prompt@Broker
Body:
  ChatID: <chat-uuid>
  PromptID: <prompt-uuid>
```


|Object|Property|Type|Description
|-|-|-|-
|Header|`From`     | string  | [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>)
||`To`       | string  | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
||`Subject` | string | `Prompt@Broker`
|Body|`ChatID`   | UUID    | ID of the [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) on the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)
||`PromptID` | UUID    | Callback to download the [Prompt 🤔](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/02 🤔 Prompt.md>) from the [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/04 🤗🎭 Host role.md>) via [Prompted@Host](<../../50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>)
|