# 😃🔩 Talker `{.Diff}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ

1. **What is a .Diff command?**

    `{.Diff}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that outputs the difference between [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).

    ---
    <br/>

1. **What's the behavior of .Diff by type?**

    |Type| Behavior
    |-|-
    | [Texts 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>) | Same as [`.Remove`](<Remove ⓕ.md>) 
    | [Lists 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) | Same as [`.Remove`](<Remove ⓕ.md>) 
    | [Maps 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) | Same as [`.Remove`](<Remove ⓕ.md>)
    | [Num 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Num holders.md>) | Returns the distance between numbers
    | [Time 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>) | Returns the [Period 🧠](<../../📃 Holders 🧠/🧠 Output holders/Period holders.md>) between timestamps
    
    ---
    <br/>

1. **What's the .Diff syntax?**

    ```yaml
    .Diff(from, to)
    ```

    | Inputs | Purpose | Examples
    |-|-|-
    | `from`  | Base value    | `1` `ABC` `.Today` 
    | `to`    | Changed value | `5` `ABE` `.Now` 

    ---
    <br/>


1. **What are examples of .Diff output for [Num 🧠 holders](<../../📃 Holders 🧠/Input holders 📥/🧠 Num holders.md>)?**

    |From|To|Result
    |-|-|-
    | `5` | `3` | `-2`
    | `3` | `5` | `2`
    | `-3` | `1` | `4`
    | `1` | `-3` | `-4`
    | `3` | `-5` | `-8`

    ---
    <br/>



1. **What's an example of .Diff for [Time 🧠 holders](<../../📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>)?**

    Here's a [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

    ```yaml
    📃 Example: 
    
    # Process the period
    - CALL|.Diff >> $period
        - .Today 
        - .Now
    
    # Show the total number of seconds since midnight
    - INFO|{$period.Seconds} seconds from midnight:
    ```
    Uses: [`.Today`](<Today ⓕ.md>) [`.Now`](<Now ⓕ.md>) [`INFO`](<../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>