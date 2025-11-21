# 🧠 Text holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are the built-in functions for text strings?**

    |Group| [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | Returns| Details 
    |-|-|-|-
    | Assess| [`.IsEmpty`](<../Any 📚 holders/IsEmpty ⓕ any.md>) | bool | Is it an empty text?
    |       | [`.IsNotEmpty`](<../Any 📚 holders/IsNotEmpty ⓕ any.md>) | bool | Is it text, not just spaces?
    |Bounds | [`.IsAbove`](<../Any 📚 holders/IsAbove ⓕ any.md>) | bool | Is it after in alphabetical order?
    |       | [`.IsBelow`](<../Any 📚 holders/IsBelow ⓕ any.md>) | bool | Is it before in alphabetical order?
    |       | [`.IsBetween`](<../Any 📚 holders/IsBetween ⓕ any.md>) | bool | Is it between in alphabetical order?
    |Compare| [`.Is`](<../Any 📚 holders/Is ⓕ any.md>) | bool | Does it have the same meaning?
    |       | [`.IsNot`](<../Any 📚 holders/IsNot ⓕ any.md>) | bool | Does it have another meaning?
    |       | [`.Equals`](<../Any 📚 holders/Equals ⓕ any.md>) | bool | Is it exactly the same string of chars?
    |       | [`.Differs`](<../Any 📚 holders/Differs ⓕ any.md>) | bool | Is it a different string of chars?
    |Lists  | [`.IsIn`](<../Any 📚 holders/IsIn ⓕ any.md>) |bool| Is it in a given list of texts?
    |Chars| [`.Length`](<../Any 📚 holders/Length ⓕ.md>) |[num](<../Num 📚 holders/🧠 Num holders.md>)| How many chars does it contain?
    |       | [`.Size`](<../Any 📚 holders/Size ⓕ.md>) |[num](<../Num 📚 holders/🧠 Num holders.md>)| Same as [`.Length`](<../Any 📚 holders/Length ⓕ.md>)
    |       | [`.First`](<../Any 📚 holders/First ⓕ.md>) |[text](<🧠 Text holders.md>)| What's the first char?
    |       | [`.Last`](<../Any 📚 holders/Last ⓕ.md>) |[text](<🧠 Text holders.md>)| What's the last char?
    |       | [`.Contains`](<../Any 📚 holders/Contains ⓕ any.md>) |bool| Does it contain a given char?
    |Change | [`.Append`](<Append ⓕ text.md>) |[text](<🧠 Text holders.md>)| What we append the given string?
    |       | [`.Add`](<../Any 📚 holders/Add ⓕ any.md>) |[text](<🧠 Text holders.md>)| Same as [`.Append`](<Append ⓕ text.md>)
    |       | [`.Plus`](<../Any 📚 holders/Plus ⓕ any.md>) |[text](<🧠 Text holders.md>)| Same as [`.Append`](<Append ⓕ text.md>)
    |       | [`.Remove`](<../Any 📚 holders/Remove ⓕ.md>) |[text](<🧠 Text holders.md>)| What if we remove the given string?
    |       | [`.Minus`](<../Any 📚 holders/Minus ⓕ any.md>) |[text](<🧠 Text holders.md>)| Same as [`.Remove`](<../Any 📚 holders/Remove ⓕ.md>)
    |       | [`.Diff`](<../Any 📚 holders/Diff ⓕ.md>) |[text](<🧠 Text holders.md>)| Same as [`.Remove`](<../Any 📚 holders/Remove ⓕ.md>)
    |       | [`.Translate`](<Translate ⓕ.md>) |[text](<🧠 Text holders.md>)| Translates between languages
    |Create | [`.UUID`](<../../📃 Functions 🐍/🐍 System 🔩 functions/generators/UUID ⓕ.md>) |[text](<🧠 Text holders.md>)| Returns a new unique ID
    |Parse|[`.Locator`](<../../📃 Functions 🐍/🐍 System 🔩 functions/parsers/Locator ⓕ.md>) | [map](<../Map 📚 holders/🧠 Map holders.md>) | Parses a [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) string
    |     |[`.Schema`](<../../📃 Functions 🐍/🐍 System 🔩 functions/parsers/Schema ⓕ.md>)  | [map](<../Map 📚 holders/🧠 Map holders.md>) | Parses a [Schema Code 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) string

    ---
    <br/>