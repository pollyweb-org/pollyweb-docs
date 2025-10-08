# 🤔 Prompts with an `Appendix`


> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

<br/>

1. **What is a prompt with an attachment?**

    Appendix-enabled prompts 
    * are [Prompts 🤔](<01 🤔 Prompt.md>)
    * that contain an Appendix ID
    * to be downloaded with [`Download@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/06 🧑‍🦰🚀🤗 Download.md>).

    ---
    <br/>

1. **What are usage examples?**

    | Format | Example | 
    |-|-
    | `PDF` | [Show the bill on vending machine payments 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    | `PNG` | [Show an image of a recovered item in a taxi 🚕](<../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/31. Recover item.md>)

    ---
    <br/>

1. **How to attach a file?**


    
    Consider the following [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) as an example.

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 💬 Who is in the picture? 🖼️ | `Elvis`
    |

    <br/>

    Here's the [Talker 😃](<../../10 📘 Talker specs/01 😃 Talker.md>).

    ```yaml
    - TEXT|Who is in the picture?:
        Appendix: {/photos/elvis.png}
    ```

    | [Command ⌘](<../../20 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
    |-|-
    | 🔠 [`TEXT`](<../7 ✏️ Input prompts/32 🔠 TEXT prompt.md>) | To ask a question with an image.
    

    <br/>
    
    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: TEXT
    Message: 💬 Who is in the picture?
    Appendix: <appendix-uuid>
    ```

    <br/>

    Here's the answer in [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: Elvis
    ```

    ---
    <br/>
