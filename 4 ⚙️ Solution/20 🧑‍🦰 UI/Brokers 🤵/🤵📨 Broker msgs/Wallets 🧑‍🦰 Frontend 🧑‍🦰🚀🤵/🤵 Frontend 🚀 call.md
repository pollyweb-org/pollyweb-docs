# 🧑‍🦰🚀🤵 Frontend @ Broker

 
> About
* The [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>) 
    * lists the [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>), [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>), and [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
    * of a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).
* Implements the [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>)
* Implemented by the [`Frontend` 📃 script](<🤵 Frontend 📃 handler.md>)

<br/>

## Synchronous Call 🚀
  
```yaml
Header: 
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Frontend@Broker

Body:

    # from Read@Helper
    Sets: Binds, Chats

    # from Read@Helper
    Outputs:        
        Binds: Title, Schema

    # from Read@Helper
    Asserts:          
        Binds:
            Vault: any-vault.dom
        Tokens:
            Status.IsIn: ACTIVE, REVOKED
```
Uses: [`.IsIn`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>)

<br/>

| Object | Property | Type  | Description|Origin
|-|-|-|-|-
| Header    |`From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|           |`To`|text| [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
|           | `Subject`|text|  `Frontend@Broker`
| Body    | `Sets`   | [enum](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Enum holders.md>)  | Set filters, like in [`Read@Helper`](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/👥🚀🤝 Read/🤝 Read 🚀 call.md>)
||||`Chats` `Binds` `Tokens` `Domains` `Schemas`
||`Outputs`| [map](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)  | Field filters, like in [`Read@Helper`](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/👥🚀🤝 Read/🤝 Read 🚀 call.md>)
||`Asserts`| [map](<../../../../37 Scripts 📃/📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)  | Item filters, like in [`Read@Helper`](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲📨 Helper msgs/👥🚀🤝 Read/🤝 Read 🚀 call.md>)
|

<br/>

## Response 


```yaml
Wallet: {...}   # Wallet properties
Chats: [...]    # Ordered list of Chats
Binds: [...]    # Ordered list of Binds
Tokens: [...]   # Ordered list of Tokens
Domains: {...}  # Indexed map of Domains
Schemas: {...}  # Indexed map of Schemas
```

| Property    |  Type  | Description | Origin | Changes
|-|-|-|-|-
| Wallet   | map | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) data | [`Onboard@`](<../Wallets 🧑‍🦰 Onboard 📣🚀🤵/🤵 Onboard 📃 handler.md>) | 
| Chats    | list   | [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) |  [`Opened@`](<../Chats 💬 Opened 🧑‍🦰🐌🤵/🤵 Opened 🐌 msg.md>) | [`Inform@`](<../Share 💼 Inform 💼🐌🤵/🤵 Inform 🐌 msg.md>)
| Binds    | list   | [Binds 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) | [`Bind@`](<../Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>) | 
| Tokens   | list   | [Tokens 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) | [`Issue@`](<../Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Revise@`](<../Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>)
| Domains  | map   | [Domains 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [`About@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 About/🕸 About 📃 handler.md>) |
| Schemas  | map   | [Schemas 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`Schema@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Schema/🕸 Schema 📃 handler.md>) |

<br/>

```yaml
Wallet:
    Language: en-US
```

| Object    | Property  | Type  | Description | 
|-|-|-|-
| Wallet   | `Language` | text | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) language code

<br/>

```yaml
Chats:
  <chat-uuid>:
    Chat: <chat-uuid>
    Host: any-host.dom
    Title: Any Form, at Any Vault
    Muted: false
    Blocked: false
```

| Object    | Property  | Type  | Description | 
|-|-|-|-
| Chats      | `Chat`        | uuid  | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | 
|           | `Host` |text| [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name
|           | `Muted`       | bool  | If muted
|           | `Blocked`     | bool  | If blocked

<br/>

```yaml
Binds:
  <bind-uuid>:
    Bind: <bind-uuid>
    Title: Any Schema, by Any Vault
    Schema: any-authority.dom/ANY-SCHEMA
    Vault: any-vault.dom
```

| Object    | Property  | Type  | Description | 
|-|-|-|-
| Binds      | `Bind`        | uuid  | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID | 
|           | `Title`       | text  | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) title
|           | `Schema`      | text  | [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|           | `Vault`       | text  | [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) name

<br/>

```yaml
Tokens:
  <token-uuid>:
    Token: <token-uuid>
    Title: Any Schema, by Any Issuer
    Status: ACTIVE
    Schema: any-authority.dom/ANY-SCHEMA
    Issuer: any-issuer.dom
```

| Object    | Property  | Type  | Description | 
|-|-|-|-
| Tokens     | `Token`       | uuid  | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID
|| `Title`       | text  | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) title
|| `Schema`      | text  | [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|| `Issuer`      | text  | [Issuer 🎴 domain](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name
|| `State`       | enum  | [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) state

<br/>

```yaml
Domains:
  any-domain.dom:
    Domain: any-domain.dom
    Title: Any Domain
    Description: bla, bla...
    Emoji: 👥
    SmallIcon: <base64>
    BigIcon: <base64>
```

| Object | Property  | Type  | Description 
|-|-|-|-
| Domains | `Domain`      | text  | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
|| `Title`       | text  | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) title
|| `Description` | text  | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) description
|| `Emoji`       | text  | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) emoji
|| `SmallIcon`   | base64| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) small icon
|| `BigIcon`     | base64| [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) big icon

<br/>

```yaml
Schemas:
  any-authority.dom/ANY-SCHEMA:
    Schema: any-authority.dom/ANY-SCHEMA
    Title: Any Schema
    Description: bla, bla...
    Emoji: 🧩
    SmallIcon: <base64>
    BigIcon: <base64>
```

| Object | Property  | Type  | Description | 
|-|-|-|-
| Schemas| `Schema`| text  | [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) 
||`Title`|text| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) title
||`Description`|text| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) description
||`Emoji`|text| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) emoji
||`SmallIcon`|base64| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) small icon
||`BigIcon`|base64| [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) big icon

---
<br/>
