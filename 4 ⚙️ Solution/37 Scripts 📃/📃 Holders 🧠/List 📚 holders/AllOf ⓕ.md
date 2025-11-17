# 😃🔩 Talker `{.AllOf}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Used by [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)

> Similar to [`.AnyOf`](<AnyOf ⓕ.md>) [`.OneOf`](<OneOf ⓕ.md>)

## FAQ

1. **What is the .AllOf function?**

    `{.AllOf}` 
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns `True` if all of the given assertions return [`.Assert`](<Assert ⓕ.md>)
    * or `False` otherwise.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    .AllOf(assertions...)
    ```
   
    Input | Purpose
    |-|-
    | `assertions...` | [List 🧠](<🧠 List holders.md>) of assertions for [`.Assert`](<Assert ⓕ.md>)


    ---
    <br/>

1. **How to use?**

     ```yaml
    ┌──────────────────────┬──────────────────────┐
    │ With .AllOf          │ Same as              │ 
    ├──────────────────────┼──────────────────────┤
    │ - IF|.AllOf($a, $b): │ - IF|$a:             │
    │     RUN|Something    │    - IF|$b:          │
    │                      │        RUN|Something │
    └──────────────────────┴──────────────────────┘   
    ```

    <br/>