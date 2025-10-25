# ⭐ RATE prompt

> Part of [blocking input prompts 🤔](<../../🤔⚙️ Prompt features/9 ✏️ as Input.md>)


<br/>

1. **What's a RATE prompt?**

    A `RATE`
    * is a [Prompt 🤔](<../../🤔 Prompt.md>) 
    * that allows ratings of 1 to 5 stars.
  
    ---
    <br/>

1. **What are use cases for RATE?**

    | Scenario | Details
    |-|-
    | `Reviewer` | [Reviewer ⭐](<../../../../50 🫥 Agent domains/Reviewers ⭐/⭐🫥 Reviewer agent.md>)

    ---
    <br/>

1. **What features does RATE implement?**

    | Feature | Details
    |-|-
    | ⊕ [`Details`](<../../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | Has expandable [+] details.
    | 📎 [`Appendix`](<../../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | Has a PDF, PNG, or JPEG attachment.
    | ✏️ [`Input`](<../../🤔⚙️ Prompt features/9 ✏️ as Input.md>) | Waits for an answer from users.
    
    ---
    <br/>


1. **What's the format of a [Talker 😃](<../../../😃 Talkers/😃 Talker role.md>)?**

    ```yaml
    # Simplest.
    RATE|<statement> >> $placeholder
    ```

    | Argument| Purpose 
    |-|-
    | `<statement>`| Message to show to the user
    | `$placeholder`| Optional [placeholder 🧠](<../../../😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) with the user's answer
    

    ```yaml
    # Comprehensive.
    RATE >> $placeholder:
        Statement: <statement>

        # Generic optional properties
        Emoji: emoji
        Details: string
        Nullable: bool
    ```
    
    | Argument| Purpose | Example
    |-|-|-
    | `Emoji` | Optional [alternative emoji 😶](<../../🤔✏️ Prompt input features/😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Nullable` | Optional [skip flag ⏭️](<../../🤔✏️ Prompt input features/⏭️ Input nullability.md>) | `Yes`
    

    ---
    <br/>



1. **What's an example of a [Chat 💬](<../../../💬 Chats/💬 Chat.md>)?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 What's the rate? | ⭐ 5
    [🫥 Agent](<../../../../50 🫥 Agent domains/$ Agent Vaults 🫥/🫥🗄️ Agent vault.md>) | 🫥 What's the code? | ⭐ 4
    | [🤲 Helper](<../../../../45 🤲 Helper domains/$ Helpers 🤲/🤲👥 Helper domain.md>) | 🫥 What's the code? | ⭐ 2
    |

    <br/>
    
    Here's the [Talker 😃](<../../../😃 Talkers/😃 Talker role.md>).
    
    ```yaml
    - RATE|What's the rate? >> $code
    ```


    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>).

    ```yaml
    Format: RATE
    Statement: 😃 What's the rate?
    ```


    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>).

    ```yaml
    Answer: 5
    ```

    ---
    <br/>


