# 1️⃣ ONE prompt


> Part of [blocking input prompts 🤔](<../../🤔⚙️ Prompt features/9 ✏️ as Input.md>)

<br/>

1. **What's a ONE prompt?**

    A `ONE` 
    * is a blocking input [Prompt 🤔](<../../🤔 Prompt.md>) 
    * that allows users to select an option from a list.

    ---
    <br/>



1. **What features does ONE implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../../🤔⚙️ Prompt features/4 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../../🤔⚙️ Prompt features/9 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>



1. **What's the syntax on a [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>)?**

    ```yaml
    # Simplest.
    ONE|<statement>|<options> >> $holder
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<statement>`| Message to show to the user
    | `<options>` | Comma-separated strings, or | `A,B,C`
    || a comma-separated dictionary | `1:A,2:B`
    | `$holder`| Optional selection [holder 🧠](<../../../Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/$Holder 🧠.md>)
    
    ```yaml
    # Comprehensive.
    ONE >> $holder:
        Text: <statement>
        
        # Generic optional properties
        Details: string
        Options: csv|string[]|object
        Nullable: bool
        Appendix: {function}
    ```
    
    | Input| Purpose | Example
    |-|-|-
    | `Details` | Optional [expandable details ⊕](<../../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../../🤔⚙️ Prompt features/4 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Nullable` | Optional [skip flag ⏭️](<../../🤔✏️ Prompt input features/⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | `<uuid>`
    
    
    ---
    <br/>


1. **What's an example of a `ONE` prompt?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Which one?<br/>- Option [A] <br/>- Option [B] | > A
    [🫥 Agent](<../../../../50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) | 🫥 Which one?<br/>- Option [A] <br/>- Option [B] | > A
    | [🤲 Helper](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | 🫥 Which one?<br/>- Option [A] <br/>- Option [B] | > A
    |
   
    <br/>

    Here's the [Script 📃](<../../../Scripts 📃/...commands ⌘/Script 📃/📃 Script.md>).
    
    ```yaml
    📃 Example:
    - ONE|Which one?:
        Options: 
          - Option /A
          - Option /B
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>).

    ```yaml
    Format: ONE
    Emoji: 😃 
    Text: Which one?
    Options: 
        - ID: A
          Title: Option A
        - ID: B
          Title: Option A
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>).

    ```yaml
    Answer: A
    ```

    ---
    <br/>
