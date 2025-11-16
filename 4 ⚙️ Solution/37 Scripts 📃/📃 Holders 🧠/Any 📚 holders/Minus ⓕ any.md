# 😃🔩 Talker `{.Minus}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Purpose
* Similar to [`.Add`](<Add ⓕ any.md>), [`.Plus`](<Plus ⓕ any.md>), but for negative values.
* Similar to [`.Diff`](<Diff ⓕ.md>) in some scenarios, for flexibility.

## FAQ 


1. **What's the behavior of .Minus by type?**

    |Type| Behavior
    |-|-
    | [Texts 🧠](<../Text 📚 holders/🧠 Text holders.md>) | Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Remove ⓕ.md>) 
    | [Lists 🧠](<../List 📚 holders/🧠 List holders.md>) | Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Remove ⓕ.md>) 
    | [Maps 🧠](<../Map 📚 holders/🧠 Map holders.md>) | Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Remove ⓕ.md>)
    | [Num 🧠](<../Num 📚 holders/🧠 Num holders.md>) | Same as [`.Sum`](<../Num 📚 holders/Sum ⓕ num.md>) with negative additions
    | [Time 🧠](<../Time 📚 holders/🧠 Time holders.md>) | Same as [`.GoBack`](<../Time 📚 holders/GoBack ⓕ time.md>)
    
    ---
    <br/>

1. **What are examples of .Minus?**

    | Example| Returns | Same as
    |-|-|-
    | `3.Minus(1)`| `2` | `3`[`.Sum`](<../Num 📚 holders/Sum ⓕ num.md>)`(-1)`  | -
    | `ABAC.Minus(A)` | `BC` | `ABCD`[`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Remove ⓕ.md>)`(A)`
    | `[A,B,A,C].Minus(A)` | `[B,C]` | `[A,B,C,D]`[`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Remove ⓕ.md>)`(A)`
    | [`.Today`](<../../📃 Functions 🐍/🐍 System 🔩 functions/time/Today ⓕ.md>)`.Minus(1 month)` | A month ago | [`.Today`](<../../📃 Functions 🐍/🐍 System 🔩 functions/time/Today ⓕ.md>)[`.GoBack`](<../Time 📚 holders/GoBack ⓕ time.md>)`(1 month ago)`
    | [`.Now`](<../../📃 Functions 🐍/🐍 System 🔩 functions/time/Now ⓕ.md>)`.Minus(1 hour)` | An hour ago | [`.Now`](<../../📃 Functions 🐍/🐍 System 🔩 functions/time/Now ⓕ.md>)[`.GoBack`](<../Time 📚 holders/GoBack ⓕ time.md>)`(1 hour ago)`
    |