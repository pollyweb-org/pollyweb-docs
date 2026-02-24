# 🤵🐌🤗 Hello @ Host

> Implementation

* Implemented by the [`Hello` 📃 handler](<🤗 Hello 📃 handler.md>)

> Purpose
* Starts a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with a [Host 🤗 domain](<../../🤗 Host role/🤗🎭 Host role.md>).

> Used by
* [🧑‍🦰👉🤗 Scan host QR @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap host locator 🔆🤗 /🧑‍🦰 Tap host locator ⏩ flow.md>)
* [🧑‍🦰👉🤗 Scan printer QR @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap alias locator 🔆🖨️ /🧑‍🦰 Tap alias locator ⏩ flow.md>)


## Async Message 🐌


```yaml
Header:
    From: any-broker.dom
    To: any-host.dom
    Subject: Hello@Host

Body:
    Chat: <chat-uuid>
```


|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header    |`From`|text| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Locate@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)
|           |`To`|text| [Host 🤗](<../../🤗 Host role/🤗🎭 Host role.md>)  | [`Locate@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)
|           | `Subject` | string    | `Hello@Host`
| Body    | `Chat`  | uuid      | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID 
|

<br/>
