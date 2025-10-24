<!-- https://quip.com/s9oCAO3UR38A#temp:C:TDDf29b75b2d0214f9a87224b338 -->

# 🤵🐌🤗 Hello @ Host

> Purpose
* Starts a [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) with a [Host 🤗 domain](<../🤗🎭 Host role.md>).

> Used by
* [🧑‍🦰👉🤗 Scan host QR @ Wallet](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/🔆🤗 Tap host locator.md>)
* [🧑‍🦰👉🤗 Scan printer QR @ Wallet](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in App 🏠/🔆🖨️ Tap alias locator.md>)

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
| Header    | `From`    | string    | [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>) name
|           | `To`      | string    | [Host 🤗 domain](<../🤗🎭 Host role.md>) name
|           | `Subject` | string    | `Hello@Host`
| Body           | `Binds`   | uuid[] | List of [Binds 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) for a [Vault 🗄️](<../../Vaults 🗄️/🗄️🎭 Vault role.md>) host
|| `Chat`  | uuid      | [Chat 💬](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID in the [Broker 🤵 domain](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🤲 Broker helper.md>)
|      | `Language`| enum    | ISO language code
|           | `Locator` | string    | [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) in the [Host 🤗 domain](<../🤗🎭 Host role.md>)
|| `Parameters`| object | Custom parameters
|           | `PublicKey`| string | For [`Prompted@`](<🧑‍🦰🚀🤗 Prompted.md>) [`Reply@`](<🧑‍🦰🐌🤗 Reply.md>) [`Download@`](<🧑‍🦰🚀🤗 Download.md>)
|           | `Schema`    | string    | [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) of the Locator
|           | `Tokens`  | uuid[] | List of [Tokens 🎫](<../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) for an [Issuer 🎴](<../../Issuers 🎴/🎴🎭 Issuer role.md>) host
|

<br/>

## Handler

```yaml
# Check if the Broker is trustworthy
- TRUSTS: $.Msg.From
    Schema: .HOST/HELLO

# Save the data
- SAVE|Chats@Host:
    Broker: $.Msg.From
    
    # It's safe to save the Body, 
    #   it's already schema-validated.
    :$.Msg.Body:  

# Start a Chat for the locator
- TALK|$.Msg.Chat|$.Msg.Locator
```

| [Command ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| 💾 [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...items/SAVE 💾 item.md>) | Save the [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) into the [Chats 🪣 table](<../🤗🪣 Host tables/🤗🪣 Chats 💬.md>)
| 😃 [`TALK`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control/TALK 😃.md>) | Start a [Talker 😃](<../../../35 💬 Chats/😃 Talkers/😃 Talker role.md>)
| 🫡 [`TRUSTS`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages/TRUSTS 🫡.md>) | Assert a [Trust 🫡](<../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) on 
|