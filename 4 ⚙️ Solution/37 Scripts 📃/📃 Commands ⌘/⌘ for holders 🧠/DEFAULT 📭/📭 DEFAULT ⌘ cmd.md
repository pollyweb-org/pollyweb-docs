# 😃📭 Talker `DEFAULT` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<br/>



1. **What's the DEFAULT command?**

    A `DEFAULT`
    * is a handler [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that assigns default values when they are missing
    * by leveraging the [`.Default`](<../../../📃 Functions 🐍/🐍🧠 Holder functions/🔩 {.Default}.md>) function.
  
    ---
    <br/>

1. **What's the syntax for defaults?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Evaluate}.md>) syntax.

    ```yaml
    DEFAULT|$input:
        <property-1>: <default-1>
        <property-n>: <default-n>, <default-m>
    ```
    
    | Input| Purpose | Examples
    |-|-|-
    | `$input`| Initial context | `$.Msg`
    | `<property>` | Property to assign default | `Role` 
    | `<default>` | List of possible default values | `*`
    
    ---
    <br/>

1. **What's an example in a Script?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    
    - DEFAULT|$.Msg:
        Truster: $.Msg.From
        Role: *
    ```

    ---
    <br/>