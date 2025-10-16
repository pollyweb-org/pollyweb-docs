# 🔆 Pop Vault

```yaml
💬 [Unbind] Vault:

# Get the Wallet 🧑‍🦰
- MAP|Wallets|$.Msg.Header.From >> $wallet

# Get the Vault 🎫
- MAP|$wallet.Vaults|$.Msg.Body.Key >> $vault

# Ask for confirmation 🤔
- CONFIRM: Unbind vault {$vault.Title}?

# Remove the Token 🎫
- CRUD|DELETE|$token

# Update the Token 🎫 list
- MSG|Updated@Notifier|$wallet.Notifier
    WalletID: $wallet.ID
    Updates: [ TOKENS ]

# Inform the user 🤔
- SUCCESS: Token removed.
```