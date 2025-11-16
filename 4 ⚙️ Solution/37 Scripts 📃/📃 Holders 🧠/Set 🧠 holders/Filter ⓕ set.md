# 😃🔩 Talker `{.Filter}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Used by [`FILTER`](<../../📃 Commands ⌘/⌘ for holders 🧠/FILTER 🔽/🔽 FILTER ⌘ cmd.md>) [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) 

## FAQ

1. **What is the .Filter function?**

    `{.Filter}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that filters a [List 🧠 holder](<../List 🧠 holders/List holders.md>).

    ---
    <br/>

1. **What's the .Filter syntax?**

    ```yaml
    .Filter($set, filters...)
    ```

    Inputs|Type|Details | Example
    |-|-|-|-
    |`$set`| [Set 🧠](<🧠 Set holders.md>) | Items to be filtered | `{A:1},{A:2}`
    |`filters...`| list | Boolean evaluations | `A.Is(2)` `A:2`

    ---
    <br/>

1. **What are example outputs?**

    ||Input [Set 🧠](<🧠 Set holders.md>)|Input filter|Output
    |-|-|-|-
    || `[]` | `A:1` | `[]`
    || `{A:1}` | `[]` | 🚫 Blocked
    || `{A:1},{A:2}` | `A:1` | `A:1`
    || `{A:1},{A:2}` | `A:3` | `[]`

    ---
    <br/>
   
1. **What's an example of .Filter?**

    Consider a list `$items`.

    ```yaml
    ┌────┬───────┬───────┐
    │ ID │ Price │ SupID │
    ├────┼───────┼───────┤
    │  1 │    10 │     A │
    │  2 │    20 │     X │
    │  3 │    30 │     X │
    │  4 │    40 │     X │
    └────┴───────┴───────┘
    ```

    |Input 1 | Input 2 |Output
    |-|-|-
    |`$items` |`SupID:X` | Items 2, 3, and 4
    |`$items` |`SupID`[`.Is`](<../Any 🧠 holders/.Is 🔩 any.md>)`(X)` <br/> `Price`[`.IsAtLeast`](<../Any 🧠 holders/.IsAtLeast 🔩 any.md>)`(30)`  | Items 3 and 4

    ---
    <br/>

1. **What are examples for functions for filtering?**

    |Function|Purpose
    |-|-
    |[`.Contains`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Contains}.md>)  | A list property contains a given value?
    |[`.Equals`](<../Any 🧠 holders/Equals ⓕ any.md>)    | A property equals a given value?
    |[`.Differs`](<../Any 🧠 holders/.Differs 🔩 any.md>)   | A property does not equal a given value?
    |[`.IsBetween`](<../Any 🧠 holders/.IsBetween 🔩 any.md>)| A property is between two given values?
    |[`.IsIn`](<../Any 🧠 holders/.IsIn 🔩 any.md>)        | A property is in a given list?
    |[`.IsNotIn`](<../Any 🧠 holders/.IsNotIn 🔩 any.md>)   | A property is not in a given list?
    |[`.Is`](<../Any 🧠 holders/.Is 🔩 any.md>)        | A property is similar to a given value?
    |[`.IsNot`](<../Any 🧠 holders/.IsNot 🔩 any.md>)        | A property is not similar to given value?
    |[`.IsAbove`](<../Any 🧠 holders/.IsAbove 🔩 any.md>)   | A property is above a given value?
    |[`.IsAtLeast`](<../Any 🧠 holders/.IsAtLeast 🔩 any.md>) | A property is equal or above a value?
    |[`.IsBelow`](<../Any 🧠 holders/.IsBelow 🔩 any.md>)   | A property is below a value?
    |[`.IsAtMost`](<../Any 🧠 holders/.IsAtMost 🔩 any.md>)  | A property is equal or below a value?
    |[`.IsEmpty`](<../Any 🧠 holders/.IsEmpty 🔩 any.md>)   | A property is empty?
    |[`.IsNotEmpty`](<../Any 🧠 holders/.IsNotEmpty 🔩 any.md>)   | A property is not empty?
    

    ---
    <br/>