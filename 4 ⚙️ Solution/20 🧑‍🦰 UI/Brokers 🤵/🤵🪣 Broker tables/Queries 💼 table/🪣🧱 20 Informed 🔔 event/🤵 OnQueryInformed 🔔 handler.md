# 🤵 OnQueryInformed 🔔 handler

> About
* Part of the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) role
* Part of the [`Broker.Queries` 🪣 table](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 OnQueryInformed ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryInformed:

# Get the candidate Binds
- SELECT >> $queryBinds:
    AllOf: 
        ID: .UUID
        Title:
        Type: BIND
        Key: Bind
        Domain: Vault
        Schema:
    FROM: $Query.Wallet.QueryBinds
    WHERE: Schema.IsIn($Query.Schemas)

# Get the candidate Tokens
- SELECT >> $queryTokens:
    AllOf: 
        ID: .UUID
        Title:
        Type: TOKEN
        Key: Token
        Domain: Issuer
        Schema:
    FROM: $Query.Wallet.QueryTokens
    WHERE: Schema.IsIn($Query.Schemas)

# Merge the lists
PUT >> $matches:
    $queryTokens
    $queryBinds

# Add the matches to the Query item
- SAVE|$Query:
    Matches: $matches
    .State: .If($matches, MATCHED, UNMATCHED)
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) [`Tokens`](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) [`Binds`](<../../Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsIn`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.If`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/If ⓕ.md>)
|
