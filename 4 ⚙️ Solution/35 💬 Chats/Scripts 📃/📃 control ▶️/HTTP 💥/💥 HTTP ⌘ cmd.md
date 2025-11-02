# 😃⤴️ Talker `HTTP` command 

> Part of [Script 📃](<../../📃 basics/Script 📃.md>)

<br/>


1. **What's a HTTP command?**

    A `HTTP` ⤴️
    * is a flow [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * that raises an HTTP exception
    * and immediately stops the [Script 📃](<../../📃 basics/Script 📃.md>).


    ---
    <br/>


1. **What's the HTTP syntax?**

    ```yaml
    # On-line syntax
    - HTTP|<code>|<message>

    # Multi-line syntax
    - HTTP:
        Code: <code>
        Message: <message>
    ```

    | Input| Purpose | Example
    |-|-|-
    | `Code`| HTTP error code | `403`
    | `Message` | Optional details about the error | `MyError`
    
    ---
    <br/>



1. **What happens after a HTTP?**

    Nothing runs on a [Script 📃](<../../📃 basics/Script 📃.md>) after an `HTTP`.

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ⏳ Waiting forever...
    |
    
    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

    ```yaml
    📃 Example:
    - TEMP|Waiting forever...
    - RUN|Test 
    - FAILURE|This command never runs.
    
    📃 Test:
    - HTTP|500
    - FAILURE|This command also never runs.
    ```

    Commands: [`TEMP`](<../../../Prompts 🤔/🤔📢 Prompt status/TEMP ⏳/TEMP ⏳ prompt.md>) [`RUN`](<../RUN ▶️/▶️ RUN ⌘ cmd.md>) [`SUCCESS`](<../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)
    
    ---
    <br/>
