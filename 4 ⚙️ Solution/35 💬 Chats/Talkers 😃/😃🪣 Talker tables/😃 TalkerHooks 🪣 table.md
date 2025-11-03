
<!-- TODO: -->

# 😃🪣 Hooks @ Talker 🪝

> Used in [`Bound@Vault`](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)

> Implements the [`REEL` 🎣 command](<../../Scripts 📃/📃 control ▶️/REEL 🎣/🎣 REEL ⌘ cmd.md>)

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
| Children | [`Holders`](<😃 TalkerHolders 🪣 table.md>)

## Example

```yaml
ID: <hook-uuid>
```