# 🧠 Text holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are the built-in functions for text strings?**

    |Group| [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | Returns| Details 
    |-|-|-|-
    | Assess| [`.IsEmpty`](<../🧠🔩 Any holders/any.IsEmpty 🔩 ext.md>) | bool | Is it an empty text?
    |       | [`.IsNotEmpty`](<../🧠🔩 Any holders/any.IsNotEmpty 🔩 ext.md>) | bool | Is it text, not just spaces?
    |Bounds | [`.IsAbove`](<../🧠🔩 Any holders/.IsAbove 🔩 any.md>) | bool | Is it after in alphabetical order?
    |       | [`.IsBelow`](<../🧠🔩 Any holders/.IsBelow 🔩 any.md>) | bool | Is it before in alphabetical order?
    |       | [`.IsBetween`](<../🧠🔩 Any holders/.IsBetween 🔩 any.md>) | bool | Is it between in alphabetical order?
    |Compare| [`.Is`](<../🧠🔩 Any holders/.Is 🔩 any.md>) | bool | Does it have the same meaning?
    |       | [`.IsNot`](<../🧠🔩 Any holders/any.IsNot 🔩 ext.md>) | bool | Does it have another meaning?
    |       | [`.Equals`](<../🧠🔩 Any holders/any.Equals 🔩 ext.md>) | bool | Is it exactly the same string of chars?
    |       | [`.Differs`](<../🧠🔩 Any holders/any.Differs 🔩 ext.md>) | bool | Is it a different string of chars?
    |Lists  | [`.IsIn`](<../🧠🔩 Any holders/🔩 {.IsIn}.md>) |bool| Is it in a given list of texts?
    |Chars| [`.Length`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Length}.md>) |[num][num]| How many chars does it contain?
    |       | [`.Size`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Size}.md>) |[num][num]| Same as [`.Length`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Length}.md>)
    |       | [`.First`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.First}.md>) |[text][text]| What's the first char?
    |       | [`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>) |[text][text]| What's the last char?
    |       | [`.Contains`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Contains}.md>) |bool| Does it contain a given char?
    |Change | [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Append}.md>) |[text][text]| What we append the given string?
    |       | [`.Add`](<../🧠🔩 Any holders/.Add 🔩 any.md>) |[text][text]| Same as [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Append}.md>)
    |       | [`.Plus`](<../🧠🔩 Any holders/any.Plus 🔩 ext.md>) |[text][text]| Same as [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Append}.md>)
    |       | [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>) |[text][text]| What if we remove the given string?
    |       | [`.Minus`](<../🧠🔩 Any holders/any.Minus 🔩 ext.md>) |[text][text]| Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>)
    |       | [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>) |[text][text]| Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>)
    |       | [`.Translate`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Translate}.md>) |[text][text]| Translates between languages
    |Create | [`.UUID`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.UUID}.md>) |[text][text]| Returns a new unique ID
    |Parse|[`.Locator`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Locator}.md>) | [map](<../🧠🔩 Map holders/Map holders.md>) | Parses a [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) string
    |     |[`.Schema`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Schema}.md>)  | [map](<../🧠🔩 Map holders/Map holders.md>) | Parses a [Schema Code 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) string

    ---
    <br/>

[text]: <Text holders.md>
[num]: <Num holders.md>