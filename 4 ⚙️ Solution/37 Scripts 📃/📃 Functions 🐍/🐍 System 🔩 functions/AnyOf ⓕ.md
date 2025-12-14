# 😃ⓕ Talker `{.AnyOf}` function

> About
* Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
* Used by [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)
* Similar to [`.AllOf`](<AllOf ⓕ.md>) [`.OneOf`](<OneOf ⓕ.md>)

## FAQ

1. **What is the .AnyOf function?**

    `{.AnyOf}` 
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns `True` if any of the given assertion returns [`.Assert`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>)
    * or `False` otherwise.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    # Without context
    .AnyOf: [assertions...]
    ```

    ```yaml
    # With context
    $context.AnyOf: [assertions...]
    ```

    Input | Purpose
    |-|-
    | `assertions...` | [List 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) of assertions for [`.Assert`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>)
   
    ---
    <br/>

1. **How to use?**

     ```r
    ┌──────────────────────┬──────────────────────┐
    │ With .AnyOf          │ Same as              │ 
    ├──────────────────────┼──────────────────────┤
    │ - IF .AnyOf($a, $b): │ - IF $a:             │
    │     RUN Something    │     RUN Something    │
    │                      │ - IF $b:             │
    │                      │     RUN Something    │
    └──────────────────────┴──────────────────────┘   
    ```

    ---
    <br/>