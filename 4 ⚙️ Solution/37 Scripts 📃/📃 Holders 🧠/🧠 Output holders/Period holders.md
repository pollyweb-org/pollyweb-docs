# 🧠 Period holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are Period holders?**

    `Period` holders 
    * are [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) that represent a span of time 
    * i.e., the interval between two [Time 🧠 holders](<../Time 📚 holders/🧠 Time holders.md>)
    * returned by [`.This`](<../Time 📚 holders/This ⓕ.md>), [`.Last`](<../Any 📚 holders/Last ⓕ.md>), [`.Previous`](<../Time 📚 holders/Previous ⓕ.md>), and [`.Diff`](<../Any 📚 holders/Diff ⓕ.md>).

    ---
    <br/>

1. **What functions return periods?**

    |[{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)|Purpose
    |-|-
    |[`.Diff`](<../Any 📚 holders/Diff ⓕ.md>)   | Returns the period between 2 [Time 🧠 holders](<../Time 📚 holders/🧠 Time holders.md>)
    |[`.This`](<../Time 📚 holders/This ⓕ.md>)   | Returns the current named period
    |[`.Last`](<../Any 📚 holders/Last ⓕ.md>)   | Returns the last named period
    |[`.Previous`](<../Time 📚 holders/Previous ⓕ.md>)| Returns the previous named period

    ---
    <br/>

1. **What's the content of a period?**
    
    | Property | Type | Example 
    |-|-|-
    | `Seconds`  | [num](<../Num 📚 holders/🧠 Num holders.md>) |  `264473`
    | `Minutes`  | [num](<../Num 📚 holders/🧠 Num holders.md>) | `123`
    | `Hours`    | [num](<../Num 📚 holders/🧠 Num holders.md>) | `123`
    | `Days`     | [num](<../Num 📚 holders/🧠 Num holders.md>) |  `123`
    | `Months`   | [num](<../Num 📚 holders/🧠 Num holders.md>) | `123`
    | `Years`    | [num](<../Num 📚 holders/🧠 Num holders.md>) | `123345`
    | `Weeks`    | [num](<../Num 📚 holders/🧠 Num holders.md>) | `123`
    | `Time`       | [text](<../Text 📚 holders/🧠 Text holders.md>) | `352h 42m 06s`
    | `Verbose(n)` | [text](<../Text 📚 holders/🧠 Text holders.md>) | `1 month, 3 days, and 6 hours` 
    |
    
    Note: 
    * `Verbose` receives the maximum number or parts.
  
    ---
    <br/>