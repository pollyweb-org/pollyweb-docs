# 😃🔩 Talker `{.Previous}` function

> Part of [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)


## FAQ

1. **What is the .Previous function?**

    `{.Previous}` 
    * is a [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * similar to [`.This`](<🔩 This.md>)
    * that returns a [Period 🧠 holder](<../../../📃 Holders 🧠/🧠 Output holders/Period holders.md>)
    * representing the previous period relative to [`.Now`](<🔩 Now.md>).


    ---
    <br/>


1. **What't the syntax of .Previous?**

    ```yaml
    .Previous(period)
    ```

    Input | Purpose | Example
    |-|-|-
    |`period` | Textual period | `year`

    ---
    <br/>

1. **What are examples of .Previous for times?**

    Consider [`.Now`](<🔩 Now.md>) as `2025-11-03 13:36`

    | Example | Result
    |-|-
    | `.Previous(hour)` | From `12:00` to `12:59`
    | `.Previous(2 hours)` | From `11:00` to `12:59`
    | `.Previous(day)` | From `00:00` to `23:59` of `Nov 2nd`
    | `.Previous(2 days)` | From `Nov 1` `00:00` to `Nov 2` `23:59`
    | `.Previous(month)` | From `Oct 1` `00:00` to `Oct 31` `23:59`
    | `.Previous(2 months)` | From `Sep 1` `00:00` to `Oct 31` `23:59`
    | `.Previous(quarter)` | From `Jul 1` `00:00` to `Sep 30` `23:59`
    | `.Previous(year)` | From `Jan 1` `00:00` to `Dec 31` `23:59`

    ---
    <br/>


1. **How to use .Previous in Scripts?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) 
    ```yaml
    📃 Example
    - ASSERT:
        - $date.IsIn(.Previous(month))
    ```
    Uses: [`.IsIn`](<../../../📃 Holders 🧠/Any 🧠 holders/IsIn ⓕ any.md>)

    ---
    <br/>

