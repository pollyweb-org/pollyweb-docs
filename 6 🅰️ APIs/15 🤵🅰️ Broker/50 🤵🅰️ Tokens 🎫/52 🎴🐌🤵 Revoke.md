<!-- #TODO -->

<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfT9e264d13fa7b4030920efe49d -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L136 -->

# 🎴🐌🤵 Revoke @ Broker

> Used by [🎴⏩🧑‍🦰 Revoke token](<../../../5 ⏩ Flows/06 🎴⏩ Issuers/02 🎴⏩🧑‍🦰 Revoke token.md>)

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
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string|[Issuer 🎴 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
| |`To`|string|[Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
| |`Subject`|string|`Revoke@Broker`
|Body|`ChatID`|string|[Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
| |`TokenID`|string|[Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID
|