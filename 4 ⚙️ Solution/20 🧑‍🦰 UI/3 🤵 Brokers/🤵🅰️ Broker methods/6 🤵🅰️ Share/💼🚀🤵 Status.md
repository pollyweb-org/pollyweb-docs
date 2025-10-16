# 💼🚀🤵  Status @ Broker


> Used in [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Prompts 🤔/👉💼 Share Token 🎫.md>)

<br/> 

## Synchronous Request 🚀

```yaml
Header:
    From: any-consumer.dom
    To: any-broker.dom
    Subject: Status@Broker

Body:
    Issuer: any-issuer.dom
    TokenID: <token-uuid>  
```


|Object|Property|Type|Description
|-|-|-|-
| Header| `From`| string | [Consumer 💼 domain](<../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) name
| | `To`    | string | [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) name
| | `Subject`| string | `Status@Broker`
| Body | `Issuer` | string | [Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>)
| | `TokenID`| string | [Token 🎫](<../../../../30 🧩 Data/3 🎫 Tokens/🎫 Token.md>) ID on the Issuer
|
    

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
| `Locator`| string | Optional [Locator 🔆](<../../../../25 🔆 Locators/1 🔆 Locators/🔆 Locator.md>) for a [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) about it
|