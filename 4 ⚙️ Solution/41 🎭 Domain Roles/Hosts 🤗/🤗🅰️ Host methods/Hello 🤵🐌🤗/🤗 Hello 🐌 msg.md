<!-- https://quip.com/s9oCAO3UR38A#temp:C:TDDf29b75b2d0214f9a87224b338 -->

# 🤵🐌🤗 Hello @ Host

> Implementation

* Implemented by the [`Hello` 📃 handler](<🤗 Hello 📃 handler.md>)

> Purpose
* Starts a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) with a [Host 🤗 domain](<../../🤗🎭 Host role.md>).

> Used by
* [🧑‍🦰👉🤗 Scan host QR @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap host locator 🔆🤗 /🧑‍🦰 Tap host locator ⏩ flow.md>)
* [🧑‍🦰👉🤗 Scan printer QR @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/Tap alias locator 🔆🖨️ /🔆🖨️ Tap alias locator ⏩ flow.md>)

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


|Object|Property|Type|Description
|-|-|-|-
| Header    | `From`    | string    | [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) name
|           | `To`      | string    | [Host 🤗 domain](<../../🤗🎭 Host role.md>) name
|           | `Subject` | string    | `Hello@Host`
| Body           | `Binds`   | uuid[] | List of [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) for a [Vault 🗄️](<../../../Vaults 🗄️/🗄️🎭 Vault role.md>) host
|| `Chat`  | uuid      | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID in the [Broker 🤵 domain](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>)
|      | `Language`| enum    | ISO language code
|           | `Locator` | string    | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) in the [Host 🤗 domain](<../../🤗🎭 Host role.md>)
|| `Parameters`| object | Custom parameters
|           | `PublicKey`| string | For [`Prompted@`](<../Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) [`Reply@`](<../Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>) [`Download@`](<../Download 🧑‍🦰🚀🤗/🤗 Download 🚀 request.md>)
|           | `Schema`    | string    | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) of the Locator
|           | `Tokens`  | uuid[] | List of [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) for an [Issuer 🎴](<../../../Issuers 🎴/🎴🎭 Issuer role.md>) host
|

<br/>
