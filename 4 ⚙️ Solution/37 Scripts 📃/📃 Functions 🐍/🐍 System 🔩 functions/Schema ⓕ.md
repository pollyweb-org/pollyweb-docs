# 😃ⓕ Talker `.Schema` function

> About
* Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
* Used by [`.Is`](<Is ⓕ.md>) [`.IsNot`](<IsNot ⓕ.md>)

## FAQ 

1. **What is the .Schema function?**

    `.Schema` 
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that parses a [Schema Code 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>).

    ---
    <br/>

1. **What is the .Schema syntax?**

    ```yaml
    $code.Schema
    ```
    | Input | Purpose | Examples
    |-|-|-
    | `$code` | [Schema Code 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | `.HOST` `any.dom/ANY/CODE:1.2`

    ---
    <br/>

1. **What's the output of the schema function?**

    The output is a [Map 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) with the following fields:

    ```yaml
    Authority: any-authority.dom
    Path: ANY/PATH
    Version: 1.0
    ```

    | Field | Type | Description
    |-| -|-
    | `Authority` | text | [Authority 🏛️ domain](<../../../45 🤲 Helper domains/Authorities 🏛️/🏛️🤲 Authority helper.md>) that set the [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
    | `Path` | text | [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) path in the [Authority 🏛️ domain](<../../../45 🤲 Helper domains/Authorities 🏛️/🏛️🤲 Authority helper.md>)
    | `Version` | text | [Schema 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) version 

    ---
    <br/>