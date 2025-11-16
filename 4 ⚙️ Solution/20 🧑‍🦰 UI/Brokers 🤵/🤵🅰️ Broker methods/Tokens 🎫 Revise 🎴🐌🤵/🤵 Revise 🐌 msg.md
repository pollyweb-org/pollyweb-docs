<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfT9e264d13fa7b4030920efe49d -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L136 -->

<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

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
    Subject: Revoke@Broker
    
Body:
    Chat: <session-uuid>
    Token: <token-uuid>
    Action: SUSPEND
    Starting: 2025-10-10T13:45:00.000Z
    Ending: 2025-12-31T00:00:00.000Z
    Locator: <reference-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|text|[Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name
| |`To`|text|[Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) name
| |`Subject`|text|`Revoke@Broker`
|Body|`Chat`|text|[Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID
| |`Token`|text|[Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID
| |`Action`| enum | `REVOKE` `SUSPEND` `ACTIVATE` `UPDATE`
| |`Starting`| timestamp | Start date and time
| |`Ending` | timestamp | Finish date and time (optional)
| |`Locator`|text| [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) for a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) about it.
|