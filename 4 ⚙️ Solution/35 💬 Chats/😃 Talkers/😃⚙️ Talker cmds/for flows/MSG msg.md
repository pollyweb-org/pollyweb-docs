<!-- TODO: add details  -->

> Example: [Pop Vault 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🔆 Broker locators/🤵🔆 Pop Vault.md>)

```yaml
# Get a bind from the database.
- GET|Binds|<bind-uuid> >> $bind

# Send a message with the bind.
- MSG|Unbound@Vault|$bind.Vault:
    Bind: $bind.ID
```