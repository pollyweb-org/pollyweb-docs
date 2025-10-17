<!-- TODO: Add lists of commands. -->
<!-- TODO: Add initial parser. -->


# 🔆 Pop Vault

> Implements [🧑‍🦰💬🤵 Unbind Vault](<../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Vaults 🗄️/💬🤵 Unbind 🗄️.md>)


```yaml
💬 [Unbind] Vault:

# Get the Vault 
- MAP >> $vault:
    Pool: $wallet.Vaults
    Key: $.Msg.Body.Key

# Ask for confirmation 🤔
- CONFIRM|Unbind vault {$vault.Title}?

# Filter the binds.
- FILTER|Which ones? >> $binds:
    Options: $vault.Binds
    ID: ID
    Title: Title

# Remove the binds
- PARALLEL|$vault.Binds >> $bind:
    - MSG|Unbound@Vault|$bind.Vault:
        BindID: $bind.ID
    - DELETE|$bind

# Update the bind list
- MSG|Updated@Notifier|$wallet.Notifier:
    WalletID: $wallet.ID
    Updates: [ BINDS ]

# Inform the user 🤔
- SUCCESS|Done.
```