# 🧠 Domain holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are Domain holders?**

    `Domain` holders 
    * are [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) returned by the [`.Domain`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Domain}.md>) function
    * that represent a [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>).

    ---
    <br/>

1. **What are the properties of a domain holder?**

    | Property | Type | Description
    |-| -|-
    | `Name` | [text](<../Text 🧠 holders/🧠 Text holders.md>) | [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
    | `Title` | [text](<../Text 🧠 holders/🧠 Text holders.md>) | Calls and caches [`.Translate`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Translate}.md>)
    | `Description` | [text](<../Text 🧠 holders/🧠 Text holders.md>) | Calls and caches [`.Translate`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Translate}.md>)
    | `IsSecure`| [bool](<../Bool 🧠 holders/Bool holders.md>) | Calls [`.IsSecure`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsSecure}.md>) 
    
    ---
    <br/>


1. **What functions act on domain holders?**

    [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)|Input|Purpose
    |-|-|-
    |[`.IsSecure`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsSecure}.md>) || Indicates if DNSSEC is in place 
    |[`.Translate`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Translate}.md>)|Language| Fills `Title` and `Description` 

    ---
    <br/>