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
- EVAL|.Distinct >> $output:
    - $lists

# Return the output
- RETURN|$output
```

Uses||
|-|-
|[Commands ⌘](<../../📃 basics/Command ⌘.md>) | [`ASSERT`](<../ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`RETURN`](<../../📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)
| [{Functions} 🐍](<../../📃 basics/Function 🐍.md>) | [`.Distinct`](<../../📃 functions 🐍/🔩 {.Distinct}.md>)
|