<!-- TODO -->

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
|[Commands ⌘](<../../📃 basics/Command ⌘.md>) | [`ASSERT`](<../ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`RETURN`](<../../📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)
| [{Functions} 🐍](<../../📃 basics/Function 🐍.md>) | [`.Filter`](<../../📃 functions 🐍/🔩 {.Filter}.md>)
|