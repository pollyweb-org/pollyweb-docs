# 😃 Append ⓕ list

> Part of [List 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>)

> Used by [`.Add`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ any.md>) [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)

## FAQ


1. **What's the syntax of list.Append?**

    ```yaml
    $list.Append(appendixes...)
    ```

    Input | Purpose | Example
    |-|-|-
    |`$list` |  [List 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) of items |  `[A,B]` `$list`
    |`appendixes...` | item to append, |  `C`
    |           | or items to merge | `[C,D]` `C,D`


    ---
    <br/>

1. **What are usage examples?**

    | | Task  | List | Appendix   | Output
    |-|-|-|-|-
    |  | Append | `[1,2]` | `3` | `[1,2,3]`
    |           | Merge  | `[1,2]` | `[3,4]` | `[1,2,3,4]`
    
    ---
    <br/>

