# 🤵🪣 Tokens @ Broker table

> About
* Implements the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>)
* Stores [Tokens 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) issued by [Issuer 🎴 domains](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)
* Mirrors the [`Issuer.Tokens` 🪣 table](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🪣 Issuer tables/Tokens 🎫 table/🪣 Tokens/🎴 Issuer.Tokens 🪣 table.md>) on [Issuer 🎴 domains](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)

<br/>

## Data access

|Flow ⏩|[Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)|[`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)|[`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)||
|-|-|:-:|:-:|-|
|[`Issue`](<../🪣🧱 10 Issue ⏩ flow/🤵 Broker.Tokens.Issue ⏩ flow.md>)|[`Issue@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 📃 handler.md>) | | X
||[`Saved@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 📃 handler.md>) | X | X
||[`Revise@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 📃 handler.md>) | X |X
|

<br/>

## Flows

|#|Flow ⏩|Purpose
|-|-|-
|1| [`Issue`](<../🪣🧱 10 Issue ⏩ flow/🤵 Broker.Tokens.Issue ⏩ flow.md>) | Receives and stores a new [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|2| [`Revise`](<../🪣🧱 50 Revise ⏩ flow/🤵 Broker.Tokens.Revise ⏩ flow.md>) | Changes the status of a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|3| [`Tag`](<../🪣🧱 30 Tag ⏩ flow/🤵 Broker.Tokens.Tag ⏩ flow.md>) | Adds a user tag a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) 
|4| [`Localize`](<../🪣🧱 20 Localize ⏩ flow/🤵 Broker.Tokens.Localize ⏩ flow.md>) | Changes the language of a [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)
|5| [`Remove`](<../🪣🧱 40 Remove ⏩ flow/🤵 Broker.Tokens.Remove ⏩ flow.md>) | Removes an existing [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>)

<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>). 

```yaml
Prefix: Broker
Table: Tokens
Item: Token
Key: Issuer, Token
```

> The [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) ID is unique per [Issuer 🎴 domain](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) name.


<br/>

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Domains`](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Schemas`](<../../Schemas 🧩 table/🪣 Schemas/🤵 Broker.Schemas 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>)

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

<br/>

Here's the [Item 🛢 Propagate](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Propagate.md>) definition.

```yaml
Propagate: 
    # Support for Frontend@Broker
    - Issuer    # Auto-populate the Domains table
    - Schema    # Auto-populate the Schemas table
```

<br/>

The [Item 🛢 Children](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Children.md>) are: [`Broker.Queries`](<../../Queries 💼 table/🪣 Queries/🤵 Broker.Queries 🪣 table.md>) 

```yaml
Children:
    Queries: # Queries that reference this Token
        Query.Token: Token.Wallet
        Query.Issuer: Token.Issuer
```

<br/>

The [Item 🛢 Distincts](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Distincts.md>) are the following.

```yaml
Distincts:
    Consumers: Queries.Consumer
```

<br/>

Here's the [Item 🛢 Handlers](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) definition.

```yaml
Handlers:

    # Updates@Notifier
    ALTERED  >> OnTokenAltered:   # Save Broker.Frontend

    # Issue flow
    ISSUED   >> OnTokenIssued:    # Call TRANSLATE
    DETAILED >> OnTokenDetailed:  # Call Prompt@Broker
    OFFERED  >> OnTokenOffered:   # Call Save@Notifier
    DECLINED >> OnTokenDeclined:  # Call Offered@Issuer
    SAVED    >> OnTokenSaved:     # Call Offered@Issuer

    # Localize flow
    UPDATED  >> OnTokenLocalized: # Call TRANSLATE
        Assert: New.Language

    # Remove flow
    REMOVED  >> OnTokenRemoved:   # Call Removed@Issuer
   
    # Revise flow
    UPDATED  >> OnTokenRevised:  
        Assert: 
            AnyOf:
                - Old.Status
                - New.Status
                - Old.Starts
                - New.Starts
                - Old.Expires
                - New.Expires
```


Flow ⏩ | Events 🪣 | Handler 🔔 |  Message 📨 | Save 💾
|-|-|-|-|-
||`ALTERED` | [`OnTokenAltered`](<../🪣🧱 00 Altered 🔔 event/🤵 OnTokenAltered 🔔 handler.md>) | [`Updated@Notifier` 🅰️](<../../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>) 
|[`Issue`](<../🪣🧱 10 Issue ⏩ flow/🤵 Broker.Tokens.Issue ⏩ flow.md>)|`ISSUED`| [`OnTokenIssued`](<../🪣🧱 11 Issued 🔔 event/🤵 OnTokenIssued 🔔 handler.md>) | [`TRANSLATE` 🈯](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) | `DETAILED`
||`DETAILED`| [`OnTokenDetailed`](<../🪣🧱 12 Detailed 🔔 event/🤵 OnTokenDetailed 🔔 handler.md>) | [`CONFIRM` 👍](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) | `OFFERED`
||`OFFERED`| [`OnTokenOffered`](<../🪣🧱 13 Offered 🔔 event/🤵 OnTokenOffered 🔔 handler.md>) | [`Save@Notifier` 🅰️ ](<../../../../Notifiers 📣/📣📨 Notifier msgs/Tokens 🎫 Save 🤵🐌📣/📣 Save 🐌 msg.md>) | 
||`DECLINED` | [`OnTokenDeclined`](<../🪣🧱 14 Declined 🔔 event/🤵 OnTokenDeclined 🔔 handler.md>) | [`Offered@Issuer` 🅰️](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)  |
||`SAVED` | [`OnTokenSaved`](<../🪣🧱 15 Saved 🔔 event/🤵 OnTokenSaved 🔔 handler.md>) | [`Offered@Issuer` 🅰️](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)  |
|[`Remove`](<../🪣🧱 40 Remove ⏩ flow/🤵 Broker.Tokens.Remove ⏩ flow.md>)|`REMOVED` | [`OnTokenRemoved`](<../🪣🧱 41 Removed 🔔 event/🤵 OnTokenRemoved 🔔 handler.md>) | [`Removed@Issuer` 🅰️](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Removed 🤵🐌🎴/🎴 Removed 🐌 msg.md>)  |
|[`Localize`](<../🪣🧱 21 Localized 🔔 event/🤵 OnTokenLocalized 🔔 handler.md>)|`UPDATED` | [`OnTokenLocalized`](<../🪣🧱 21 Localized 🔔 event/🤵 OnTokenLocalized 🔔 handler.md>) | [`TRANSLATE` 🈯](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>) |
|[`Revise`](<../🪣🧱 50 Revise ⏩ flow/🤵 Broker.Tokens.Revise ⏩ flow.md>)|`UPDATED` | [`OnTokenRevised`](<../🪣🧱 51 Revised 🔔 event/🤵 OnTokenRevised 🔔 handler.md>) |   |
|

<br/>

Here's the [Item 🛢 Views](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Views.md>) definition.

```yaml
Views:

    FRONTEND: # Filter for Frontend@ 
        
        # From the Token lifecycle
        .State.IsIn: ACTIVE, RESTORED

    QUERY: # Filter for Query@ 

        # From the Token lifecycle
        .State.IsIn: ACTIVE, RESTORED

        # From Issue@Broker and Revise@Broker
        Status.Is: ACTIVE
        Starts.IsPast:
        Expires.IsEmpty.Or.IsFuture:
```

Uses: [`.Is`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>) [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.IsPast`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsPast ⓕ.md>) [`.IsEmpty`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsEmpty ⓕ.md>) [`.IsFuture`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsFuture ⓕ.md>) [`.Or`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Or ⓕ.md>)


