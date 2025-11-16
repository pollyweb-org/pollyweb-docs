# 😃🔩 Talker `{.Assert}` function

> Part of [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Used by [`.AllOf`](<AllOf ⓕ.md>) [`.AnyOf`](<AnyOf ⓕ.md>) [`.OneOf`](<OneOf ⓕ.md>)

## FAQ

1. **What is the .Assert function?**

    `{.Assert}`
    * is a [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that evaluates an assertion on a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).
    
    ---
    <br/>


1. **What's the .Assert syntax?**

    ```yaml
    .Assert(assertion)
    ```
    
    Input|Purpose|Example
    |-|-|-
    |`assertion`| Assertion to assert | `$h.Is(7)`

    ---
    <br/>

1. **What's the behavior of .Assert?**

    |Assertion|Example|Behavior
    |-|-|-
    |[`$holder`](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | `$h` | Returns [`.IsNotEmpty`](<../../../📃 Holders 🧠/Any 📚 holders/IsNotEmpty ⓕ any.md>)
    |[`.Function`](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)`(`[`$holder`](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)`)`| `.Is($h,7)` | Returns the function result
    | [`$holder`](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)`.`[`Function`](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | `$h.Is(7)` | Returns `False` if [`.IsEmpty`](<../../../📃 Holders 🧠/Any 📚 holders/IsEmpty ⓕ any.md>)
    ||| Otherwise the [function](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) result 
    | [`$holder`](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)`: <value>` | `$h: 7`| Same as `$h`[`.Is`](<../../../📃 Holders 🧠/Any 📚 holders/Is ⓕ any.md>)`(<value>)`
    
    ---
    <br/>

1. **What are examples of .Assert?**

    Consider the following [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).

    |[Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | Content
    |-|-
    | $emp | empty
    | $txt | `A`
    |
    
    Here are a few results.

    | Result | Input 
    |-|-|
    |  ✅ True | `$txt` `$txt:A` `$txt.Is(A)`   `.Is($txt, A)` `$emp.IsEmpty`
    |  ❌ False | `$emp` `$emp:A`  `$emp.Is(A)` `$emp.IsNot(A)` `.Is($emp, A)` 
    |