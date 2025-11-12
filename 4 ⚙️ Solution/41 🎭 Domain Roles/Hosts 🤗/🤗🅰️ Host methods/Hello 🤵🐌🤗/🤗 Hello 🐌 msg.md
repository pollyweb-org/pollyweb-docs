<!-- https://quip.com/s9oCAO3UR38A#temp:C:TDDf29b75b2d0214f9a87224b338 -->

# 🤵🐌🤗 Hello @ Host

> Implementation

* Implemented by the [`Hello` 📃 handler](<🤗 Hello 📃 handler.md>)

> Purpose
* Starts a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with a [Host 🤗 domain](<../../🤗 Host role/🤗🎭 Host role.md>).

> Used by
* [🧑‍🦰👉🤗 Scan host QR @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap host locator 🔆🤗 /🧑‍🦰 Tap host locator ⏩ flow.md>)
* [🧑‍🦰👉🤗 Scan printer QR @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap alias locator 🔆🖨️ /🧑‍🦰 Tap alias locator ⏩ flow.md>)

<br/> 

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
| Header    |`From`|domain| [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Assess@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)
|           |`To`|domain| [Host 🤗](<../../🤗 Host role/🤗🎭 Host role.md>)  | [`Assess@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)
|           | `Subject` | string    | `Hello@Host`
| Body    | `Chat`  | uuid      | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID 
|

<br/>
