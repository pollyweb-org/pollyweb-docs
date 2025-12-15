# 🌪️ DISTINCT 📃 script

> Purpose
* Implements the [`DISTINCT`](<🌪️ DISTINCT ⌘ cmd.md>) command.

## Script

```yaml
📃 .DISTINCT:

# Assert the inputs
- ASSERT:
    AllOf: $lists
    Lists: $lists

# Filter the list
- PUT >> $output:
    .Distinct: $lists

# Return the output
- RETURN: $output
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PUT`](<../PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Distinct`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Distinct ⓕ.md>)
|