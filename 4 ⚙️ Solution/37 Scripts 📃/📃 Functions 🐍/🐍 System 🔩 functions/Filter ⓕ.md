# 😃ⓕ `set.Filter` extension

> Part of [Set 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>)

> Used by [`FILTER`](<../../📃 Commands ⌘/⌘ for holders 🧠/FILTER 🔽/🔽 FILTER ⌘ cmd.md>) [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) 

## FAQ


1. **What's the .Filter syntax?**

    ```yaml
    .Filter($set, filters...)
    ```

    Inputs|Type|Details | Example
    |-|-|-|-
    |`$set`| [Set 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>) | Items to be filtered | `{A:1},{A:2}`
    |`filters...`| list | Boolean evaluations | `A.Is(2)` `A:2`

    ---
    <br/>

1. **What are example outputs?**

    ||Input [Set 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>)|Input filter|Output
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
    |`$items` |`SupID`[`.Is`](<Is ⓕ.md>)`(X)` <br/> `Price`[`.IsAtLeast`](<IsAtLeast ⓕ.md>)`(30)`  | Items 3 and 4

    ---
    <br/>

1. **What are examples for functions for filtering?**

    |Function|Purpose
    |-|-
    |[`.Contains`](<Contains ⓕ.md>)  | A list property contains a given value?
    |[`.Equals`](<Equals ⓕ.md>)    | A property equals a given value?
    |[`.Differs`](<Differs ⓕ.md>)   | A property does not equal a given value?
    |[`.IsBetween`](<IsBetween ⓕ.md>)| A property is between two given values?
    |[`.IsIn`](<IsIn ⓕ.md>)        | A property is in a given list?
    |[`.IsNotIn`](<IsNotIn ⓕ.md>)   | A property is not in a given list?
    |[`.Is`](<Is ⓕ.md>)        | A property is similar to a given value?
    |[`.IsNot`](<IsNot ⓕ.md>)        | A property is not similar to given value?
    |[`.IsAbove`](<IsAbove ⓕ.md>)   | A property is above a given value?
    |[`.IsAtLeast`](<IsAtLeast ⓕ.md>) | A property is equal or above a value?
    |[`.IsBelow`](<IsBelow ⓕ.md>)   | A property is below a value?
    |[`.IsAtMost`](<IsAtMost ⓕ.md>)  | A property is equal or below a value?
    |[`.IsEmpty`](<IsEmpty ⓕ.md>)   | A property is empty?
    |[`.IsNotEmpty`](<IsNotEmpty ⓕ.md>)   | A property is not empty?
    

    ---
    <br/>