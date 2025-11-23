# 🧠 Period holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are Period holders?**

    `Period` holders 
    * are [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) that represent a span of time 
    * i.e., the interval between two [Time 🧠 holders](<../🧠 Input holders/🧠 Time holders.md>)
    * returned by [`.This`](<../../📃 Functions 🐍/🐍 System 🔩 functions/This ⓕ.md>), [`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Last ⓕ.md>), [`.Previous`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Previous ⓕ.md>), and [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Diff ⓕ.md>).

    ---
    <br/>

1. **What functions return periods?**

    |[{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)|Purpose
    |-|-
    |[`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Diff ⓕ.md>)   | Returns the period between 2 [Time 🧠 holders](<../🧠 Input holders/🧠 Time holders.md>)
    |[`.This`](<../../📃 Functions 🐍/🐍 System 🔩 functions/This ⓕ.md>)   | Returns the current named period
    |[`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Last ⓕ.md>)   | Returns the last named period
    |[`.Previous`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Previous ⓕ.md>)| Returns the previous named period

    ---
    <br/>

1. **What's the content of a period?**
    
    | Property | Type | Example 
    |-|-|-
    | `Seconds`  | [num](<../🧠 Input holders/🧠 Num holders.md>) |  `264473`
    | `Minutes`  | [num](<../🧠 Input holders/🧠 Num holders.md>) | `123`
    | `Hours`    | [num](<../🧠 Input holders/🧠 Num holders.md>) | `123`
    | `Days`     | [num](<../🧠 Input holders/🧠 Num holders.md>) |  `123`
    | `Months`   | [num](<../🧠 Input holders/🧠 Num holders.md>) | `123`
    | `Years`    | [num](<../🧠 Input holders/🧠 Num holders.md>) | `123345`
    | `Weeks`    | [num](<../🧠 Input holders/🧠 Num holders.md>) | `123`
    | `Time`       | [text](<../🧠 Input holders/🧠 Text holders.md>) | `352h 42m 06s`
    | `Verbose(n)` | [text](<../🧠 Input holders/🧠 Text holders.md>) | `1 month, 3 days, and 6 hours` 
    |
    
    Note: 
    * `Verbose` receives the maximum number or parts.
  
    ---
    <br/>