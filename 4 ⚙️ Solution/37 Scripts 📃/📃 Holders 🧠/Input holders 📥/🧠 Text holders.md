# 🧠 Text holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are the built-in functions for text strings?**

    |Group| [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | Returns| Details 
    |-|-|-|-
    | Assess| [`.IsEmpty`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsEmpty ⓕ any.md>) | bool | Is it an empty text?
    |       | [`.IsNotEmpty`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsNotEmpty ⓕ any.md>) | bool | Is it text, not just spaces?
    |Bounds | [`.IsAbove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsAbove ⓕ any.md>) | bool | Is it after in alphabetical order?
    |       | [`.IsBelow`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsBelow ⓕ any.md>) | bool | Is it before in alphabetical order?
    |       | [`.IsBetween`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsBetween ⓕ any.md>) | bool | Is it between in alphabetical order?
    |Compare| [`.Is`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ any.md>) | bool | Does it have the same meaning?
    |       | [`.IsNot`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsNot ⓕ any.md>) | bool | Does it have another meaning?
    |       | [`.Equals`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Equals ⓕ any.md>) | bool | Is it exactly the same string of chars?
    |       | [`.Differs`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Differs ⓕ any.md>) | bool | Is it a different string of chars?
    |Lists  | [`.IsIn`](<../../📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ any.md>) |bool| Is it in a given list of texts?
    |Chars| [`.Length`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Length ⓕ.md>) |[num](<🧠 Num holders.md>)| How many chars does it contain?
    |       | [`.Size`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Size ⓕ.md>) |[num](<🧠 Num holders.md>)| Same as [`.Length`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Length ⓕ.md>)
    |       | [`.First`](<../../📃 Functions 🐍/🐍 System 🔩 functions/First ⓕ text.md>) |[text](<🧠 Text holders.md>)| What's the first char?
    |       | [`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Last ⓕ.md>) |[text](<🧠 Text holders.md>)| What's the last char?
    |       | [`.Contains`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Contains ⓕ any.md>) |bool| Does it contain a given char?
    |Change | [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Append ⓕ.md>) |[text](<🧠 Text holders.md>)| What we append the given string?
    |       | [`.Add`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ any.md>) |[text](<🧠 Text holders.md>)| Same as [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Append ⓕ.md>)
    |       | [`.Plus`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Plus ⓕ any.md>) |[text](<🧠 Text holders.md>)| Same as [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Append ⓕ.md>)
    |       | [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Remove ⓕ.md>) |[text](<🧠 Text holders.md>)| What if we remove the given string?
    |       | [`.Minus`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Minus ⓕ any.md>) |[text](<🧠 Text holders.md>)| Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Remove ⓕ.md>)
    |       | [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Diff ⓕ.md>) |[text](<🧠 Text holders.md>)| Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Remove ⓕ.md>)
    |       | [`.Translate`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Translate ⓕ.md>) |[text](<🧠 Text holders.md>)| Translates between languages
    |Create | [`.UUID`](<../../📃 Functions 🐍/🐍 System 🔩 functions/UUID ⓕ.md>) |[text](<🧠 Text holders.md>)| Returns a new unique ID
    |Parse|[`.Locator`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Locator ⓕ.md>) | [map](<🧠 Map holders.md>) | Parses a [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) string
    |     |[`.Schema`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Schema ⓕ.md>)  | [map](<🧠 Map holders.md>) | Parses a [Schema Code 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) string

    ---
    <br/>