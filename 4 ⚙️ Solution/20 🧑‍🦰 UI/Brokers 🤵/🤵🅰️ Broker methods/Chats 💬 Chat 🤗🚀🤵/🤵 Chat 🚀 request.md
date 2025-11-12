# 🧑‍🦰🚀🤵 Chat @ Broker

> Implementation 
* Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* Implemented by the [`Chat` 📃 handler](<🤵 Chat 📃 handler.md>)

> Purpose
* The [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * returns the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) details
    * to a [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).

> Used in
* [`CHAT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CHAT 💬/💬 CHAT ⌘ cmd.md>) command


## Synchronous Request 🚀
  
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
| Header    |`From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|           |`To`|domain| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|           | `Subject`| string|  `Chat@Broker`
| Body|`Chat`| uuid | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|


## Response 


```yaml
ID: <chat-uuid>
PublicKey: ... 
Timezone: UTC+1
Language: en-us

# Locator
Schema: nlweb.dom/THING
Key: MY-THING-ID
Parameters: 
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
| | `ID`        | uuid  | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Converse@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>)
|| `PublicKey` |string| For  [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)  | |[`Prompted@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>)<br/>[`Reply@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>) <br/>[`Download@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Download 🧑‍🦰🚀🤗/🤗 Download 🚀 request.md>)
|| `Timezone`|string| For [`.Now`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Now}.md>) and [`.Today`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Today}.md>)  
|| `Language` |string| For the [`.Translate`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Translate}.md>) function | [`Language@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Language 🧑‍🦰🐌🤵/🤵 Language 🐌 msg.md>) | [`Prompt@`](<../Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
|           | `Schema`    | string    | Locator  [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`Assess@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)
|           | `Key` | string    | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) | [`Assess@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | 
|| `Parameters`| object | Custom parameters | [`Assess@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)
|           | `Tokens`  | uuid[] | Host  [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)  | [`Offer@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
|| `Binds`   | uuid[] | Host [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)  | [`Bound@`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|


<br/>
