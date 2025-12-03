# 😃🔆 Talker `PARSE` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

> Used by [`Grab@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️📨 Printer msgs/Grab 👥🚀🖨️/🖨️ Grab 🚀 call.md>)

## FAQ

1. **What's the PARSE command?**
   
   `PARSE` 
   * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
   * that parses a [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) with the [`.Locator`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Locator ⓕ.md>) function
   * or a [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) with the [`.Schema`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Schema ⓕ.md>) function.

    ---
    <br/>

1. **What's the PARSE syntax?**

    ```yaml
    PARSE >> $out:
        Locator: $locator
        Schema: $schema
    ```

    | Inputs | Purpose
    |-|-
    | `Locator` | Optional [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) input for [`.Locator`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Locator ⓕ.md>)
    | `Schema`| Optional [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) input for [`.Schema`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Schema ⓕ.md>) 
    | `$out` | [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the answer from the parser function
    |        | Upon multiple inputs, returns a [map](<../../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) of outputs

    ---
    <br/>


1. **How to use the PARSE command?**
    
    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    - PARSE >> $out:
        Locator: .HOST:1.0,any-host.dom,ANY-RESOURCE
    ```

    ---
    <br/>

