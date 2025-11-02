# 🤔 Prompts with an `Appendix`


> Part of [Prompts 🤔](<../🤔 Prompt.md>)

<br/>

1. **What is a prompt with an attachment?**

    Appendix-enabled prompts 
    * are [Prompts 🤔](<../🤔 Prompt.md>)
    * that contain an Appendix ID
    * to be downloaded with [`Download@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Download 🧑‍🦰🚀🤗/🤗 Download 🚀 request.md>).

    ---
    <br/>

1. **What are usage examples?**

    | Format | Example | 
    |-|-
    | `PDF` | [Show the bill on vending machine payments 🏪](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/11 💧 Buy water.md>)
    | `PNG` | [Show an image of a recovered item in a taxi 🚕](<../../../../3 🤝 Use Cases/03 🧳 Travel/04 🧳 Travel by taxi 🚕/3 🚕 Customer @ Drop-off/31. Recover item.md>)

    ---
    <br/>

1. **How to attach a file?**


    
    Consider the following [Chat 💬](<../../Chats 💬/💬 Chat.md>) as an example.

    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 Who is in the picture? 🖼️ | `Elvis`
    |

    <br/>

    Here's the [Script 📃](<../../Scripts 📃/📃 basics/Script 📃.md>).

    ```yaml
    - TEXT|Who is in the picture?:
        Appendix: {/photos/elvis.png}
    ```

    | [Command ⌘](<../../Scripts 📃/📃 basics/Command ⌘.md>) | Purpose
    |-|-
    | 🔠 [`TEXT`](<../🤔✏️ Prompt inputs/TEXT 🔠/TEXT 🔠 prompt.md>) | To ask a question with an image.
    |
    

    <br/>
    
    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>).

    ```yaml
    Format: TEXT
    Text: 💬 Who is in the picture?
    Appendix: <appendix-uuid>
    ```

    <br/>

    Here's the answer in [`Reply@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>).

    ```yaml
    Answer: Elvis
    ```

    ---
    <br/>
