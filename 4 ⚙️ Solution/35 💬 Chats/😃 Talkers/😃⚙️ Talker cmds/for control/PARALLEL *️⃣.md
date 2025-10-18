<!-- TODO: detail -->

> Example: [Pop Vault 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🔆 Broker locators/🤵🔆 Pop Vault.md>)

```yaml
- PARALLEL|$vault.Binds >> $bind:
    - MSG|Unbound@Vault|$bind.Vault:
        Bind: $bind.ID
    - DELETE|$bind
```