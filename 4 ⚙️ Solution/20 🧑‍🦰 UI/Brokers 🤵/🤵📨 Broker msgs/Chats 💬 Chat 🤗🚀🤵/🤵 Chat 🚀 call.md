# 🧑‍🦰🚀🤵 Chat @ Broker

> Implementation 
* Implements the [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>)
* Implemented by the [`Chat` 📃 handler](<🤵 Chat 📃 handler.md>)

> Purpose
* The [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>) 
    * returns the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) details
    * to a [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).

> Used in
* [`CHAT`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/CHAT 💬/💬 CHAT ⌘ cmd.md>) command


## Synchronous Call 🚀
  
```yaml
Header: 
    From: any-host.dom
    To: any-broker.dom
    Subject: Chat@Broker
Body:
    Chat: <chat-uuid>
```

| Object | Property | Type  | Description|Origin
|-|-|-|-|-
| Header    |`From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|           |`To`|text| [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|           | `Subject`|text|  `Chat@Broker`
| Body|`Chat`| uuid | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|


## Response 


```yaml
ID: <chat-uuid>
PublicKey: ... 
Timezone: UTC+1
Language: en-us

# Locator
Schema: pollyweb.org/THING
Key: MY-THING-ID
Inputs: 
    Param1: Value1
    Param2: Value2

# Shares
Binds: 
    - <bind-#1-uuid>
    - <bind-#2-uuid>
Tokens:
    - <token-#1-uuid>
    - <token-#2-uuid>
```


| | Property  | Type  | Description | Origin|Purpose
|-|-|-|-|-|-
| | `ID`        | uuid  | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Open@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
|| `PublicKey` |text| For [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/VERIFY ⌘/🔐 VERIFY ⌘ cmd.md>)  | |[`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>)<br/>[`Reply@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>) <br/>[`Download@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Download 🧑‍🦰🚀🤗/🤗 Download 🚀 call.md>)
|| `Timezone`|text| For [`.Now`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>) and [`.Today`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Today ⓕ.md>)  
|| `Language` |text| For [`TRANSLATE`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) | Pop 🎈  | [`Prompt@`](<../Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|           | `Key` | string    | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) | [`Locate@`](<../Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | 
|| `Inputs`| object | Custom parameters | [`Locate@`](<../Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)
|           | `Tokens`  | uuid[] | Host  [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)  | [`Issue@`](<../Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>)
|| `Binds`   | uuid[] | Host [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)  | [`Bound@`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|


<br/>
