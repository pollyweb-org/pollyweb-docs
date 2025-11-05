<!-- TODO: -->

# 🐍 {/file} function

> Part of [{Functions} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

<br/>

1. **What's syntax for files?**

    ```yaml
    # Static paths
    {/path/to/file} 

    # Dynamic paths
    {/{function}}
    ```

    | Input| Purpose
    |-|-
    | `/path/to/file` | Path to a file in the [Hoster ☁️](<../../../45 🤲 Helper domains/Hosters ☁️/☁️🤲 Hoster helper.md>) folders.
    | `{function}` | Function that evaluates to a path.

    ---
    <br/>
   

1. **What's an example for files?**


    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Prompts 🤔/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 [Who is in the picture?](<../../📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>) 🖼️ | `Elvis`


    ```yaml
    # 😃 Talker configuration
    💬 Example:
    TEXT|Who is in the picture?:
        Appendix: {/photos/elvis.png}
    ```
    
    Commands: [`TEXT`](<../../📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>)

    ---
    <br/>