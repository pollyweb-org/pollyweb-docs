
# 😃🪝 Talker.Hooks 🪣 table 

> Used in [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️📨 Vault msgs/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)

> Implements the [`REEL` 🎣 command](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>)

> Data access

* [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) by [`BIND`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) [`ISSUE`](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴⌘ Issuer cmds/ISSUE 🎫/🎫 ISSUE ⌘ cmd.md>) [`SHARE`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/SHARE 💼/💼 SHARE ⌘ cmd.md>)
* [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) by the [`REEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>) command

## Schema

```yaml
# Hooks.yaml

Prefix: Talker
Table: Hooks
Keys: ID
Children: 
    Holders: {Holders.Hook: Hooks.ID}
```

| Relationship | Table | Contains
|-|-|-
| Children | [`Holders`](<../Imprint🦶 » Recall 🪶/😃 Talker.Holders 🪣 table.md>)

## Example

```yaml
ID: <hook-uuid>
```