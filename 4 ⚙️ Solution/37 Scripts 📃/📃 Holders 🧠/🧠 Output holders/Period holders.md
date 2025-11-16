# 🧠 Period holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are Period holders?**

    `Period` holders 
    * are [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) that represent a span of time
    * i.e., the interval between two [Time 🧠 holders](<../🧠 Input holders/Time holders.md>).

    ---
    <br/>

1. **What functions return periods?**

    |[{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)|Purpose
    |-|-
    |[`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>)   | Returns the period between 2 [Time 🧠 holders](<../🧠 Input holders/Time holders.md>)
    |[`.This`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.This}.md>)   | Returns the current named period
    |[`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>)   | Returns the last named period
    |[`.Previous`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Previous}.md>)| Returns the previous named period

    ---
    <br/>

1. **What's the content of a period?**
    
    | Property | Type | Example 
    |-|-|-
    | `Verbose(n)` | {{text}} | `1 month, 3 days, and 6 hours` 
    | `Time`       | {{text}} | `352h 42m 06s`
    | `Seconds`  | int |  `264473`
    | `Minutes`  | int | `123`
    | `Hours`    | int | `123`
    | `Days`     | int |  `123`
    | `Months`   | int | `123`
    | `Years`    | int | `123345`
    | `Weeks`    | int | `123`
    |
    
    Note: 
    * `Verbose` receives the maximum number or parts.
  
    ---
    <br/>