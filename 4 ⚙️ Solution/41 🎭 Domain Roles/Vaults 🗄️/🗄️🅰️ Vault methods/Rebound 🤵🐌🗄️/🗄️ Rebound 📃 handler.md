# 🗄️ Rebound 📃 handler

## Script
```yaml
📃 Rebound@Vault:

# Verify the message
- VERIFY|$.Msg

# Resolve the bind
- READ >> $bind:
    Set: Vault.Binds
    Key: $.Msg.Hook
```