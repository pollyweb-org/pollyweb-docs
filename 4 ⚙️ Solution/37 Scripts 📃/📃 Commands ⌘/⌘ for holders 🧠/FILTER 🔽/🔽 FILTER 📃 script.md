# 🔽 FILTER 📃 script

> Purpose
* Implements the [`FILTER`](<🔽 FILTER ⌘ cmd.md>) command.

## Script

```yaml
📃 .FILTER:

# Assert the inputs
- ASSERT:
    AllOf: $filters
    Lists: $list, $filters

# Filter the list
- EVAL|.Filter >> $output:
    - $list
    - $filters

# Return the output
- RETURN|$output
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Filter`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Filter}.md>)
|