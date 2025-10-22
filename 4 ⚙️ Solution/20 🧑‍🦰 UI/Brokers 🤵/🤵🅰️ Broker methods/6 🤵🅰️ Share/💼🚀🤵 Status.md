# 💼🚀🤵  Status @ Broker


> Used in [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Token 🎫.md>)

<br/> 

## Synchronous Request 🚀

```yaml
Header:
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Status@Broker

Body:
    Token: <token-uuid>  
```


|Object|Property|Type|Description
|-|-|-|-
| Header| `From`| string | [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) name
| | `To`    | string | [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) name
| | `Subject`| string | `Status@Broker`
| Body | `Token`| uuid | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) from [`Receive@Consumer`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/🧑‍🦰🐌💼 Receive.md>)
|
    
<br/>


## Synchronous Response

```yaml
Status: SUSPENDED
Starting: 2025-10-10T13:45:00.000Z
Ending: 2025-12-31T00:00:00.000Z
Locator: .HOST,any-host.dom,any-key
```

|Property|Type|Description
|-|-|-
| `Status`  | string | `ACTIVE` `SUSPENDED` `REVOKED` `EXPIRED`
| `Starting`| string | Optional date of start of status
| `Ending`  | string | Optional date of ending of status
| `Locator`| string | Optional [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) for a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) about it
|

<br/>

## Handler

```yaml
# Verify the Consumer message
- VERIFY|$.Msg

# Get the Token
- GET >> $token:
    Set: Tokens@Broker
    Key: $.Msg.Token

# Return the Status
- REEL:
    Status: $token.Status
    Starting: $token.Starting
    Ending: $token.Ending
    Locator: $token.Locator
```