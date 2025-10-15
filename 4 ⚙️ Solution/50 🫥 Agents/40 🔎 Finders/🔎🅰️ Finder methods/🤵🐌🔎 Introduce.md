
# Introduce @ [Finder](<../🔎🫥 Finder agent.md>)

* Ask for a [Finder 🔎 domain](<../🔎🫥 Finder agent.md>) 
    * to introduce a [Host 🤗 domain](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) 
    * to the user in a new [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>).
* Used by the [🔎⏩🧑‍🦰 Introduce 🤗](<../🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>) flow:
    * followed by [`Introduced@Broker`](<../../../../6 🅰️ APIs/15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/04 🔎🐌🤵 Introduced.md>)

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-broker.com
    To: any-finder.com
    Subject: Introduce@Broker

Body:
    ChatID: <chat-uuid>
    Host: any-host.com
```

|Object|Property|Type|Description
|-|-|-|-
| Header | `From`    | string | [Finder 🔎](<../🔎🫥 Finder agent.md>) register as user [Agent 🫥](<../../$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) 
|        | `To`      | string | [Broker 🤵](<../../../45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>) |
|        | `Subject` | string | `Introduced@Broker`
| Body   | `ChatID`  | uuid   | [Chat 💬](<../../../20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
|       | `Host`| string | [Host 🤗](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) from [`Converse@Notifier`](<../../../20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
|