<!-- TODO: detail -->

> Example: [Pop Vault 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🔆 Broker locators/🤵🔆 Pop Vault.md>)

```yaml
- PARALLEL|$vault.Binds|$bind >> $binds:
    - MSG:
        To: $bind.Vault
        Subject: Unbound@Vault
        Bind: $bind.ID
    - DELETE|$bind
```