# 😃⤴️ Talker `HTTP` command 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<br/>


1. **What's a HTTP command?**

    A `HTTP` ⤴️
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that raises an HTTP exception
    * and immediately stops the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).


    ---
    <br/>


1. **What's the HTTP syntax?**

    ```yaml
    # On-line syntax
    - HTTP <code>|<message>

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

    Nothing runs on a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) after an `HTTP`.

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ⏳ Waiting forever...
    |
    
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    - TEMP: Waiting forever...
    - RUN: Test 
    - FAIL: This command never runs.
    
    📃 Test:
    - HTTP 500
    - FAIL: This command also never runs.
    ```

    Uses: [`TEMP`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/TEMP ⏳/TEMP ⏳ prompt.md>) [`RUN`](<../RUN 🏃/🏃 RUN ⌘ cmd.md>) [`DONE`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`HTTP`](<💥 HTTP ⌘ cmd.md>)
    
    ---
    <br/>
