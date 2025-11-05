# 😃🐍 Talker `{Function}` 

> Part of [Script 📃](<Script 📃.md>)

<br/>

1. **What's a Talker {Function}?**

    A [{Function}](<Function 🐍.md>) 
    * is a string encapsulated in brackets 
    * that calculates one if the following values.

    |Format|Details
    |-|-
    | `{$holder}`| The value of a [holder 🧠](<Holder 🧠.md>).
    | `{/path/to/file}` | A file in the [Hoster ☁️](<../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) file system.
    | `{handler(args)}`| Logic in a code handler - e.g., python.
    | `{.helper(args)}`| Pre-built functions - e.g., `Sum()`
    

    ---
    <br/>
    


1. **What's the syntax for built-in helper functions?**

    ```yaml
    {.helper(params)}
    ```

    | Input| Purpose
    |-|-
    | `.helper`  | Name of the built-in helper function.
    | `params`  | Optional comma-separated parameters.

    ---
    <br/>



1. **What are examples of built-in helper functions?**

    |[Holder 🧠 type](<Holder 🧠.md>)|Examples
    |-|-
    |[`List` holders](<../../37 Scripts 📃/📃 Holders 🧠/🧠 Holder types/List holders.md>) | [`.Size`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Size}.md>) [`.Contains`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Contains}.md>) [`.Filter`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Filter}.md>) [`.Distinct`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Distinct}.md>)
    |[`Math` holders](<../../37 Scripts 📃/📃 Holders 🧠/🧠 Holder types/Math holders.md>) | [`.IsBetween`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.IsBetween}.md>) [`.IsAtLeast`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.IsAtLeast}.md>) [`.IsBelow`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.IsBelow}.md>) [`.Random`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Random}.md>)
    |[`Text` holders](<../../37 Scripts 📃/📃 Holders 🧠/🧠 Holder types/Text holders.md>) | [`.UUID`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.UUID}.md>) [`.Is`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Is}.md>) [`.Equals`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Equals}.md>) [`.Diff`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Diff}.md>)
    |[`Time` holders](<../../37 Scripts 📃/📃 Holders 🧠/🧠 Holder types/Time holders.md>)| [`.Now`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Now}.md>) [`.Today`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Today}.md>) [`.This`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.This}.md>) [`.Previous`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System functions 🔩/🔩 {.Previous}.md>)


    ---
    <br/>
