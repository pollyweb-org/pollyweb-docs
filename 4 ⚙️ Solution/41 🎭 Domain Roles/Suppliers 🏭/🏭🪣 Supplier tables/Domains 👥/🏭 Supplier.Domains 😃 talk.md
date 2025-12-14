# 🏭 Supplier.Domains 😃 talk

## Script

```yaml
💬 Register Domain:

- BIND: .HOST >> $bind
- SHARE: .DOMAIN >> $token
- SAVE Supplier.Domains >> $domain:
    Domain: $token.Issuer
    Bind: $bind.ID
    Token: $token
```

Uses: [`BIND`](<../../../Vaults 🗄️/🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) [`SHARE`](<../../../Consumers 💼/💼⌘ Consumer cmds/SHARE 💼/💼 SHARE ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)