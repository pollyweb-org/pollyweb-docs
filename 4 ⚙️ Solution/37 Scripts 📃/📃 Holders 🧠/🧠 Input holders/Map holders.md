# 🧠 Map holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are Map holders?**

    Map holders 
    * are [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    * store key-value pair structures - e.g. `{A:1,B:2}`

    ---
    <br/>

1. **How are the called across the main programming languages?**
   
    |Synonym |Languages
    |-|-
    | `Array` | PHP, Shell scripting
    | `Dictionary` | C#, Python, Objective-C, Swift, VB.NET
    | `Document` | NoSQL
    | `Element` | XML
    | `Hash` | Perl, Ruby
    | `List` | R, Haskell
    | `Map` | C++, Dart, Erlang, F#, Go, Java, Kotlin, Rust, Scala
    | `Mapping`| Python, YAML
    | `Object` | Javascript, JSON
    | `Pairs` | Fortran, Pascal
    | `Record` | TypeScript
    | `Table` | COBOL, PowerShell, SQL

    ---
    <br/>

1. **What are the built-in functions for maps?**

    |Group| [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | Type | Details 
    |-|-|-|-
    | Assess| [`.IsEmpty`](<../../📃 Functions 🐍/🐍🧠 Holder functions/🔩 {Holder.IsEmpty}.md>) | bool| Is it an empty [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)?
    |       | [`.IsNotEmpty`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsNotEmpty}.md>) | bool | Does it contain a map?
    |Compare| [`.Is`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Is}.md>) | bool | Is it the same map meaning?
    |       | [`.IsNot`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsNot}.md>) | bool | Is it a different meaning?
    |       | [`.Equals`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Equals}.md>) | bool | Same as [`.Is`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Is}.md>) 
    |       | [`.Differs`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Differs}.md>) | bool | Same as [`.IsNot`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsNot}.md>)
    |Read | [`.Key`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Key}.md>) | [map][map] | Return a pair with a given key
    || [`.Keys`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Keys}.md>) | [list](<List holders.md>)  |Return all pair keys as a [List 🧠](<List holders.md>)
    || [`.Value`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Value}.md>) | any | Return the value of a given key
    || [`.Values`](<../../📃 Functions 🐍/🐍🧠 Map functions/🔩 {Map.Values}.md>) | [list](<List holders.md>) | Return all pair values as a [List 🧠](<List holders.md>)
    |Change | [`.Set`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Set}.md>) |[map][map]|  Change or add one or more pairs
    ||[`.Add`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>) | [map][map] | Same as [`.Set`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Set}.md>)
    |       | [`.Plus`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Plus}.md>) | [map][map] | Same as [`.Set`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Set}.md>)
    |       | [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>) | [map][map] | Remove one or more keys
    |       | [`.Minus`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Minus}.md>) | [map][map] | Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>)
    |       | [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>) | [map][map] | Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>)

    ---
    <br/>

[map]: <Map holders.md>