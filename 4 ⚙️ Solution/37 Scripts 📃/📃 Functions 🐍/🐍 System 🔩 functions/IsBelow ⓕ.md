# 😃ⓕ Talker `.IsBelow` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ

1. **What is the .IsBelow function?**

    `.IsBelow`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns `True` if one input if below the other
    * or `False` otherwise.

    ---
    <br/>


1. **How does .Above comparisons work?**

    | Situation | Behavior | Input 1 | Input 2 | Result 
    |-|-|-|-|-
    | `Num` | Num is math |`1.0` | `5`   | ✅ True
    | `Text` | Check order | `ABC` | `99`  |  ❌ False
    ||                               | `A` | `A` | ❌ False
    ||                               | `XZ` | `ABC` | ✅ True
    | `Empties` | Are ignored | `$empty` | `1` | ❌ False
    | `Lists` | Use [`.Length`](<Length ⓕ.md>) |  `[C]` |`[A,B]` | ✅ True
    | `Others` | Are blocked | `{A:1}` | `{A:2}` | 🚫 Blocked
    | | | `{A:1}` | `1` | 🚫 Blocked

    ---
    <br/>

1. **What's the syntax of .IsBelow?**
    
    ```yaml
    $value1.IsBelow: $value2    
    ```