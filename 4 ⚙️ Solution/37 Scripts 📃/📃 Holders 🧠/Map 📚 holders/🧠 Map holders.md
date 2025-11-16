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
    | Assess| [`.IsEmpty`](<../Any 📚 holders/IsEmpty ⓕ any.md>) | bool| Is it an empty [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)?
    |       | [`.IsNotEmpty`](<../Any 📚 holders/IsNotEmpty ⓕ any.md>) | bool | Does it contain a map?
    |Compare| [`.Is`](<../Any 📚 holders/Is ⓕ any.md>) | bool | Is it the same map meaning?
    |       | [`.IsNot`](<../Any 📚 holders/IsNot ⓕ any.md>) | bool | Is it a different meaning?
    |       | [`.Equals`](<../Any 📚 holders/Equals ⓕ any.md>) | bool | Same as [`.Is`](<../Any 📚 holders/Is ⓕ any.md>) 
    |       | [`.Differs`](<../Any 📚 holders/Differs ⓕ any.md>) | bool | Same as [`.IsNot`](<../Any 📚 holders/IsNot ⓕ any.md>)
    |Read | [`.Key`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Key}.md>) | [map][map] | Return a pair with a given key
    || [`.Keys`](<Keys ⓕ map.md>) | [list](<../List 📚 holders/🧠 List holders.md>)  |Return all pair keys as a [List 🧠](<../List 📚 holders/🧠 List holders.md>)
    || [`.Value`](<../Any 📚 holders/Value ⓕ any.md>) | any | Return the value of a given key
    || [`.Values`](<Values ⓕ map.md>) | [list](<../List 📚 holders/🧠 List holders.md>) | Return all pair values as a [List 🧠](<../List 📚 holders/🧠 List holders.md>)
    |Change | [`.Set`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Set}.md>) |[map][map]|  Change or add one or more pairs
    ||[`.Add`](<../Any 📚 holders/Add ⓕ any.md>) | [map][map] | Same as [`.Set`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Set}.md>)
    |       | [`.Plus`](<../Any 📚 holders/Plus ⓕ any.md>) | [map][map] | Same as [`.Set`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Set}.md>)
    |       | [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>) | [map][map] | Remove one or more keys
    |       | [`.Minus`](<../Any 📚 holders/Minus ⓕ any.md>) | [map][map] | Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>)
    |       | [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>) | [map][map] | Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>)

    ---
    <br/>

[map]: <Map holders.md>