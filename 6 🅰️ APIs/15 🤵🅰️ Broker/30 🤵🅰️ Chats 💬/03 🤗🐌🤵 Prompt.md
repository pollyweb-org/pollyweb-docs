<!-- Docs: https://quip.com/FNbzAVSVu9z6#temp:C:RCPf6c15c5e6e2d47c294917a750 -->

# 🤗🐌🤵 Prompt @ Broker

> Part of the [🤗⏩🧑‍🦰 Prompt 🤔](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/⏩ Host flows/🤗⏩🧑‍🦰 Prompt 🤔.md>) flow.

* The [Broker 🤵 domain](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) 
  * forwards the [Prompt 🤔](<../../../9 😃 Talkers/10 📘 Talker specs/20 🤔 Prompt.md>) 
  * to the [Notifier 📣 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/📣 Notifier domain.md>).

<br/>

## Async Message 🐌

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
|Header|`From`     | string  | [Host 🤗 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>)
||`To`       | string  | [Broker 🤵 domain](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)
||`Subject` | string | `Prompt@Broker`
|Body|`ChatID`   | uuid    | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID from [`Hello@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/🤵🐌🤗 Hello.md>)
||`PromptID` | uuid    | Callback to [`Prompted@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>)
||`TTL`| timestamp | Expiration of [`Prompted@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>) cache
|