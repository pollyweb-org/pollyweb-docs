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
