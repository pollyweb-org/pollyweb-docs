# 👍 CONFIRM prompt

> Part of [blocking input prompts 🤔](<../../🤔⚙️ Prompt features/9 ✏️ as Input.md>)

<br/>

1. **What's a `CONFIRM` prompt?**

    A `CONFIRM`
    * is a [blocking input prompt 🤔](<../../🤔⚙️ Prompt features/9 ✏️ as Input.md>)
    * that asks a simple `Yes` or `No` to user,
    * typically to progress with a workflow.

    ---
    <br/>

1. **What's the syntax of a `CONFIRM`?**

    ```yaml
    # Simplest
    CONFIRM|<text>
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<text>` |  Message to show to the user. | `Sure?`

    ```yaml
    # Comprehensive
    CONFIRM:
        Text: <text>
        
        # Specific optional properties
        Then: Script|Command
        Else: Script|Command

        # Generic optional properties
        Emoji: emoji
        Details: string
        Appendix: {function}
    ```
    
    | Input| Purpose | Example
    |-|-|-
    | `Then` | [Script 📃](<../../../Scripts 📃/📃 basics/Script 📃.md>) or [Command ⌘](<../../../Scripts 📃/📃 basics/Command ⌘.md>) on `True` | `INFO\|OK`
    | `Else` | [Script 📃](<../../../Scripts 📃/📃 basics/Script 📃.md>) or [Command ⌘](<../../../Scripts 📃/📃 basics/Command ⌘.md>) on `False` | `INFO\|NOK`
    | `Emoji` | Optional [alternative emoji 😶](<../../🤔✏️ Prompt input features/😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../../🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Appendix` | Optional [file attachment 📎](<../../🤔⚙️ Prompt features/5 📎 with Appendix.md>) | `{/...}`
       
    ---
    <br/>

1. **What's a [Chat 💬](<../../../Chats 💬/💬 Chat.md>) example without actions?**

    > Rejecting this stops the flow.

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Confirm first? | > Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Confirm second? | > No
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | (none)
    |

    <br/>
    

    Here's the [Script 📃](<../../../Scripts 📃/📃 basics/Script 📃.md>).

    ```yaml
    # 😃 Talker
    - CONFIRM|Confirm first?
    - CONFIRM|Confirm second?
    - CONFIRM|Confirm third? # Never gets here.
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>).

    ```yaml
    Format: CONFIRM
    Emoji: 😃 
    Text: Confirm first?
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>).

    ```yaml
    # Returns: Yes|No|(empty)
    Answer: Yes
    ```

    ---
    <br/>

1. **What's a [Chat 💬](<../../../Chats 💬/💬 Chat.md>) example with actions?**

    > Rejecting this does not block the flow.
    
    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Approve the task? | > No
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ You rejected the task.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 How about the other?
    |

    <br/>

    Here's the [Script 📃](<../../../Scripts 📃/📃 basics/Script 📃.md>).

    ```yaml
    # 😃 Talker
    - CONFIRM|Approve the task?:
        Then: INFO|You approved the task.
        Else: INFO|You rejected the task.
    - CONFIRM|How about the other?
    ```

    ---
    <br/>
