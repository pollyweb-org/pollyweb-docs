<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfT7b35acc03fa342b9bc6e581e0 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L48 -->

# 🎴🐌🤵 Offer @ Broker

> An [Issuer 🎴 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) issues a [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) and asks a [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) to offer it to the user in a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).

> Used by the [🎴⏩🧑‍🦰 Offer Token @ Issuer](<../../../5 ⏩ Flows/60 🎴⏩ Issuers/01 🎴⏩🧑‍🦰 Offer token.md>) flow.

<br/>

## 🐌 Async Message

```yaml
Header:
    From: any-issuer.com
    To: any-broker.com
    Subject: Offer@Broker
  
Body:
    ChatID: <chat-uuid>
    TokenID: <token-uuid>
    Code: any-authority/ANY-CODE
    Version: 1.0.0
    Starts: 2018-12-10T13:45:00.000Z
    Expires: 2018-12-10T13:45:00.000Z
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Issuer 🎴 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/02 🎴🎭 Issuer role.md>) name
||`To`|string| [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
||`Subject`|string|`Offer@Broker`
|Body  |`ChatID` |uuid  | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) ID
| |`TokenID` |uuid  | [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) ID
|      |`Code`   |string| [Schema Code 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) 
|      |`Version`|string| Schema version|      
|      |`Starts` |timestamp| Valid from
|      |`Expires`|timestamp| Valid until
|

<br/>

## FAQ

1. **Why are the schema and timestamp properties for?**

    | Reason | Details
    |-|-
    |`Reject`| [Broker 🤵 domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) verify if the lifespan of the offered [Token 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) is worth showing to the user, rejecting [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) already expired or too far ahead in the future.
    `Translate` | [Broker 🤵 domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) need to translate the [Schema Code 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)  into for users in their [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) language.
    `Share`| When [Broker 🤵 domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) answer a [Query@Broker](<../60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) call, they need to filter only the active [Tokens 🎫](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 🎫 Tokens/01 🎫 Token.md>) of a certain [Schema Code 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)  within a version interval to be shared.
    |

    