<br/>

Here's the [Item 🛢 Assert](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Assert.md>) definition.

```yaml
Assert:
    AllOf: Token, Issuer, Status, Starts, Chat, Wallet, Schema
    UUIDs: Token, Chat, Wallet
    Texts: Locator, Schema, Tag
    Times: Starts, Expires
    Issuer.IsDomain:
    Status.IsIn: REVOKED, SUSPENDED, ACTIVE
    Expires.IsAfter: Starts
    Schema.IsSchema: 
    Language.IsLanguage:
```
Uses: [`.IsDomain`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.IsAfter`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsAfter ⓕ.md>) [`.IsLanguage`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsLanguage ⓕ.md>) [`.IsSchema`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>)


<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

Key from [`Issue@Broker` 🐌 handler](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 📃 handler.md>)

```yaml
Issuer: any-issuer.dom
Token: <token-uuid>
```

From [`Issue@Broker` 🐌 handler](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 📃 handler.md>)

```yaml
Chat: <chat-uuid>
Wallet: <wallet-uuid>
Schema: any-authority.dom/ANY-SCHEMA:1.0
```

From [`Issue@Broker` 🐌 handler](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 📃 handler.md>) and [`Revise@Broker` 🐌 handler](<../../../🤵📨 Broker msgs/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 📃 handler.md>)

```yaml
Status: REVOKED
Starts: 2018-12-10T13:45:00.000Z
Expires: 2018-12-10T13:45:00.000Z
```

From [`OnTokenOffered` 🔔 handler](<../🪣🧱 13 Offered 🔔 event/🤵 OnTokenOffered 🔔 handler.md>)

```yaml
Language: en-us
IssuerTitle: Any Issuer
SchemaTitle: Any Schema Title
Description: Any Schema description.
Title: Any Schema, by Any Issuer
```

From [`Saved@Broker` 🐌 handler](<../../../🤵📨 Broker msgs/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 📃 handler.md>)

```yaml
Path: /path/to/token
```

From [`OnPopTagToken` 📃 handler](<../../../🤵😃 Broker talkers/PopToken 🎫 talker/Token » Tag/🤵 PopTokenTag 😃 handler.md>)

```yaml
Tag: My Token
```


|Property|Type|Description | Origin | Purpose
|-|-|-|-|-
| `Wallet` | uuid | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) |  | [`Frontend@`](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
| `Token` | uuid | [Token 🎫](<../../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) | [`Issue@`](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Offered@`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)
| `Issuer` |text| [Issuer 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>)  | [`Issue@`](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Offered@`](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴📨 Issuer msgs/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)
| `IssuerTitle` |text| [Issuer 🎴](<../../../../../41 🎭 Domain Roles/Issuers 🎴/🎴 Issuer/🎴🎭 Issuer role.md>) Title | | [`Frontend@`](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
| `Schema` |text| [Schema Code 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`Issue@`](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Query@`](<../../../🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Starts` | time | Valid from | [`Issue@`](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Query@`](<../../../🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Expires` | time | Valid until | [`Issue@`](<../../../🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) | [`Query@`](<../../../🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Path` |text| [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) path | [`Saved@`](<../../../🤵📨 Broker msgs/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 🐌 msg.md>) | [`Frontend@`](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
| `Status`|text| `ACTIVE` <br/> `SUSPENDED` <br/> `REVOKED` | [`Revise@`](<../../../🤵📨 Broker msgs/Tokens 🎫 Revise 🎴🐌🤵/🤵 Revise 🐌 msg.md>) | [`Query@`](<../../../🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>)
| `Tag` |text| User alias | Pop 🎈 | [`Frontend@`](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
| `Title`|text| [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) title | (multiple) | [`Frontend@`](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
||
