# 🤔 Prompts with an `Appendix`


> Part of [Prompts 🤔](<../🤔 Prompt.md>)

<br/>

1. **What is a prompt with an attachment?**

    Appendix-enabled prompts 
    * are [Prompts 🤔](<../🤔 Prompt.md>)
    * that contain an Appendix ID
    * to be downloaded with [`Download@Host`](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Download.md>).

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


    
    Consider the following [Chat 💬](<../../12 💬 Chats/💬 Chat.md>) as an example.

    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | 💬 Who is in the picture? 🖼️ | `Elvis`
    |

    <br/>

    Here's the [Talker 😃](<../../../../9 😃 Talkers/10 😃 Talker.md>).

    ```yaml
    - TEXT|Who is in the picture?:
        Appendix: {/photos/elvis.png}
    ```

    | [Command ⌘](<../../../../9 😃 Talkers/😃🌊 Talker flow/10 ⌘ Command.md>) | Purpose
    |-|-
    | 🔠 [`TEXT`](<../7 ✏️ Input prompts/32 🔠 TEXT prompt.md>) | To ask a question with an image.
    

    <br/>
    
    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: TEXT
    Statement: 💬 Who is in the picture?
    Appendix: <appendix-uuid>
    ```

    <br/>

    Here's the answer in [`Reply@Host`](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: Elvis
    ```

    ---
    <br/>
