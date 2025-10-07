# 🤔 Prompts with an `Attachment`


> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

<br/>

1. **What is a prompt with an attachment?**

    Attachment-enabled prompts 
    * are [Prompts 🤔](<01 🤔 Prompt.md>)
    * that contain an Attachment ID
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


    
    Consider the following [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) as an example.

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 💬 Who is in the picture? 🖼️ | `Elvis`
    |

    The related [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) would be.

    ```yaml
    TEXT|Who is in the picture?:
        Attachment: {/photos/elvis.png}
    ```
    
    The [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method would be.

    ```yaml
    Format: TEXT
    Message: Who is in the picture?
    Attachment: <attachment-uuid>
    ```

    ---
    <br/>
