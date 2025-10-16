# 🔆 Pop Vault

> Implements [🧑‍🦰💬🤵 Unbind Vault](<../../1 🧑‍🦰 Wallets/🧑‍🦰💬 Wallet in Vaults 🗄️/💬🤵 Unbind 🗄️.md>)


```yaml
💬 [Unbind] Vault:

# Get the Vault 
- MAP|$wallet.Vaults|$.Msg.Body.Key >> $vault

# Ask for confirmation 🤔
- CONFIRM|Unbind vault {$vault.Title}?

# Filter the binds.
- FILTER|Which ones? >> $binds:
    Options: $vault.Binds
    ID: ID
    Title: Title

# Remove the binds
- FOR|$vault.Binds >> $bind:
    - CRUD|DELETE|$bind
    - MSG|Unbound@Vault|$bind.Vault:
        BindID: $bind.ID

# Update the bind list
- MSG|Updated@Notifier|$wallet.Notifier:
    WalletID: $wallet.ID
    Updates: [ BINDS ]

# Inform the user 🤔
- SUCCESS|Done.
```