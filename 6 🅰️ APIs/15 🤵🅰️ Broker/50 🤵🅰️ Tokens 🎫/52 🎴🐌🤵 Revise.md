<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfT9e264d13fa7b4030920efe49d -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L136 -->

# 🎴🐌🤵 Revise @ Broker

> Updates the status of a [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>).

> Used by:
> <br/>• [🎴⏩🧑‍🦰 Revise Token @ Issuer](<../../../5 ⏩ Flows/60 🎴⏩ Issuers/02 🎴⏩🧑‍🦰 Revise token.md>) flow
> <br/>• [💼⏩🧑‍🦰 Token Status @ Consumer](<../../../5 ⏩ Flows/20 💼⏩ Consumers/05 💼⏩🧑‍🦰 Token status.md>) flow

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-issuer.com
    To: any-broker.com
    Subject: Revoke@Broker
    
Body:
    ChatID: <session-uuid>
    TokenID: <token-uuid>
    Action: SUSPEND
    Starting: 2025-10-10T13:45:00.000Z
    Ending: 2025-12-31T00:00:00.000Z
    Locator: <reference-uuid>
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string|[Issuer 🎴 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
| |`To`|string|[Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
| |`Subject`|string|`Revoke@Broker`
|Body|`ChatID`|string|[Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID
| |`TokenID`|string|[Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID
| |`Action`| enum | `REVOKE` `SUSPEND` `ACTIVATE` `UPDATE`
| |`Starting`| timestamp | Start date and time
| |`Ending` | timestamp | Finish date and time (optional)
| |`Locator`| string | [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) for a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) about it.
|