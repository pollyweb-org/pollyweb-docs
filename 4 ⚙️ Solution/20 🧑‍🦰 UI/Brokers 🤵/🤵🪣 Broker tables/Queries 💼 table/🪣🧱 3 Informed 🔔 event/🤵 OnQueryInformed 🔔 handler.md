# 🤵 OnQueryInformed 🔔 handler

## Diagram

![alt text](<🤵 OnQueryInformed ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnQueryInformed:

# Get the candidate Binds
- SELECT >> $queryBinds:
    AllOf: Bind, Vault, Title
    FROM: $Query.Wallet.QueryBinds
    WHERE: Schema.IsIn($Query.Schemas)

# Get the candidate Tokens
- SELECT >> $queryTokens:
    AllOf: Token, Issuer, Title
    FROM: $Query.Wallet.QueryTokens
    WHERE: Schema.IsIn($Query.Schemas)

# Verify the trust of each token
- PARALLEL|$queryTokens|$token:

    # Ask the Graph
    - TRUSTS >> $trusts:
        Truster: $Query.Consumer
        Trusted: $token.Issuer
        Schema: $token.Schema
        Role: VAULT

    # If trusted, add to the trusted list
    - IF|$trusts:
        PUT +> $trusted:
            Type: TOKEN
            Schema: $token.Schema
            Domain: $token.Issuer
            Title: $token.Title

# Verify the trust of each token
- PARALLEL|$queryTokens|$token:

    # Ask the Graph
    - TRUSTS >> $trusts:
        Truster: $Query.Consumer
        Trusted: $token.Issuer
        Schema: $token.Schema
        Role: VAULT

    # If trusted, add to the trusted list
    - IF|$trusts:
        PUT +> $trusted:
            Type: TOKEN
            Schema: $token.Schema
            Domain: $token.Issuer
            Title: $token.Title
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`TRUSTS`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/TRUSTS 🫡/🫡 TRUSTS ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Queries`](<../🪣 Queries/🤵 Broker.Queries 🪣 table.md>) [`Wallets`](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) [`Tokens`](<../../Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>) [`Binds`](<../../Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
|
