# 🤵 OnTokenDetailed 📃 handler

<br/>

## Script

```yaml
📃 OnTokenDetailed:

# Assert the inputs
- ASSERT|$Token:
    AllOf: Schema, Issuer, Language

# Invoke Save@Notifier
- SEND:
    Header:
        To: $Token.Wallet.Notifier
        Subject: Save@Notifier
    Body:
        Wallet: $Token.Wallet
        Hook: $Token.Hook
        Token: $Token.ID
```