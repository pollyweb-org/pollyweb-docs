<!-- Docs: https://quip.com/HrgkAuQCqBez#temp:C:bXD09ae7595fe4943d5985d83fd0 -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L10 -->


# 🧑‍🦰🚀🤵 Frontend 🧑‍🦰🚀🤵 @ Broker

> Implementation 
* Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* Implemented by the [`Frontend` 📃 script](<🤵 Frontend 📃 handler.md>)
  
> Purpose
* The [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * lists the [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>), [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>), and [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
    * of a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).

<br/>

## Synchronous Call 🚀
  
```yaml
Header: 
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Frontend@Broker

Body:
    Chats: [Field1, Field2, ...]
    Binds: [Field1, Field2, ...]
    Tokens: [Field1, Field2, ...]
    Domains: [Field1, Field2, ...]
```

| Object | Property | Type  | Description|Origin
|-|-|-|-|-
| Header    |`From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|           |`To`|text| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|           | `Subject`|text|  `Frontend@Broker`
| Body    | `Chats`   |list  | Optional [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) fields to list
|        | `Binds`   |list  | Optional [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) fields to list
|        | `Tokens`  |list  | Optional [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) fields to list
|        | `Domains` |list  | Optional [Domain 🌐](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) fields to list

<br/>

## Response 


```yaml
Wallet:
    Language: en-US

Chats:
    <chat-uuid>:
        Chat: <chat-uuid>
        Host: any-host.dom
        Muted: false
        Blocked: false

Binds:
    <bind-uuid>:
        Bind: <bind-uuid>
        Title: Any Schema, by Any Vault
        Schema: any-authority.dom/ANY-SCHEMA
        Vault: any-vault.dom

Tokens:
    <token-uuid>:
        Token: <token-uuid>
        Title: Any Schema, by Any Issuer
        Schema: any-authority.dom/ANY-SCHEMA
        Issuer: any-issuer.dom
        State: ACTIVE

Domains:
    any-domain.dom:
        Domain: any-domain.dom:
        Title: Any Domain
        Description: bla, bla...
        SmallIcon: <base64>
        BigIcon: <base64>

Schemas:
    any-authority.dom/ANY-SCHEMA:
        Schema: any-authority.dom/ANY-SCHEMA
        Title: Any Schema
        Description: bla, bla...
```

| Object    | Property  | Type  | Description | 
|-|-|-|-
| Wallet   | `Language` | text | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) language code
| Chats      | `Chat`        | uuid  | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | 
|           | `Host` |text| [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name
|           | `Muted`       | bool  | If muted
|           | `Blocked`     | bool  | If blocked
| Binds      | `Bind`        | uuid  | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID | 
|           | `Title`       | text  | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) title
|           | `Schema`      | text  | [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|           | `Vault`       | text  | [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) name
| Tokens     | `Token`       | uuid  | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID
|       | `Title`       | text  | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) title
|       | `Schema`      | text  | [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|       | `Issuer`      | text  | [Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name
|       | `State`       | enum  | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) state
| Domains    | `Domain`      | text  | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
|       | `Title`       | text  | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) title
|       | `Description` | text  | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) description
|       | `SmallIcon`   | base64| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) small icon
|       | `BigIcon`     | base64| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) big icon
| Schemas    | `Schema`      | text  | [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) 
|       | `Title`       | text  | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) title
|       | `Description` | text  | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) description
|

<br/>
