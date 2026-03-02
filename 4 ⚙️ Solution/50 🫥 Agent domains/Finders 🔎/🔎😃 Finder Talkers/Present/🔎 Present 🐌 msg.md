
# Present @ [Finder](<../../🔎 Finder agent/🔎 Finder 🫥 agent.md>)

> Purpose

* Ask for a [Finder 🔎 domain](<../../🔎 Finder agent/🔎 Finder 🫥 agent.md>) 
    * to introduce a [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) 
    * to the user in a new [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

> Used by 

*  [🔎⏩🧑‍🦰 Present 🤗](<../../🔎⏩ Finder flows/Present 🔎⏩🧑‍🦰/🔎 Present ⏩ flow.md>) flow:

<br/>

## Event

```yaml
Broker: any-broker.dom
Chat: <chat-uuid>
Host: any-host.dom
Language: en-us
Reviewer: any-reviewer.dom
```

||Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| |`Finder`|text| [Finder 🔎](<../../🔎 Finder agent/🔎 Finder 🫥 agent.md>) | [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|        |`Broker`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | [`Open@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) |[`Prompt@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|   | `Chat`  | uuid   | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Open@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) | [`Prompt@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|       | `Host`| domain | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | [`Open@Notifier`](<../../../../20 🧑‍🦰 UI/Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) | [`About@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 About/🕸 About 🚀 call.md>)
|       | `Language` |text| [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) language | Pop 🎈 | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>)
| | `Reviewer` | domain | [Reviewer ⭐](<../../../Reviewers ⭐/⭐ Reviewer agent/⭐ Reviewer 🫥 agent.md>) | [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>) | [`Reviews@Reviewer`](<../../../Reviewers ⭐/⭐📨 Reviewer msgs/Reviews 🔎🚀⭐/🔎🚀⭐ Reviews.md>)
|