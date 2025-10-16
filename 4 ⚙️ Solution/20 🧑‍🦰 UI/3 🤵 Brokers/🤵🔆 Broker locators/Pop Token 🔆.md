# 🔆 Pop Token

```yaml
💬 [Remove] Token:

# Get the Wallet 🧑‍🦰
- MAP|Wallets|$.Msg.Header.From >> $wallet

# Get the Token 🎫
- MAP|$wallet.Tokens|$.Msg.Body.Key >> $token

# Ask for confirmation 🤔
- CONFIRM: Remove token {$token.Title}?

# Remove the Token 🎫
- CRUD|DELETE|$token

# Update the Token 🎫 list
- MSG|Updated@Notifier|$wallet.Notifier
    WalletID: $wallet.ID
    Updates: [ TOKENS ]

# Inform the user 🤔
- SUCCESS: Token removed.
```