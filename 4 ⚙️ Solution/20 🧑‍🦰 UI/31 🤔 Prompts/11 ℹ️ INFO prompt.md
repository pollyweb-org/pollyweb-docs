# Non-blocking info ℹ️ ⓘ

> Part of [Non-blocking status prompts 🤔](<08 🤔✨ with Status behavior.md>)

<br/>

1. **What is a non-blocking INFO?**

    An `INFO` 
    * is an informative [Prompt 🤔](<01 🤔 Prompt.md>) 
    * that does not require the user input.

    ---
    <br/>

1. **What features does it implement?**

    | Feature | Details
    |-|-
    | [`Details`](<03 🤔✨ with Details.md>) | Has expandable [+] details.
    | [`Options`](<04 🤔✨ with Options.md>) | Has options for users to select.
    | [`Attachment`](<05 🤔✨ with Attachments.md>) | Has a PDF, PNG, or JPEG attachment.
    | [`Status` behavior](<08 🤔✨ with Status behavior.md>) | Informs and continues the flow.
    
    ---
    <br/>

1. **How do INFO emojis work?**
   
    |Emoji | Details
    |-|-
    ℹ️ | The strong info emoji ℹ️ represents the chat's [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) and any [Helper 🛠️ domains](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) that it may [invite ⏩](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>).
    ⓘ | The faded info emoji ⓘ represents the user's [Agent 🫥 vaults](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>).

    ---
    <br/>



1. **What's an example in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Simple info.
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | ℹ️ Simple info.
    | [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | ⓘ Simple info.
    |
    
    Consider the following [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    INFO|Simple info.
    ```
    
    ---
    <br/>


1. **What's the format for a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    # Inline
    INFO|<message> >> $selected

    # Multi-line 
    INFO >> $selected:
        Message: <message>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<message>` |  Message to show to the user. | `Hi!`
    
    ---
    <br/>

