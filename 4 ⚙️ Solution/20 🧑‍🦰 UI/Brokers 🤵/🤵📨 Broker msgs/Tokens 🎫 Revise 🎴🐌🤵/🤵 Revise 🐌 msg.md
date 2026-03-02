# 🎴🐌🤵 Revise @ Broker

> Purpose

* Updates the status of a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>).

> Used by
* [🎴⏩🧑‍🦰 Revise Token @ Issuer](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴⏩ Issuer flows/Revise Token 🎴⏩🧑‍🦰/🎴 Revise Token ⏩ flow.md>) flow
* [💼⏩🧑‍🦰 Token Status @ Consumer](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Token Status 💼⏩🎫/💼 Token Status ⏩ flow.md>) flow

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-issuer.dom
    To: any-broker.dom
    Subject: Revise@Broker
    
Body:
    Token: <token-uuid>
    Status: SUSPENDED
    Starting: 2025-10-10T13:45:00.000Z
    Ending: 2025-12-31T00:00:00.000Z
    Locator: <reference-uuid>
```

|Object|Property|Type|Description|Origin
|-|-|-|-|-
|Header|`From`|text|[Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name | [`Issue@`](<../Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>)
| |`To`|text|[Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>) name
| |`Subject`|text|`Revise@Broker`
|Body|`Token`|text| Hook from [`Issue@Broker`](<../Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>)
| |`Status`| enum | `REVOKED` `SUSPENDED` `ACTIVE`
| |`Starting`| time | Start of status period
| |`Ending` | time | End of status period (optional)
| |`Locator`|text| [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) for a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) about it
|