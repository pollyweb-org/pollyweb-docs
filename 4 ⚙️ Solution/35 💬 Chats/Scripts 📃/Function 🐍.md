# 😃🐍 Talker `{Function}` 

> Part of [Script 📃](<Script 📃.md>)

<br/>

1. **What's a Talker {Function}?**

    A [{Function}](<Function 🐍.md>) 
    * is a string encapsulated in brackets 
    * that calculates one if the following values.

    |Format|Details
    |-|-
    | [`{$holder}`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 Functions types/🧠 {$holder}.md>) | The value of a [holder 🧠](<Holder 🧠.md>).
    | [`{/path/to/file}`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 Functions types/📄 {file}.md>) | A file in the [Hoster ☁️](<../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) file system.
    | [`{handler(args)}`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>) | Logic in a code handler - e.g., python.
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
    | [Holders 🧠](<Holder 🧠.md>) | [`.IsEmpty`](<../../37 Scripts 📃/📃 Holders 🧠/Any 🧠 holders/.IsEmpty 🔩 any.md>) [`.IsNotEmpty`](<../../37 Scripts 📃/📃 Holders 🧠/Any 🧠 holders/.IsNotEmpty 🔩 any.md>) [`.Assert`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/assert/🔩 Assert.md>) [`.AllOf`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/assert/🔩 AllOf.md>) 
    |[`List` holders](<../../37 Scripts 📃/📃 Holders 🧠/List 🧠 holders/List holders.md>) | [`.Size`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Size}.md>) [`.Contains`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Contains}.md>) [`.Filter`](<../../37 Scripts 📃/📃 Holders 🧠/Set 🧠 holders/Filter ⓕ set.md>) [`.Distinct`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Distinct}.md>)
    |[`Num` holders](<../../37 Scripts 📃/📃 Holders 🧠/Num 🧠 holders/🧠 Num holders.md>) | [`.IsBetween`](<../../37 Scripts 📃/📃 Holders 🧠/Any 🧠 holders/.IsBetween 🔩 any.md>) [`.IsAtLeast`](<../../37 Scripts 📃/📃 Holders 🧠/Any 🧠 holders/.IsAtLeast 🔩 any.md>) [`.IsBelow`](<../../37 Scripts 📃/📃 Holders 🧠/Any 🧠 holders/.IsBelow 🔩 any.md>) [`.Random`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Random}.md>)
    |[`Text` holders](<../../37 Scripts 📃/📃 Holders 🧠/Text 🧠 holders/🧠 Text holders.md>) | [`.UUID`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.UUID}.md>) [`.Is`](<../../37 Scripts 📃/📃 Holders 🧠/Any 🧠 holders/.Is 🔩 any.md>) [`.Equals`](<../../37 Scripts 📃/📃 Holders 🧠/Any 🧠 holders/Equals ⓕ any.md>) [`.Diff`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>)
    |[`Time` holders](<../../37 Scripts 📃/📃 Holders 🧠/Time 🧠 holders/🧠 Time holders.md>)| [`.Now`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/time/🔩 Now.md>) [`.Today`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/time/🔩 Today.md>) [`.This`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/time/🔩 This.md>) [`.Previous`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/time/🔩 Previous.md>)


    ---
    <br/>
