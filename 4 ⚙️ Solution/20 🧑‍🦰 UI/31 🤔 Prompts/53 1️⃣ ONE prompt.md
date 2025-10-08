# 1️⃣ ONE prompt


> Part of [blocking input prompts 🤔](<11 ✏️ Input behavior.md>)

<br/>

1. **What's a ONE prompt?**

    A `ONE` 
    * is a blocking input [Prompt 🤔](<01 🤔 Prompt.md>) 
    * that allows users to select an option from a list.

    ---
    <br/>



1. **What features does ONE implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<03 🤔⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<04 🤔🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<05 🤔📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<11 ✏️ Input behavior.md>) | Waits for an answer from users.
    
    ---
    <br/>



1. **What's the syntax on a [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/01 😃 Talker.md>)?**

    ```yaml
    # Simplest.
    ONE|<message>|<options> >> $placeholder
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<message>`| Message to show to the user
    | `<options>` | Comma-separated strings, or | `A,B,C`
    || a comma-separated dictionary | `1:A,2:B`
    | `$placeholder`| Optional selection placeholder
    
    ```yaml
    # Comprehensive.
    ONE >> $placeholder:
        Message: <message>
        
        # Generic optional properties
        Details: string
        Options: csv|string[]|object
        Nullable: bool
        Appendix: {function}
    ```
    
    | Argument| Purpose | Example
    |-|-|-
    | `Details` | Optional [expandable details ⊕](<03 🤔⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<04 🤔🔘 with Options.md>) | `A,B` `{A:B}`
    | `Nullable` | Optional [skip flag ⏭️](<12 ✏️⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<05 🤔📎 with Appendix.md>) | `<uuid>`
    
    
    ---
    <br/>


1. **What's an example of a `ONE` prompt?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Which one?<br/>- Option [A] <br/>- Option [B] | > A
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 Which one?<br/>- Option [A] <br/>- Option [B] | > A
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 Which one?<br/>- Option [A] <br/>- Option [B] | > A
    |
   
    <br/>

    Here's the [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/01 😃 Talker.md>).
    
    ```yaml
    # Talker 😃
    - ONE|Which one?
        Options: 
          - Option [A]
          - Option [B]
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: ONE
    Message: 😃 Which one?
    Options: 
        - ID: A
          Translation: Option A
        - ID: B
          Translation: Option A
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: A
    ```

    ---
    <br/>
