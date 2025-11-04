# 🤵 Merge Schemas 📃 script

> Part of the [`Query` 📃 handler](<../🤵 Query 📃 handler.md>)

> Returns `{Schema, Domain}[]`

## Script 

```yaml
📃 Merge-Schemas:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: chat, Schemas

# Match with Tokens
- EVAL >> $tokens:
    Schema, Issuer
    FROM $:chat.Wallet.Tokens
    MATCH Schema.In($.Msg.Schemas)

# Match with Binds
- EVAL >> $binds:
    Schema, Vault
    FROM $:chat.Wallet.Binds
    MATCH Schema.In($.Msg.Schemas)

# Merge tokens
- EVAL|$tokens +> $merges:
    Schema: Schema
    Domain: Issuers

# Merge binds
- EVAL|$binds +> $merges:
    Schema: Schema
    Domain: Vault
    
# Return the merges
- RETURN:
    $merges
```

|Users||
|-|-
