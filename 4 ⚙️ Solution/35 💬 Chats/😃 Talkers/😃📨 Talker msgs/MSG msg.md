<!-- TODO: add details  -->

> Example: [Pop Vault 🔆](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🔆 Broker locators/🤵🔆 Pop Vault.md>)

```yaml
# Get a bind from the database.
- MAP|Binds|<bind-uuid> >> $bind

# Send a message with the bind.
- MSG|Unbound@Vault|$bind.Vault:
    BindID: $bind.ID
```