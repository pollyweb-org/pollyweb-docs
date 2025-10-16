<!-- https://quip.com/s9oCAO3UR38A#temp:C:TDDf29b75b2d0214f9a87224b338 -->

# 🤵🐌🤗 Hello @ Host

> Starts a [Chat 💬](<../../../35 Chats/12 💬 Chats/💬 Chat.md>) with a [Host 🤗 domain](<../🤗🎭 Host role.md>).

> Used by:
> <br/>• [🧑‍🦰👉🤗 Scan host QR @ Wallet](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/01 🧑‍🦰👉🤗 Scan host QR.md>)
> <br/>• [🧑‍🦰👉🤗 Scan printer QR @ Wallet](<../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/15 👉🔆 Locators/02 🧑‍🦰👉🤗 Scan printer QR.md>)

<br/> 

## Async Message 🐌


```yaml
Header:
    From: any-broker.com
    To: any-host.com
    Subject: Hello@Host

Body:
    Language: en-us
    ChatID: <chat-uuid>
    PublicKey: <public-key>
    Code: nlweb.org/THING
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
| Header    | `From`    | string    | [Broker 🤵 domain](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>) name
|           | `To`      | string    | [Host 🤗 domain](<../🤗🎭 Host role.md>) name
|           | `Subject` | string    | `Hello@Host`
| Body      | `Language`| enum    | ISO language code
|           | `ChatID`  | uuid      | [Chat 💬](<../../../35 Chats/12 💬 Chats/💬 Chat.md>) ID in the [Broker 🤵 domain](<../../../45 🤲 Helper domains/24 🤵 Brokers/🤵🤲 Broker helper.md>)
|           | `PublicKey`| string | For [`Prompted@`](<🧑‍🦰🚀🤗 Prompted.md>) [`Reply@`](<🧑‍🦰🐌🤗 Reply.md>) [`Download@`](<🧑‍🦰🚀🤗 Download.md>)
|           | `Locator` | string    | [Locator 🔆](<../../../25 Locators/15 🔆 Locators/🔆 Locator.md>) in the [Host 🤗 domain](<../🤗🎭 Host role.md>)
|           | `Code`    | string    | [Schema Code 🧩](<../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) of the Locator
|           | `Binds`   | uuid[] | List of [Binds 🔗](<../../../30 Data/20 🔗 Binds/🔗 Bind.md>) for a [Vault 🗄️](<../../80 🗄️ Vaults/🗄️🎭 Vault role.md>) host
|           | `Tokens`  | uuid[] | List of [Tokens 🎫](<../../../30 Data/30 🎫 Tokens/🎫 Token.md>) for an [Issuer 🎴](<../../40 🎴 Issuers/🎴🎭 Issuer role.md>) host
|| `Parameters`| object | Custom parameters
|
