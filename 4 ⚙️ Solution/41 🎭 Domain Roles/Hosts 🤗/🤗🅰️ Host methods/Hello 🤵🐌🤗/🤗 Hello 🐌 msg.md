<!-- https://quip.com/s9oCAO3UR38A#temp:C:TDDf29b75b2d0214f9a87224b338 -->

# 🤵🐌🤗 Hello @ Host

> Implementation

* Implemented by the [`Hello` 📃 handler](<🤗 Hello 📃 handler.md>)

> Purpose
* Starts a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) with a [Host 🤗 domain](<../../🤗🎭 Host role.md>).

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
    Language: en-us
    Chat: <chat-uuid>
    PublicKey: <public-key>
    Schema: nlweb.dom/THING
    Locator: MY-THING-ID
    Binds: 
        - <bind-#1-uuid>
        - <bind-#2-uuid>
    Tokens:
        - <token-#1-uuid>
        - <token-#2-uuid>
    Parameters: 
        Param1: Value1
        Param2: Value2
```


|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
| Header    | `From`    | string    | [Broker 🤵](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) | [`Assess@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)
|           | `To`      | string    | [Host 🤗](<../../🤗🎭 Host role.md>)  | [`Assess@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)
|           | `Subject` | string    | `Hello@Host`
| Body           | `Binds`   | uuid[] | [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) of a [Vault 🗄️](<../../../Vaults 🗄️/🗄️🎭 Vault role.md>) host | [`Bound@`](<../../../Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|| `Chat`  | uuid      | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID 
|      | `Language`| enum    | ISO language code | [`Language@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Language 🧑‍🦰🐌🤵/🤵 Language 🐌 msg.md>)
|           | `Locator` | string    | [Host 🤗](<../../🤗🎭 Host role.md>) [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) | [`Assess@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>) | 
|| `Parameters`| object | Custom parameters | [`Assess@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)
|           | `PublicKey`| string | For signing || [`Prompted@`](<../Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>)<br/>[`Reply@`](<../Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>) <br/>[`Download@`](<../Download 🧑‍🦰🚀🤗/🤗 Download 🚀 request.md>)
|           | `Schema`    | string    | Locator  [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`Assess@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)
|           | `Tokens`  | uuid[] |  [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) of a [Issuer 🎴](<../../../Issuers 🎴/🎴🎭 Issuer role.md>) host | [`Offer@`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>)
|

<br/>
