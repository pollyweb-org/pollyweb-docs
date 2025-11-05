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
    | `{/path/to/file}` | A file in the [Hoster ☁️](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) file system.
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

1. **What are the built-in functions for time?**

    |Group| Function | Details 
    |-|-|-
    |Get    | {{.Now}}      | What's the current time?
    |       | {{This}}      | What's the given current period? 
    |       | {{Previous}}  | What's the given previous period? 
    |Compare| {{.Between}}  | Is it between two given times?
    |       | {{.Is}}       | Is it in a given period?
    |Change | {{.Add}}

    ---
    <br/>

1. **What are the built-in functions for lists?**

    Group | Function | Purpose 
    |-|-|-
    |Size   | [`.IsEmpty`](<../📃 functions 🐍/🔩 {.IsEmpty}.md>)  | Is empty?
    |       | {{.IsOne}}    | Has only one item?
    |       | [`.AreMany`](<../📃 functions 🐍/🔩 {.AreMany}.md>)  | Has more than one item?
    |       | [`.Length`](<../📃 functions 🐍/🔩 {.Length}.md>)   | What's the length?
    |       | [`.Size`](<../📃 functions 🐍/🔩 {.Size}.md>)     | What's the length?
    |Query| [`.Contains`](<../📃 functions 🐍/🔩 {.Contains}.md>) | Contains a given item?
    |       | {{.First}}    | What's the first item?
    |       | {{.Last}}     | What's the last item
    |       | {{.Equals}}   | Has these items in this order?
    |       | {{.Differs}}  | Does not equal this other list?
    |       | {{.Is}}       | Has these items in any order?
    |       | {{.IsNot}}    | Are any of these items missing?
    |Change | [`.Distinct`](<../📃 functions 🐍/🔩 {.Distinct}.md>) | What are the unique items?
    |       | {{.Filter}}   | What items meet given filters?
    |       | {{.Add}}      | What if we add items?
    |       | {{.Minus}}    | What if we remove items?
    
    ---
    <br/>

1. **What are examples of built-in helper functions?**

    | Function | Details | Example
    |-|-|-
    | [`.Add`](<../📃 functions 🐍/🔩 {.Add}.md>) | Add math, text, lists, objects | `.Add(10,-4)` → `6`
    | [`.Diff`](<../📃 functions 🐍/🔩 {.Diff}.md>) | Difference between lists| `.Diff([1,2,3], [2])`
    | [`.IsIn`](<../📃 functions 🐍/🔩 {.IsIn}.md>) | A value is in a list? | `.IsIn(1, [1,2,3])`
    | [`.Now`](<../📃 functions 🐍/🔩 {.Now}.md>) | Current time | 	`2025-10-24T00:05:18Z`
    | [`.Random`](<../📃 functions 🐍/🔩 {.Random}.md>) | Random integer | `.Random(1,9)` → `7`
    | [`.Today`](<../📃 functions 🐍/🔩 {.Today}.md>) | Current date | `2025-10-24T00:00:00Z`
    | [`.UUID`](<../📃 functions 🐍/🔩 {.UUID}.md>) | New UUID | `<uuid>`
    
    ---
    <br/>
