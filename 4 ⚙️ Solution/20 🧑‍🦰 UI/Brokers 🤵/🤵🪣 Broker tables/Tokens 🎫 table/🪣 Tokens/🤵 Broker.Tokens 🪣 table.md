# 🤵🪣 Tokens @ Broker table

> Implementation
* Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Purpose
* Stores [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) issued by [Issuer 🎴 domains](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>).
* Mirrors the [`Issuer.Tokens` 🪣 table](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🪣 Issuer tables/Tokens 🎫 table/🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>) on [Issuer 🎴 domains](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>).

> Data access
* Read by [`Frontend@Broker`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>) 
* Written by [`Issue@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) [`Saved@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) [`Revise@Broker`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>)

<br/>

## Flows

|#|Flow ⏩|Purpose
|-|-|-
|1| [`Issue`](<../🪣🧱 10 Issue ⏩ flow/🤵 Broker.Tokens.Issue ⏩ flow.md>) | Receives and stores a new [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|2| [`Revise`](<../🪣🧱 70 Revise ⏩ flow/🤵 Broker.Tokens.Revise ⏩ flow.md>) | Changes the status of a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|3| [`Tag`](<../🪣🧱 50 Tag ⏩ flow/🤵 Broker.Tokens.Tag ⏩ flow.md>) | Adds a user tag a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) 
|4| [`Localize`](<../🪣🧱 30 Localize ⏩ flow/🤵 Broker.Tokens.Localize ⏩ flow.md>) | Changes the language of a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|5| [`Remove`](<../🪣🧱 60 Remove ⏩ flow/🤵 Broker.Tokens.Remove ⏩ flow.md>) | Removes an existing [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Tokens
Item: Token
Key: Issuer, Token
```
Note: The [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID is unique per [Issuer 🎴 domain](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name.

<br/>

Here's the [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) definition.

```yaml
Parents:

    Wallet: # Wallet that holds the Token
        Wallets.ID: Tokens.Wallet

    Issuer: # Domain that issued the Token
        Domains.Name: Tokens.Issuer
        Domains.Wallet: Tokens.Wallet

    Schema: # Definition of the Token
        Schemas.Code: Tokens.Schema
        Schemas.Wallet: Tokens.Wallet
```
References: [`Broker.Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Broker.Schemas`](<../../Schemas 🧩 table/🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>) [`Broker.Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)

<br/>

Here's the [Item 🛢 Propagate](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) definition.

```yaml
Propagate: 
    # Support for Frontend@Broker
    - Issuer    # Auto-populate the Domains table
    - Schema    # Auto-populate the Schemas table
```

<br/>

Here's the [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition.

```yaml
Handlers:

    OnTokenAltered: ALTERED     # Save Front@Notifier
    OnTokenIssued: ISSUED       # Call TRANSLATE
    OnTokenDetailed: DETAILED   # Call Prompt@Broker
    OnTokenOffered: OFFERED     # Call Save@Notifier
    OnTokenDeclined: DECLINED   # Call Offered@Issuer
    OnTokenSaved: SAVED         # Call Offered@Issuer
    OnTokenRemoved: REMOVED     # Call Removed@Issuer

    OnTokenLocalized:           # Call TRANSLATE
        Events: UPDATED
        Assert: New.Language

    OnTokenRevised:                     
        Events: UPDATED
        Assert: 
            AnyOf:
                - Old.Status
                - New.Status
                - Old.Starts
                - New.Starts
                - Old.Expires
                - New.Expires
```


Events 🪣 | Handler 🔔 |  Message 📨 | Save 💾
|-|-|-|-
`ALTERED` | [`OnTokenAltered`](<../🪣🧱 00 Altered 🔔 event/🤵 OnTokenAltered 🔔 handler.md>) | [`Updated@Notifier` 🅰️](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) 
`ISSUED`| [`OnTokenIssued`](<../🪣🧱 11 Issued 🔔 event/🤵 OnTokenIssued 🔔 handler.md>) | [`TRANSLATE` 🈯](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) | `DETAILED`
`DETAILED`| [`OnTokenDetailed`](<../🪣🧱 12 Detailed 🔔 event/🤵 OnTokenDetailed 🔔 handler.md>) | [`CONFIRM` 👍](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) | `OFFERED`
`OFFERED`| [`OnTokenOffered`](<../🪣🧱 13 Offered 🔔 event/🤵 OnTokenOffered 🔔 handler.md>) | [`Save@Notifier` 🅰️ ](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>) | 
`DECLINED` | [`OnTokenDeclined`](<../🪣🧱 14 Declined 🔔 event/🤵 OnTokenDeclined 🔔 handler.md>) | [`Offered@Issuer` 🅰️](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)  |
`SAVED` | [`OnTokenSaved`](<../🪣🧱 15 Saved 🔔 event/🤵 OnTokenSaved 🔔 handler.md>) | [`Offered@Issuer` 🅰️](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)  |
`REMOVED` | [`OnTokenRemoved`](<../🪣🧱 61 Removed 🔔 event/🤵 OnTokenRemoved 🔔 handler.md>) | [`Removed@Issuer` 🅰️](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Removed 🤵🐌🎴/🎴 Removed 🐌 msg.md>)  |
`UPDATED` | [`OnTokenLocalized`](<../🪣🧱 31 Localized 🔔 event/🤵 OnTokenLocalized 🔔 handler.md>) | [`TRANSLATE` 🈯](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) |
`UPDATED` | [`OnTokenRevised`](<../🪣🧱 71 Revised 🔔 event/🤵 OnTokenRevised 🔔 handler.md>) |   |
|

<br/>

Here's the [Item 🛢 Views](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Views.md>) definition.

```yaml
Views:

    FRONTEND: # Filter for Frontend@ 
        
        # From the Token lifecycle
        - .State.IsIn(ACTIVE, RESTORED)

    QUERY: # Filter for Query@ 

        # From the Token lifecycle
        - .State.IsIn(ACTIVE, RESTORED)

        # From Issue@Broker and Revise@Broker
        - Status.Is(ACTIVE) 
        - Starts.IsPast                 
        - Expires.IsEmpty.Or.IsFuture
```

Uses: [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>) [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.IsPast`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsPast ⓕ.md>) [`.IsEmpty`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsEmpty ⓕ.md>) [`.IsFuture`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>) [`.Or`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Or ⓕ.md>)


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

# From Saved@Broker
Path: /path/to/token

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
| `Path` |text| [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) path | [`Saved@`](<../../../🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) | [`Frontend@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
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