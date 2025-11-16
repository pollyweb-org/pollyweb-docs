# 😃🔩 Talker `{.Plus}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Purpose
* Alternative to [`.Add`](<any.Add 🔩 ext.md>), for flexibility.

## FAQ

1. **What's the behavior of .Plus?**

    |Type|Behavior
    |-|-
    |[Num 🧠](<../🧠🔩 Num holders/Num holders.md>) | Same as [`.Sum`](<../🧠🔩 Num holders/num.Sum 🔩 ext.md>)
    |[Time 🧠](<../🧠🔩 Time holders/Time holders.md>) | Same as [`.Advance`](<../🧠🔩 Time holders/time.Advance2 🔩 ext.md>)

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    .Plus(original, additional)
    ```

    Input|Purpose|Example
    |-|-|-
    | `original` | Original [Num 🧠 holder](<../🧠🔩 Num holders/Num holders.md>) | `9`
    |           | Original [Time 🧠 holder](<../🧠🔩 Time holders/Time holders.md>) | `.Now`
    | `additional` | Number(s) for [`.Sum`](<../🧠🔩 Num holders/num.Sum 🔩 ext.md>) | `1` `1,2,3`
    |              | Period for [`.Advance`](<../🧠🔩 Time holders/time.Advance2 🔩 ext.md>) | `1 day` 
    
    ---
    <br/>
