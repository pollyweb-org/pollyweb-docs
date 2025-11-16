# 🧠 Bool holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are Bool holders?**

    `Bool` holders
    * capture binary states such as `True` and `False`
    * steer [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) branches like guards, flags, and feature toggles
    * can be empty until a condition is evaluated.

    ---
    <br/>

1. **How are they called across the main programming languages?**
   
    |Language|Synonyms
    |-|-
    | `C#`         | Bool, Boolean
    | `Go`         | Bool
    | `Java`       | Boolean
    | `JavaScript` | Boolean, Bool
    | `PHP`        | Bool, Boolean
    | `Python`     | Bool, Boolean
    | `Ruby`       | Bool, Boolean
    | `Swift`      | Bool, Boolean
    
    ---
    <br/>

1. **What are the built-in functions for bools?**

    |Group| [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | Returns| Details 
    |-|-|-|-
    |Assess| [`.IsEmpty`](<../🧠🔩 Any holders/🔩 {$holder.IsEmpty}.md>) |bool| Is it unset or missing?
    |      | [`.IsNotEmpty`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsNotEmpty}.md>) |bool| Has a value been provided?
    |Compare| [`.Is`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Is}.md>) |bool| Is it the expected boolean?
    |        | [`.IsNot`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsNot}.md>) |bool| Is it the opposite value?
    |        | [`.Equals`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Equals}.md>) |bool| Equal comparison alias for `.Is`
    |        | [`.Differs`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Differs}.md>) |bool| Not-equal alias for `.IsNot`
    |Lists  | [`.IsIn`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsIn}.md>) |bool| Is it one of the accepted values?
    |Combine| [`.AllOf`](<../../📃 Functions 🐍/🐍 System 🔩 functions/asserts/🔩 AllOf.md>) |bool| Are all of these booleans `true`?
    |       | [`.AnyOf`](<../../📃 Functions 🐍/🐍 System 🔩 functions/asserts/🔩 AnyOf.md>) |bool| Is any of these booleans `true`?
    |       | [`.OneOf`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.OneOf}.md>) |bool| Is exactly one of them `true`?
    |Default| [`.Default`](<../🧠🔩 Any holders/🔩 {.Default}.md>) |bool| Substitute a fallback when empty
    
    ---
    <br/>

1. **What are the commands for bool holders?**

    |[Command ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| Purpose
    |-|-
    | 🚦 [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) | Validates a condition resolves to the expected boolean
    | 📭 [`DEFAULT`](<../../📃 Commands ⌘/⌘ for holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>) | Applies a fallback boolean when empty
    | ⬇️ [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) | Overwrites a bool holder with a new value
    | ↘️ [`SET`](<../../📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>) | Overwrites a bool holder with a new value
    
    ---
    <br/>

[bool]: <Bool holders.md>
