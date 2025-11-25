# 🤵🪣 Tokens @ Broker table

> Implementation
* Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Purpose
* Stores [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)

> Data access
* Read by [`Frontend@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>) 
* Written by [`Issue@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) [`Saved@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) [`Revise@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Tokens.yaml

Prefix: Broker
Table: Tokens
Item: Token

# The Token UUID is unique per Issuer
Key: Issuer, Token

Parents:

    Wallet: # Wallet that holds the Token
        Wallets.ID: Tokens.Wallet

    Issuer: # Domain that issued the Token
        Domains.Name: Tokens.Issuer
        Domains.Wallet: Tokens.Wallet

    Schema: # Definition of the Token
        Schemas.Code: Tokens.Schema
        Schemas.Wallet: Tokens.Wallet

Propagate: 
    # Support for Frontend@Broker
    - Issuer    # Auto-populate the Domains table
    - Schema    # Auto-populate the Schemas table

Views:
    Active: # Filter for Frontend@ and Query@ 
        - .Now.IsBetween(Starts, Expires)
        - .State.IsIn(ACTIVE, RESTORED)
        - .Status.IsIn(ACTIVE)

Handlers:

    # Call Remove@Notifier
    OnTokenPurged: 
        Events: PURGED
    
    # Call Updated@Notifier
    OnTokenChanges: 
        Events: ALTERED

    # Call Offered@Issuer
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
|           | [`Domains` 🪣](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) | [domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)


## Handlers

[Handler 🔔](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) |  [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | Events
|-|-|-
| [`OnTokenPurged` 📃](<../🪣🔔 A Deleted/🤵 OnTokenDeleted 📃 handler.md>) | [`Remove@Notifier` 🅰️](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Remove 🤵🐌📣/📣 Remove 🐌 msg.md>) | `PURGED`
| [`OnTokenChanges` 📃](<../🪣🔔 0 Altered/🤵 OnTokenAltered 📃 handler.md>) | [`Updated@Notifier` 🅰️](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) | `ALTERED`
| [`OnTokenAccepted` 📃](<../🪣🔔 3 Offered/🤵 OnTokenOffered 📃 handler.md>) | [`Offered@Issuer` 🅰️](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>) | `UPDATED`

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.


```yaml
# Key from Issue@Broker
Issuer: any-issuer.dom
Token: <token-uuid>

# From Issue@Broker
Chat: <chat-uuid>
Wallet: <wallet-uuid>
Schema: any-authority.dom/ANY-SCHEMA:1.0
Starts: 2018-12-10T13:45:00.000Z
Expires: 2018-12-10T13:45:00.000Z

# From OnTokenOffered
Language: en-us
IssuerTitle: Any Issuer
SchemaTitle: Any Schema Title
Description: Any Schema description.
Title: Any Schema, by Any Issuer

# From Revise@Broker
Status: REVOKED

# From Pop@Broker
Tag: My Token
```


|Property|Type|Description | Origin | Purpose
|-|-|-|-|-
| `Wallet` | uuid | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) |  | [`Frontend@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
| `Token` | uuid | [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) | [`Issue@`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Offered@`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)
| `Issuer` |text| [Issuer 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)  | [`Issue@`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Offered@`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)
| `IssuerTitle` |text| [Issuer 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) Title | | [`Frontend@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
| `Schema` |text| [Schema Code 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`Issue@`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Query@`](<../../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Starts` | time | Valid from | [`Issue@`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Query@`](<../../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Expires` | time | Valid until | [`Issue@`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Query@`](<../../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Status`|text| `ACTIVE` <br/> `SUSPENDED` <br/> `REVOKED` | [`Revise@`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>) | [`Query@`](<../../../🤵🅰️ Broker methods/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Tag` |text| User alias | [`Pop@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | [`Frontend@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
| `Title`|text| [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) title | (multiple) | [`Frontend@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
||

## Title lifecycle

| Method | Action | Details
|-|-|-
| [`Saved@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Sets the initial translatable title
| [`Pop@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Translates when the language changes
| [`Pop@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Adds a non-translatable tag
|