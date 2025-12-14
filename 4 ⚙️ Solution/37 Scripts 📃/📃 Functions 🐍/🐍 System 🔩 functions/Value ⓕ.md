# 😃ⓕ Talker `$map.Value` function

> About
* Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
* Works with [`.Key`](<Key ⓕ.md>) [`.Values`](<Values ⓕ.md>)

## FAQ


1. **What is the .Value function?**

    `.Value`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that given a {{Map}} and a key name
    * returns the value associated with that key.

    ---
    <br/>


1. **What's the .Value syntax?**

    ```yaml
    $map.Value: $key
    ```
    
    ---
    <br/>

1. **What are examples of .Value?**

    |Holder|Key|Output
    |-|-|-
    | `{A:1,B:2}`| `A` | `1`
    | `{A:1,B:{C:3,C:4}}`| `B` | `{C:3,C:4}`

    ---
    <br/>