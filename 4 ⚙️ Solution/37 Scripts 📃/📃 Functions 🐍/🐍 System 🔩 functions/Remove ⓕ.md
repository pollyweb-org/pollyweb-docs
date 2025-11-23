# 😃🔩 Talker `{.Remove}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Used by [`.Diff`](<Diff ⓕ.md>) [`.Minus`](<Minus ⓕ any.md>)

## FAQ 

1. **What's the behavior of .Remove by type?**

    |Type| Behavior
    |-|-
    | [Texts 🧠](<../../📃 Holders 🧠/Text 📚 holders/🧠 Text holders.md>)| Removes all instances of a substring
    | [Lists 🧠](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>)  | Removes all matching list items
    | [Maps 🧠](<../../📃 Holders 🧠/Map 📚 holders/🧠 Map holders.md>) | Remove a matching property
    
    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    .Remove(from, remove)
    ```

    ---
    <br/>

1. **What are .Remove examples for [Text 🧠 holders](<../../📃 Holders 🧠/Text 📚 holders/🧠 Text holders.md>)?**

    | From | Remove | Output | Explanation
    |-|-|-|-
    | `Banana`| `a` | `Bnn` | `a` was removed
    | `Banana`| `na` | `Ba` | `na` was removed
    | `Banana`| `ta` | `Banana` | `ta` was not found

    ---
    <br>



1. **What are .Remove examples for [List 🧠 holders](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>)?**

    | From | Remove | Output  | Reasons
    |-|-|-|-
    | `B,a,n,n,n,a` | `a` | `B,n,n` | `a` was removed
    | `B,a,n,a,n,a`| `n,a` | `B` | `n` and `a` were removed

    ---
    <br>


1. **What are .Remove examples for [Map 🧠 holders](<../../📃 Holders 🧠/Map 📚 holders/🧠 Map holders.md>)?**

    | From | Remove | Output  | Behavior
    |-|-|-|-
    | `{A:1,B:2}`| `B`| `{A:1}` | Removed property `B` 
    |            | `B:2`| `{A:1}` | Removed `B` with value `2`
    |            | `B:3`| `{A:1,B:2}` | Nothing removed
    | `{A:1,B:2,C:3}`| `A,C`| `{B:2}` | Removed `A` and `C` 

    ---
    <br>
