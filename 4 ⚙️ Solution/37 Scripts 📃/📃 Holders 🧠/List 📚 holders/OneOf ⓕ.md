# 😃🔩 Talker `{.OneOf}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Used by [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)

> Similar to [`.AllOf`](<AllOf ⓕ.md>) [`.AnyOf`](<AnyOf ⓕ.md>)

## FAQ

1. **What is the .OneOf function?**

    `{.OneOf}` 
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns `True` if one (and only one) of the given inputs returns [`.IsNotEmpty`](<../Any 📚 holders/IsNotEmpty ⓕ any.md>)
    * or `False` otherwise.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    .OneOf(assertions...)
    ```
   
    Input | Purpose
    |-|-
    | `assertions...` | [List 🧠](<🧠 List holders.md>) of assertions for [`.Assert`](<Assert ⓕ.md>)


    ---
    <br/>

1. **How to use?**

     ```yaml
    - IF|.OneOf($a, $b):
        RUN|Something  
    ```

    <br/>