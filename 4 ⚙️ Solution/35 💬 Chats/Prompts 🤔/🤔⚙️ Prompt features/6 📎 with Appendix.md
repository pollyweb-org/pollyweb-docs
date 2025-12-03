# 🤔📎 Prompts with an `Appendix`


> Part of [Prompts 🤔](<../../Chats 💬/🤔 Prompt.md>)

## FAQ

1. **What is a prompt with an attachment?**

    Appendix-enabled prompts 
    * are [Prompts 🤔](<../../Chats 💬/🤔 Prompt.md>)
    * that contain an Appendix ID
    * to be downloaded with [`Download@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Download 🧑‍🦰🚀🤗/🤗 Download 🚀 call.md>).

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

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 💬 Who is in the picture? 🖼️ | `Elvis`
    |

    <br/>

    Here's the [Script 📃](<../../Scripts 📃/Script 📃.md>).

    ```yaml
    - TEXT|Who is in the picture?:
        Appendix: {/photos/elvis.png}
    ```

    | [Command ⌘](<../../Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 🔠 [`TEXT`](<../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>) | To ask a question with an image.
    |
    

    <br/>
    
    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).

    ```yaml
    Format: TEXT
    Text: 💬 Who is in the picture?
    Appendix: <appendix-uuid>
    ```

    <br/>

    Here's the answer in [`Reply@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>).

    ```yaml
    Answer: Elvis
    ```

    ---
    <br/>
