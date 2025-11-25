<!-- Docs: https://quip.com/sN8DACFLN9wM#temp:C:AfT7b35acc03fa342b9bc6e581e0 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_TOKENS_TESTS.py#L48 -->

# 🎴🐌🤵 Issue @ Broker

> Flow
* Part of the [`Save Token` ⏩ flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>)
* Followed by the [`Save@Notifier` 🅰️ method](<../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>)

> Implementation
* Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* Implemented by the [`Offer` 📃 handler](<🤵 Issue 📃 handler.md>)

> Purpose
* An [Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) 
    * issues a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) 
    * and asks a [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * to offer it to the user in a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).


<br/>

## Async Message 🐌

```yaml
Header:
    From: any-issuer.dom
    To: any-broker.dom
    Subject: Issue@Broker
  
Body:
    Chat: <chat-uuid>
    Token: <token-uuid>
    Schema: any-authority.dom/ANY-SCHEMA:1.0
    Starts: 2018-12-10T13:45:00.000Z
    Expires: 2018-12-10T13:45:00.000Z
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|text| [Issuer 🎴](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) |[`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`To`|text| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
||`Subject`|text|`Issue@Broker`
|Body  |`Chat` |uuid  | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| |`Token` |uuid  | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) key || [`Issued@`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 call.md>) [`Accepted@`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>) [`Share@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Share 🤵🐌📣/📣 Share 🐌 msg.md>)
|      |`Schema`   |text| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)| |[`Query@Broker`](<../Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)     
|      |`Starts` |time| Valid from | | [`Query@Broker`](<../Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|      |`Expires`|time| Valid until| | [`Query@Broker`](<../Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
|

<br/>

## FAQ


1. **What are the `Schema` and `Times` properties for?**

    | Reason | Details
    |-|-
    |`Reject`| [Broker 🤵 domains](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) verify if the lifespan of the offered [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) is worth showing to the user, rejecting [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) already expired or too far ahead in the future.
    `Translate` | [Broker 🤵 domains](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) need to translate the [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)  into for users in their [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) language.
    `Share`| When [Broker 🤵 domains](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) answer a [Query@Broker](<../Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) call, they need to filter only the [Trusted 🫡](<../../../../30 🧩 Data/Trusts 🫡/🫡 Domain Trust.md>) and active [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) of a certain [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)  within a version interval to be shared.
    |

    