<!-- TODO: Add lists of commands. -->
<!-- TODO: Add initial parser. -->


# 🔆 Pop Vault

> Implements [🧑‍🦰💬🤵 Unbind Vault](<../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Vaults 🗄️/💬🤵 Unbind 🗄️.md>)


```yaml
💬 [Unbind] Vault:

# Get the Vault 
- GET >> $vault:
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
- PARALLEL|$vault.Binds|$bind:
    - SEND:
        To: $bind.Vault
        Subject: Unbound@Vault
        Bind: $bind.ID
    - DELETE|$bind

# Update the bind list
- SEND:
    To: $wallet.Notifier
    Subject: Updated@Notifier
    Wallet: $wallet.ID
    Updates: [ BINDS ]

# Inform the user 🤔
- SUCCESS|Done.
```