# 😃 Append ⓕ

> Used by [`.Add`](<Add ⓕ any.md>) [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)

## FAQ

1. **What's the syntax of $text.Append?**

    ```yaml
    .Append($text, appendixes...)
    ```

    Input | Purpose | Example
    |-|-|-
    |`$text` | Original [Text 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>) | `AB` `$str`
    |`appendixes...` | string to append | `CD`
    

    ---
    <br/>

1. **What are usage examples of $text.Append?**

    |       | Task  | List | Appendix   | Output
    |-|-|-|-|-
    |  | Append | `AB` | `CD` | `ABCD`
    
    ---
    <br/>



1. **What's the syntax of $list.Append?**

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

1. **What are usage examples of $list.Append?**

    | | Task  | List | Appendix   | Output
    |-|-|-|-|-
    |  | Append | `[1,2]` | `3` | `[1,2,3]`
    |           | Merge  | `[1,2]` | `[3,4]` | `[1,2,3,4]`
    
    ---
    <br/>

