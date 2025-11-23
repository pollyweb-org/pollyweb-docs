# 🤵🪣 Tokens @ Broker table

> Implementation
* Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Purpose
* Stores [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)

> Data access
* Read by [`Frontend@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>) 
* Written by [`Offer@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) [`Saved@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) [`Revise@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Tokens.yaml

Prefix: Broker
Table: Tokens
Item: Token
Key: ID

Parents:
    Wallet: 
        Wallets.ID: Tokens.Wallet
    Issuer: 
        Domains.Name: Tokens.Issuer
        Domains.Wallet: Tokens.Wallet

Propagate:
    - Issuer

Views:
    Offered: 
        - .State: OFFERED
    Active: 
        - .Now.IsBetween(Starts, Expires)
        - .State: ACTIVE

Handlers:

    # Call Remove@Notifier
    OnTokenPurged: 
        Events: PURGED
    
    # Call Updated@Notifier
    OnTokenChanges: 
        Events: ALTERED

    # Call Accepted@Issuer
    OnTokenAccepted: 
        Events: UPDATED
        Assert: 
            New.State: ACTIVE
            Old.State: OFFERED
```

Uses: [`.Now`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>) [`.IsBetween`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsBetween ⓕ.md>) 


## Links

| Link | Table | Stores
|-|-|-
| Parent    | [`Wallets` 🪣](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) | [Wallets 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) |
|           | [`Domains` 🪣](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domain 🪣 table.md>) | [domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)


## Handlers

[Handler 🔔](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) |  [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Events
|-|-|-
| [`OnTokenPurged` 📃](<../🪣🔔 9 Deleted/🤵 OnTokenDeleted 📃 handler.md>) | [`Remove@Notifier` 🅰️](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>) | `PURGED`
| [`OnTokenChanges` 📃](<../🪣🔔 0 Altered/🤵 OnTokenAltered 📃 handler.md>) | [`Updated@Notifier` 🅰️](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) | `ALTERED`
| [`OnTokenAccepted` 📃](<../🪣🔔 4 Accepted/🤵 OnTokenAccepted 📃 handler.md>) | [`Accepted@Issuer` 🅰️](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>) | `UPDATED`

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.


```yaml
# READ|Tokens|<token-uuid>

# From Offer@Broker
Hook: <hook-uuid>
ID: <token-uuid>
Wallet: <wallet-uuid>
Issuer: any-issuer.dom
Issuer$: Any Issuer
Schema: any-authority.dom/ANY-SCHEMA:1.0
Schema$: Any Schema Title
Key: token-1234
Starts: 2018-12-10T13:45:00.000Z
Expires: 2018-12-10T13:45:00.000Z

# From Revise@Broker
Status: REVOKED

# From Pop@Broker
Tag: My Token

# From multiple 
Title: My Token
```


|Property|Type|Description | Origin | Purpose
|-|-|-|-|-
| `Hook` | uuid | [Issuer 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) hook | [`Offer@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) | [`Accepted@Issuer`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>)
| `ID`| uuid |  [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) | [`Offer` 📃 handler](<../../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 📃 handler.md>) | [`Pop@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>)
| `Wallet` | uuid | [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) | [`Offer` 📃 handler](<../../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 📃 handler.md>) | [`Frontend@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
| `Issuer` |text| [Issuer 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)  | [`Offer@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) | [`Accepted@Issuer`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Accepted 🤵🐌🎴/🎴 Accepted 🐌 msg.md>)
| `Issuer$` |text| [Issuer 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) Title | [`Translate@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate/🕸 Translate 🚀 call.md>) | [`Frontend@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
| `Key` |text| [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) Key |  [`Offer@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) | [`Receive@Consumer`](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)
| `Schema` |text| [Schema Code 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`Offer@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) | [`Query@Broker`](<../../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Starts` | time | Valid from | [`Offer@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) | [`Query@Broker`](<../../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Expires` | time | Valid until | [`Offer@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Offer 🎴🐌🤵/🤵 Offer 🐌 msg.md>) | [`Query@Broker`](<../../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Status`|text| `OFFERED` <br/> `ACTIVE` <br/> `SUSPENDED` <br/> `REVOKED` | [`Revise@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>) | [`Query@Broker`](<../../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Tag` |text| User alias | [`Pop@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | [`Frontend@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
| `Title`|text| [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) title | (multiple) | [`Frontend@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
||

## Title lifecycle

| Method | Action | Details
|-|-|-
| [`Saved@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Sets the initial translatable title
| [`Pop@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Translates the title
| [`Pop@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Adds a non-translatable tag
|