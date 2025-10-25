<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfT7b35acc03fa342b9bc6e581e0 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L48 -->

# 🎴🐌🤵 Offer @ Broker

> Part of the [`Save Token` 👉 flow](<../../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉🎴 Save token.md>).

> Implemented by the [`Offer` 📃 script](<🤵📃 Offer 🎫 handler.md>)

> Purpose: 
* An [Issuer 🎴 domain](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) 
    * issues a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) 
    * and asks a [Broker 🤵 domain](<../../../🤵🤲 Broker helper.md>) 
    * to offer it to the user in a [Chat 💬](<../../../../../35 💬 Chats/💬 Chats/💬 Chat.md>).


<br/>

## Async Message 🐌

```yaml
Header:
    From: any-issuer.dom
    To: any-broker.dom
    Subject: Offer@Broker
  
Body:
    Chat: <chat-uuid>
    Hook: <hook-uuid>
    Schema: any-authority.dom/ANY-SCHEMA:1.0
    Starts: 2018-12-10T13:45:00.000Z
    Expires: 2018-12-10T13:45:00.000Z
```

|Object|Property|Type|Description
|-|-|-|-
|Header|`From`|string | [Issuer 🎴 domain](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🎭 Issuer role.md>) name
||`To`|string| [Broker 🤵 domain](<../../../🤵🤲 Broker helper.md>) name
||`Subject`|string|`Offer@Broker`
|Body  |`Chat` |uuid  | [Chat 💬](<../../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
| |`Hook` |uuid  | Hook for [`Issued@`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🧑‍🦰🚀🎴 Issued.md>) [`Accepted@`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/🤵🐌🎴 Accepted.md>)
|      |`Schema`   |string| [Schema 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) of the [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>)     
|      |`Starts` |timestamp| [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) valid from
|      |`Expires`|timestamp| [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) valid until
|

<br/>

## FAQ

1. **Why are the schema and timestamp properties for?**

    | Reason | Details
    |-|-
    |`Reject`| [Broker 🤵 domains](<../../../🤵🤲 Broker helper.md>) verify if the lifespan of the offered [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) is worth showing to the user, rejecting [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) already expired or too far ahead in the future.
    `Translate` | [Broker 🤵 domains](<../../../🤵🤲 Broker helper.md>) need to translate the [Schema 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)  into for users in their [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) language.
    `Share`| When [Broker 🤵 domains](<../../../🤵🤲 Broker helper.md>) answer a [Query@Broker](<../../6 ...for Share 💼/💼🐌🤵 Query.md>) call, they need to filter only the active [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token.md>) of a certain [Schema 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)  within a version interval to be shared.
    |

    