
# Introduce @ [Finder](<../../4 ⚙️ Solution/30 🫥 Agents/40 🔎 Finders/02 🔎🫥 Finder vault.md>)

* Ask for a [Finder 🔎 domain](<../../4 ⚙️ Solution/30 🫥 Agents/40 🔎 Finders/02 🔎🫥 Finder vault.md>) 
    * to introduce a [Host 🤗 domain](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) 
    * to the user in a new [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>).
* Used by the [🔎⏩🧑‍🦰 Introduce 🤗](<../../5 ⏩ Flows/40 🔎⏩ Finders/01 🔎⏩🧑‍🦰 Introduce 🤗.md>) flow:
    * followed by [`Introduced@Broker`](<../15 🤵🅰️ Broker/30 🤵🅰️ Chats 💬/04 🔎🐌🤵 Introduced.md>)

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
| Header | `From`    | string | [Finder 🔎](<../../4 ⚙️ Solution/30 🫥 Agents/40 🔎 Finders/02 🔎🫥 Finder vault.md>) register as user [Agent 🫥](<../../4 ⚙️ Solution/30 🫥 Agents/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) 
|        | `To`      | string | [Broker 🤵](<../../4 ⚙️ Solution/45 🛠️ Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Converse@Notifier`](<../65 📣🅰️ Notifier/02 📣💬🅰️ Chats/21 🤵🐌📣 Converse.md>) |
|        | `Subject` | string | `Introduced@Broker`
| Body   | `ChatID`  | uuid   | [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) from [`Converse@Notifier`](<../65 📣🅰️ Notifier/02 📣💬🅰️ Chats/21 🤵🐌📣 Converse.md>)
|       | `Host`| string | [Host 🤗](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) from [`Converse@Notifier`](<../65 📣🅰️ Notifier/02 📣💬🅰️ Chats/21 🤵🐌📣 Converse.md>)
|