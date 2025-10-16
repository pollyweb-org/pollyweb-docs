
# Introduce @ [Finder](<../🔎🫥 Finder agent.md>)

* Ask for a [Finder 🔎 domain](<../🔎🫥 Finder agent.md>) 
    * to introduce a [Host 🤗 domain](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) 
    * to the user in a new [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>).
* Used by the [🔎⏩🧑‍🦰 Introduce 🤗](<../🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>) flow:
    * followed by [`Introduced@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🔎🐌🤵 Introduced.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.dom
    To: any-finder.dom
    Subject: Introduce@Broker

Body:
    ChatID: <chat-uuid>
    Host: any-host.dom
```

|Object|Property|Type|Description
|-|-|-|-
| Header | `From`    | string | [Finder 🔎](<../🔎🫥 Finder agent.md>) register as user [Agent 🫥](<../../$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) 
|        | `To`      | string | [Broker 🤵](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🤲 Broker helper.md>) from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>) |
|        | `Subject` | string | `Introduced@Broker`
| Body   | `ChatID`  | uuid   | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
|       | `Host`| string | [Host 🤗](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/2 📣 Notifiers/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
|