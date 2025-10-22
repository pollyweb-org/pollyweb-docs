<!-- TODO: detail -->

# 😃*️⃣ Talker `PARALLEL` command

> Part of [Talker 😃](<../../😃 Talker role.md>)

<br/>

> Example: [Pop Vault 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📃 Broker scripts/...procedures/🤵📃 Pop Vault 🗄️.md>)

1. **What is a PARALLEL command?**

1. **What is the syntax of the PARALLEL command?**
   
1. **How to use the PARALLEL command?**

1. **What is the difference to a standard FOR cycle?**
```yaml
- PARALLEL|$vault.Binds|$bind >> $binds:
    - SEND:
        To: $bind.Vault
        Subject: Unbound@Vault
        Bind: $bind.ID
    - DELETE|$bind
```