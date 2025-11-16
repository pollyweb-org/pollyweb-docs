# 😃🔩 Talker `{.Append}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Used by [`.Add`](<../Any 🧠 holders/.Add 🔩 any.md>) [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)

# FAQ

1. **What is the .Append function?**

    `{.Append}` 
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that appends text to a [Text 🧠 holder](<🧠 Text holders.md>), 
    * and appends items to a [List 🧠 holder](<../List 🧠 holders/List holders.md>).

    ---
    <br/>

1. **What's the syntax of .Append?**

    ```yaml
    .Append(list, appendixes...)
    ```

    Input | Purpose | Example
    |-|-|-
    |`list` | Original [Text 🧠](<🧠 Text holders.md>), | `AB` `$str`
    |       | or [List 🧠](<../List 🧠 holders/List holders.md>) of items |  `[A,B]` `$list`
    |`appendixes...` | string to append, | `CD`
    |           | or item to append, |  `C`
    |           | or items to merge | `[C,D]` `C,D`


    ---
    <br/>

1. **What are usage examples?**

    | Type      | Task  | List | Appendix   | Output
    |-|-|-|-|-
    | [Texts 🧠](<🧠 Text holders.md>)    | Append | `AB` | `CD` | `ABCD`
    | [Lists 🧠](<../List 🧠 holders/List holders.md>)   | Append | `[1,2]` | `3` | `[1,2,3]`
    |           | Merge  | `[1,2]` | `[3,4]` | `[1,2,3,4]`
    
    ---
    <br/>

