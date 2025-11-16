# 🔽 FILTER 📃 script

> Purpose
* Implements the [`FILTER`](<🔽 FILTER ⌘ cmd.md>) command.

## Script

```yaml
📃 .FILTER:

# Assert the inputs
- ASSERT:
    AllOf: $Filters
    Lists: $Set, $Filters

# Filter the list
- CALL|.Filter >> $output:
    - $Set
    - $Filters

# Return the output
- RETURN|$output
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CALL`](<../CALL 🧮/🧮 CALL ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Filter`](<../../../📃 Holders 🧠/Set 🧠 holders/Filter ⓕ set.md>)
|