# 😃🔩 Talker `{.Now}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ


1. **What is the .Now function?**

    `{.Now}` 
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns the current time
    * based on the [`$.Chat`](<../🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>) timezone and language.

    ---
    <br/>


1. **What's the syntax of .Now?**

    ```yaml
    .Now
    ````

    ---
    <br/>

1. **What are usage examples?**

    | Context | Invocation  |  Results in...
    |-|-|-
    | [Chat 💬](<../../../35 💬 Chats/Chats 💬/💬 Chat.md>)    | `.Now` | `22:34` `10:34 PM`
    | Custom |      `.Now(Ddd DD, HH:MI:SS)` | `Mon 21, 01:34:06`
    | UTC |      `.Now(UTC)` | `2024-09-21T12:34:00Z`
    | [`.Add`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ any.md>) | `.Now` |`2024-09-21T12:34:00Z`   
    
    ---
    <br/>