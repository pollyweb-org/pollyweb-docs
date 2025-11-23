# 😃🔩 Talker `{.Plus}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Purpose
* Alternative to [`.Add`](<Add ⓕ any.md>), for flexibility.

## FAQ

1. **What's the behavior of .Plus?**

    |Type|Behavior
    |-|-
    |[Num 🧠](<../../📃 Holders 🧠/Num 📚 holders/🧠 Num holders.md>) | Same as [`.Sum`](<../../📃 Holders 🧠/Num 📚 holders/Sum ⓕ num.md>)
    |[Time 🧠](<../../📃 Holders 🧠/Time 📚 holders/🧠 Time holders.md>) | Same as [`.Advance`](<../../📃 Holders 🧠/Time 📚 holders/Advance ⓕ time.md>)

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    .Plus(original, additional)
    ```

    Input|Purpose|Example
    |-|-|-
    | `original` | Original [Num 🧠 holder](<../../📃 Holders 🧠/Num 📚 holders/🧠 Num holders.md>) | `9`
    |           | Original [Time 🧠 holder](<../../📃 Holders 🧠/Time 📚 holders/🧠 Time holders.md>) | `.Now`
    | `additional` | Number(s) for [`.Sum`](<../../📃 Holders 🧠/Num 📚 holders/Sum ⓕ num.md>) | `1` `1,2,3`
    |              | Period for [`.Advance`](<../../📃 Holders 🧠/Time 📚 holders/Advance ⓕ time.md>) | `1 day` 
    
    ---
    <br/>
