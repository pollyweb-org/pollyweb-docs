# 💼🚀🤵  Status @ Broker


> Used in [💼⏩🧑‍🦰 Share Token @ Consumer](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>)

<br/> 

## Synchronous Request 🚀

```yaml
Header:
    From: any-consumer.com
    To: any-broker.com
    Subject: Status@Broker

Body:
    Issuer: any-issuer.com
    TokenID: <token-uuid>  
```


|Object|Property|Type|Description
|-|-|-|-
| Header| `From`| string | [Consumer 💼 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) name
| | `To`    | string | [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) name
| | `Subject`| string | `Status@Broker`
| Body | `Issuer` | string | [Issuer 🎴 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/40 🎴 Issuers/$ 🎴🎭 Issuer role.md>)
| | `TokenID`| string | [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/$ 🎫 Token.md>) ID on the Issuer
|
    

## Synchronous Response

```yaml
Status: SUSPENDED
Starting: 2025-10-10T13:45:00.000Z
Ending: 2025-12-31T00:00:00.000Z
Locator: .HOST,any-host.com,any-key
```

|Property|Type|Description
|-|-|-
| `Status`  | string | `ACTIVE` `SUSPENDED` `REVOKED` `EXPIRED`
| `Starting`| string | Optional date of start of status
| `Ending`  | string | Optional date of ending of status
| `Locator`| string | Optional [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) for a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) about it
|