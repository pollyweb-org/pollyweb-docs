# 😃ⓕ Talker `.Equals` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ

1. **What is the .Equals function?**

    `.Equals`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * similar to [`.Is`](<Is ⓕ.md>) but more strict
    * and the opposite to [`.Differs`](<Differs ⓕ.md>)
    * that returns `True` if two values are the same
    * or `False` otherwise.

    ---
    <br/>


1. **What's the .Equals syntax?**

    ```yaml
    $this.Equals: $that
    ```

    | Inputs | Purpose | Examples
    |-|-|-
    | `$this`  | Base for comparison    | `1` `ABC` `.Today` 
    | `$that`  | Target for comparison | `5` `ABE` `.Now` 

    ---
    <br/>


1. **How do equal comparisons work?**

    Type| Meaning | This | Equals ✅
    |-|-|-|-
    |[Texts 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)| Same spoken words | `a` | `A` 
    |[Nums 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Num holders.md>)|  Same mathematical result | `01`| `1.0` 
    |[Lists 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>)|  Same ordered sequence | `[1,2]` | `[1,2]`
    |[Maps 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)|  Same map despite order | `A:1,B:2` | `B:2,A:1`

    ---
    <br/>


