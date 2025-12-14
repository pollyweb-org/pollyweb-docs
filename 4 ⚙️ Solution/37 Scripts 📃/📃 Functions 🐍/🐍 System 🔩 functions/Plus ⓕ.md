# 😃ⓕ Talker `.Plus` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Purpose
* Alternative to [`.Add`](<Add ⓕ.md>), for flexibility.

## FAQ

1. **What's the behavior of .Plus?**

    |Type|Behavior
    |-|-
    |[Num 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Num holders.md>) | Same as [`.Sum`](<Sum ⓕ.md>)
    |[Time 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>) | Same as [`.Advance`](<Advance ⓕ.md>)

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    $original.Plus: <additional>
    ```

    Input|Purpose|Example
    |-|-|-
    | `original` | Original [Num 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Num holders.md>) | `9`
    |           | Original [Time 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>) | `.Now`
    | `additional` | Number(s) for [`.Sum`](<Sum ⓕ.md>) | `1` `1,2,3`
    |              | Period for [`.Advance`](<Advance ⓕ.md>) | `1 day` 
    
    ---
    <br/>
