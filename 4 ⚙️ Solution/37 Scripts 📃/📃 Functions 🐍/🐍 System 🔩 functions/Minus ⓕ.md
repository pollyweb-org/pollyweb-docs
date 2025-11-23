# 😃🔩 Talker `{.Minus}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Purpose
* Similar to [`.Add`](<Add ⓕ.md>), [`.Plus`](<Plus ⓕ.md>), but for negative values.
* Similar to [`.Diff`](<Diff ⓕ.md>) in some scenarios, for flexibility.

## FAQ 


1. **What's the behavior of .Minus by type?**

    |Type| Behavior
    |-|-
    | [Texts 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>) | Same as [`.Remove`](<Remove ⓕ.md>) 
    | [Lists 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) | Same as [`.Remove`](<Remove ⓕ.md>) 
    | [Maps 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) | Same as [`.Remove`](<Remove ⓕ.md>)
    | [Num 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Num holders.md>) | Same as [`.Sum`](<Sum ⓕ num.md>) with negative additions
    | [Time 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>) | Same as [`.GoBack`](<GoBack ⓕ time.md>)
    
    ---
    <br/>

1. **What are examples of .Minus?**

    | Example| Returns | Same as
    |-|-|-
    | `3.Minus(1)`| `2` | `3`[`.Sum`](<Sum ⓕ num.md>)`(-1)`  | -
    | `ABAC.Minus(A)` | `BC` | `ABCD`[`.Remove`](<Remove ⓕ.md>)`(A)`
    | `[A,B,A,C].Minus(A)` | `[B,C]` | `[A,B,C,D]`[`.Remove`](<Remove ⓕ.md>)`(A)`
    | [`.Today`](<Today ⓕ.md>)`.Minus(1 month)` | A month ago | [`.Today`](<Today ⓕ.md>)[`.GoBack`](<GoBack ⓕ time.md>)`(1 month ago)`
    | [`.Now`](<Now ⓕ.md>)`.Minus(1 hour)` | An hour ago | [`.Now`](<Now ⓕ.md>)[`.GoBack`](<GoBack ⓕ time.md>)`(1 hour ago)`
    |