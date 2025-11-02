
# Introduce @ [Finder](<../../🔎 Finder agent/🔎 Finder 🫥 agent.md>)

> Purpose

* Ask for a [Finder 🔎 domain](<../../🔎 Finder agent/🔎 Finder 🫥 agent.md>) 
    * to introduce a [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) 
    * to the user in a new [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

> Used by 

*  [🔎⏩🧑‍🦰 Introduce 🤗](<../../🔎⏩ Finder flows/Introduce 🔎⏩🧑‍🦰/🔎 Introduce ⏩ flow.md>) flow:
* followed by [`Introduced@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Introduced 🔎🐌🤵/🤵 Introduced 🐌 msg.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-finder.dom
    Subject: Introduce@Broker

Body:
    Chat: <chat-uuid>
    Host: any-host.dom
    Language: en-us
    Reviewer: any-reviewer.dom
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header |`From`|domain| [Finder 🔎](<../../🔎 Finder agent/🔎 Finder 🫥 agent.md>) | [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|        |`To`|domain| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Converse@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>) |[`Prompt@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|        | `Subject` | string | `Introduced@Broker`
| Body   | `Chat`  | uuid   | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Converse@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>) | [`Prompt@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|       | `Host`| domain | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | [`Converse@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>) | [`Identity@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)
|       | `Language` | string | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) language | [`Language@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Language 🧑‍🦰🐌🤵/🤵 Language 🐌 msg.md>) | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| | `Reviewer` | domain | [Reviewer ⭐ agent](<../../../Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>)
|