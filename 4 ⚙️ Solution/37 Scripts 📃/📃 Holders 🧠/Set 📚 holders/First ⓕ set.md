# 😃🔩 Talker `{$set.First}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Used by [`.Take`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Take ⓕ.md>) [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)

## FAQ

1. **What is the $set.First function?**

    `{$set.First}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns the start of a [Set 🧠 holder](<🧠 Set holders.md>).


    ---
    <br/>

1. **What's the behavior of .First?**

    |Input|Behavior
    |-|-
    |[`$set`](<../../📃 Holders 🧠/Set 📚 holders/🧠 Set holders.md>)`.First({A:1},n)`| Applies [`.Filter`](<../../📃 Holders 🧠/Set 📚 holders/Filter ⓕ set.md>) then `.First(n)`
    |[$set](<../../📃 Holders 🧠/Set 📚 holders/🧠 Set holders.md>)`.First({A:1})` | Equals `$set.First({A:1},1)`
    ---
    <br/>
