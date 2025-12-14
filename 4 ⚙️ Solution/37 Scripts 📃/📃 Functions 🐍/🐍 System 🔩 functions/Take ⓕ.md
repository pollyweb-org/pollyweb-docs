# 😃ⓕ Talker `.Take` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)


## FAQ


1. **What's the behavior of .Take?**

    Type| Behavior
    |-|-
    | [Lists 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) | Same as [`.First`](<First ⓕ.md>)
    | [Texts 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>) | Same as [`.First`](<First ⓕ.md>)
    | [Nums 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Num holders.md>) | Same as [`.Calculate`](<Calculate ⓕ.md>)


    ---
    <br/>


1. **What's the .Take syntax?**

    ```yaml
    $source.Take: $dimension
    ```

    Inputs|Details | Example
    |-|-|-|
    |`source`| [List 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) of values | `[1,2,3]`
    |       | or [List 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) of [Maps 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) | `{A:1},{A:2}`
    |       | or [Text 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>) | `ABC`
    |       | or [Num 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Num holders.md>) | `123`
    |`dimension`| Number of items | `2`
    |           | or mathematical formula | `2x`
    

    ---
    <br/>

