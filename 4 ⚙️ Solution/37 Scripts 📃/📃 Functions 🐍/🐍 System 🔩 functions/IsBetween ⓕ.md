# 😃ⓕ Talker `{.IsBetween}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ


1. **What is the .IsBetween function?**

    `{.IsBetween}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that verifies if a value is in between two other values.

    ---
    <br/>

1. **What's the .IsBetween syntax?**

    ```yaml
    $value.IsBetween: $lower, $upper
    ```

    | Inputs | Purpose | Examples
    |-|-|-
    | `<value>`  | Value to assess | `1` 
    | `<lower>`  | Lower bound interval | `0` 
    | `<upper>`  | Upper bound interval | `2` 

    ---
    <br/>

1. **What are examples of .IsBetween for math?**

    |Value | Lower | Upper |Result
    |-|-|-|-
    |1 | 0|2 | ✅ True
    |1 | 2|3 | ❌ False
    
    ---
    <br/>


1. **What are examples of .IsBetween for times?**

    |Value | Lower | Upper 
    |-|-|-
    [`.Now`](<Now ⓕ.md>) | `$starts` | `$expires` 
    
    ---
    <br/>
