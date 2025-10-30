# 🤵📃 Join

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 commands ⌘/Script 📃/📃 Script.md>) that implements the [`Join@Broker`](<🤵 Join 🐌 msg.md>) method.

## Script

```yaml
📃 Join@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    OneOf: Chat, Host, Token, Issuer, Bind, Vault
    UUIDs: Chat, Token, Bind
    Texts: Host, Issuer, Vault
```

<!-- TODO: Finish the code -->
<!-- TODO: add a script diagram -->