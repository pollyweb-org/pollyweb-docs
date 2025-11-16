# 🧠 Period holders

> Part of [Holders 🧠][Holder]

## FAQ

1. **What are Period holders?**

    `Period` holders 
    * are [Holders 🧠][Holder] that represent a span of time 
    * i.e., the interval between two [Time 🧠 holders][time]
    * returned by [`.This`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.This}.md>), [`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>), [`.Previous`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Previous}.md>), and [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>).

    ---
    <br/>

1. **What functions return periods?**

    |[{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)|Purpose
    |-|-
    |[`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>)   | Returns the period between 2 [Time 🧠 holders][time]
    |[`.This`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.This}.md>)   | Returns the current named period
    |[`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>)   | Returns the last named period
    |[`.Previous`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Previous}.md>)| Returns the previous named period

    ---
    <br/>

1. **What's the content of a period?**
    
    | Property | Type | Example 
    |-|-|-
    | `Seconds`  | [num][num] |  `264473`
    | `Minutes`  | [num][num] | `123`
    | `Hours`    | [num][num] | `123`
    | `Days`     | [num][num] |  `123`
    | `Months`   | [num][num] | `123`
    | `Years`    | [num][num] | `123345`
    | `Weeks`    | [num][num] | `123`
    | `Time`       | [text][text] | `352h 42m 06s`
    | `Verbose(n)` | [text][text] | `1 month, 3 days, and 6 hours` 
    |
    
    Note: 
    * `Verbose` receives the maximum number or parts.
  
    ---
    <br/>

[text]: <../🧠 Input holders/Text holders.md>
[time]: <../🧠 Input holders/Time holders.md>
[Holder]: <../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>
[num]: <../🧠 Input holders/Num holders.md>