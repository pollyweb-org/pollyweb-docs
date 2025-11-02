
# Introduce @ [Finder](<../🔎🫥 Finder agent.md>)

> Purpose

* Ask for a [Finder 🔎 domain](<../🔎🫥 Finder agent.md>) 
    * to introduce a [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) 
    * to the user in a new [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

> Used by 

*  [🔎⏩🧑‍🦰 Introduce 🤗](<../🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>) flow:
* followed by [`Introduced@Broker` 🅰️ method](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Introduced 🔎🐌🤵/🤵 Introduced 🐌 msg.md>)

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
```

|Object|Property|Type|Description
|-|-|-|-
| Header |`From`|domain| [Finder 🔎](<../🔎🫥 Finder agent.md>) register as user [Agent 🫥](<../../$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) 
|        |`To`|domain| [Broker 🤵](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/Broker 🤵 helper 🤲.md>) from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>) |
|        | `Subject` | string | `Introduced@Broker`
| Body   | `Chat`  | uuid   | [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>) from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>)
|       | `Host`| string | [Host 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>)
|