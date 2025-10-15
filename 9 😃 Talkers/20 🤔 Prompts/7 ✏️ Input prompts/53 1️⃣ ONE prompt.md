# 1️⃣ ONE prompt


> Part of [blocking input prompts 🤔](<../1 📘 Prompt specs/09 ✏️ as Input.md>)

<br/>

1. **What's a ONE prompt?**

    A `ONE` 
    * is a blocking input [Prompt 🤔](<../../10 📘 Talker specs/20 🤔 Prompt.md>) 
    * that allows users to select an option from a list.

    ---
    <br/>



1. **What features does ONE implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | Has expandable [+] details.
    | 🔘 [`Options`](<../1 📘 Prompt specs/04 🔘 with Options.md>) | Has options for users to select.
    | 📎 [`Appendix`](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../1 📘 Prompt specs/09 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>



1. **What's the syntax on a [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>)?**

    ```yaml
    # Simplest.
    ONE|<statement>|<options> >> $placeholder
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<statement>`| Message to show to the user
    | `<options>` | Comma-separated strings, or | `A,B,C`
    || a comma-separated dictionary | `1:A,2:B`
    | `$placeholder`| Optional selection [$placeholder 💾](<../../30 🗃️ Talker data/10 💾 $Placeholder.md>)
    
    ```yaml
    # Comprehensive.
    ONE >> $placeholder:
        Statement: <statement>
        
        # Generic optional properties
        Details: string
        Options: csv|string[]|object
        Nullable: bool
        Appendix: {function}
    ```
    
    | Argument| Purpose | Example
    |-|-|-
    | `Details` | Optional [expandable details ⊕](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | `Hint...`
    | `Options` | Optional [selectable options 🔘](<../1 📘 Prompt specs/04 🔘 with Options.md>) | `A,B` `{A:B}`
    | `Nullable` | Optional [skip flag ⏭️](<../2 ✏️ Input specs/12 ⏭️ Input nullability.md>) | `Yes`
    | `Appendix` | Optional [file attachment 📎](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | `<uuid>`
    
    
    ---
    <br/>


1. **What's an example of a `ONE` prompt?**

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | 😃 Which one?<br/>- Option [A] <br/>- Option [B] | > A
    [🫥 Agent](<../../../4 ⚙️ Solution/50 🫥 Agents/$ 🫥 Agent Vaults/$ 🫥🗄️ Agent vault.md>) | 🫥 Which one?<br/>- Option [A] <br/>- Option [B] | > A
    | [🛠️ Helper](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>) | 🫥 Which one?<br/>- Option [A] <br/>- Option [B] | > A
    |
   
    <br/>

    Here's the [Talker 😃](<../../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    # Talker 😃
    - ONE|Which one?
        Options: 
          - Option [A]
          - Option [B]
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/54 🧑‍🦰🚀🤗 Prompted@Host.md>).

    ```yaml
    Format: ONE
    Statement: 😃 Which one?
    Options: 
        - ID: A
          Translation: Option A
        - ID: B
          Translation: Option A
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🅰️ Host methods/55 🧑‍🦰🐌🤗 Reply@Host.md>).

    ```yaml
    Answer: A
    ```

    ---
    <br/>
