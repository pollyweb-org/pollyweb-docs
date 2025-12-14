# 😃ⓕ Talker `{.Differs}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ

1. **What is the .Differs function?**

    `{.Differs}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns the opposite to [`.Equals`](<Equals ⓕ.md>).

    ---
    <br/>


1. **What's the .Differs syntax?**

    ```yaml
    $this.Differs: $that
    ```

    | Inputs | Purpose | Examples
    |-|-|-
    | `$this`  | Base for comparison    | `1` `ABC` `.Today` 
    | `$that`  | Target for comparison | `5` `ABE` `.Now` 

    ---
    <br/>




1. **How do unequal comparisons work?**
   
    |Type| Meaning | This | Differs ✅
    |-|-|-|-
    |[Text 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| Different meaning | `a`|`b`  
    |[Num 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Num holders.md>)| Different math results| `1` | `1.1`
    |[List 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>)| Different sequence | `[1,3,2]` | `[1,2,3]`
    |[Map 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)| Different pair content | `{A:2}` | `{A:1}`
    
    ---
    <br/>
