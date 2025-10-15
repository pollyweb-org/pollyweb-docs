# Non-blocking info ℹ️ ⓘ

> Part of [Non-blocking status prompts 🤔](<../1 📘 Prompt specs/08 ⚠️ as Status.md>)

<br/>

1. **What is a non-blocking INFO?**

    An `INFO` 
    * is an informative [Prompt 🤔](<../../10 📘 Talker specs/20 🤔 Prompt.md>) 
    * that does not require the user input.

    ---
    <br/>

1. **What features does it implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../1 📘 Prompt specs/04 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ⚠️ [`Status`](<../1 📘 Prompt specs/08 ⚠️ as Status.md>) | Informs and continues the flow.
    
    ---
    <br/>

1. **How do INFO emojis work?**
   
    |Emoji | Details
    |-|-
    ℹ️ | The strong info emoji ℹ️ represents the chat's [Host 🤗 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) and any [Helper 🛠️ domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) that it may [invite ⏩](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>).
    ⓘ | The faded info emoji ⓘ represents the user's [Agent 🫥 vaults](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>).

    ---
    <br/>



1. **What's the INFO format for a [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>)?**

    ```yaml
    # Inline
    INFO|<statement> 
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<statement>` |  Message to show to the user. | `Hi!`

    ```yaml
    # Multi-line 
    INFO:
        Statement: <statement>
        
        # Generic optional properties
        Details: string
        Options: csv|string[]|object
        Appendix: {function}
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `Details` | Optional [expandable details ⊕](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../1 📘 Prompt specs/04 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Appendix` | Optional [file attachment 📎](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | `{/...}`
    
    
    
    ---
    <br/>

1. **What's an example in a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)?**

    

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Simple info.
    | [🛠️ Helper](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | ℹ️ Simple info.
    | [🫥 Agent](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | ⓘ Simple info.
    |
    
    <br/>

    Here's the [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    # Talker 😃
    - INFO|Simple info.
    ```
    
    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: INFO
    Statement: ℹ️ Simple info.
    ```

    ---
    <br/>


