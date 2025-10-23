# 😃🐍 Talker `{Function}` 

> Part of [Talker 😃](<../../😃 Talker role.md>)

<br/>

1. **What's a Talker {Function}?**

    A [{Function}](<{Function} 🐍.md>) 
    * is a string encapsulated in brackets 
    * that calculates one if the following values.

    |Format|Details
    |-|-
    | `{$placeholder}`| The value of a [placeholder 🧠](<../...placeholders/$Placeholder 🧠.md>).
    | `{/path/to/file}` | A file in the [Hoster ☁️](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) file system.
    | `{handler(args)}`| Logic in a code handler - e.g., python.
    | `{.helper(args)}`| Pre-built functions - e.g., `Sum()`
    

    ---
    <br/>
    


1. **What's the syntax for built-in helper functions?**

    ```yaml
    {.helper(params)}
    ```

    | Argument| Purpose
    |-|-
    | `.helper`  | Name of the built-in helper function.
    | `params`  | Optional comma-separated parameters.

    ---
    <br/>


1. **What are examples of built-in helper functions?**

    | Function | Details | Example
    |-|-|-
    | `.Len` | Length of a list | `.Len([x,y,z])` → `3`
    | `.Sum` | Sums numbers | `.Sum([1,2,3])` → `6`
    | `.Subtract` | Subtracts B from A | `.Subtract([10,4])` → `6`
    | `.Multiply` | Multiplies numbers | `.Multiply([2,3,4])` → `24`
    | `.RandomInt` | Random integer | `.RandomInt(1,9)` → `7`
    | `.InRange` | Checks intervals | `.InRange(5,1,10)` → `True`
    | `.Time` | Current time | `.Time()` → `10:30:00Z`
    | [`.UUID`](<🔩 {.UUID}.md>) | New UUID | `.UUID()` → `<uuid>`
    
    ---
    <br/>
