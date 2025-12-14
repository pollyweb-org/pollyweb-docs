# 😃ⓕ Talker `{.OneOf}` function

> About
* Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
* Used by [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)
* Similar to [`.AllOf`](<AllOf ⓕ.md>) [`.AnyOf`](<AnyOf ⓕ.md>)

## FAQ

1. **What is the .OneOf function?**

    `{.OneOf}` 
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns `True` if one (and only one) of the given inputs returns [`.IsNotEmpty`](<IsNotEmpty ⓕ.md>)
    * or `False` otherwise.

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    # Without context
    .OneOf: [assertions...]
    ```

    ```yaml
    # With context
    $context.OneOf: [assertions...]
    ```
   
    Input | Purpose
    |-|-
    | `assertions...` | [List 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) of assertions for [`.Assert`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>)


    ---
    <br/>

1. **How to use?**

     ```yaml
    - IF:
        .OneOf: $a, $b
    - THEN:
        RUN: Something  
    ```
    Uses: [`IF`](<../../📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RUN`](<../../📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`THEN`](<../../📃 Commands ⌘/⌘ for control ▶️/THEN ⤵️/⤵️ THEN ⌘ cmd.md>)

    <br/>