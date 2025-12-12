# 👍 CONFIRM prompt

> Part of [blocking input prompts 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>)

## FAQ

1. **What's a `CONFIRM` prompt?**

    A `CONFIRM`
    * is a [blocking input prompt 🤔](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>)
    * that asks a simple `Yes` or `No` to user,
    * typically to progress with a workflow.

    ---
    <br/>

1. **When is `CONFIRM` non-blocking?**

    * When there's a [`THEN`](<../../../📃 Commands ⌘/⌘ for control ▶️/THEN ⤵️/⤵️ THEN ⌘ cmd.md>) or [`ELSE`](<../../../📃 Commands ⌘/⌘ for control ▶️/ELSE ⤵️/⤵️ ELSE ⌘ cmd.md>) right after it,
    * and when the result is sent to a [Placeholder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) using the `>>` syntax.

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
    
        # Generic optional properties
        Emoji: emoji
        Details: string
        Appendix: {...}
    ```
    
    | Input| Purpose | Example
    |-|-|-
    | `Emoji` | Optional [alternative emoji 😶](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/3 ⊕ with Details.md>) | `Hint...`
    | `Appendix` | Optional [file attachment 📎](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/6 📎 with Appendix.md>) | `{/...}`
       
    ---
    <br/>

1. **What's a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) example without actions?**

    > Rejecting this stops the flow.

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Confirm first? | > Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Confirm second? | > No
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | (none)
    |

    <br/>
    

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    # 😃 Talker
    - CONFIRM: Confirm first?
    - CONFIRM: Confirm second?
    - CONFIRM: Confirm third? # Never gets here.
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 call.md>).

    ```yaml
    Format: CONFIRM
    Emoji: 😃 
    Text: Confirm first?
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Reply 🧑‍🦰🐌🤗/🤗 Reply 🐌 msg.md>).

    ```yaml
    # Returns: Yes|No|(empty)
    Answer: Yes
    ```

    ---
    <br/>

1. **What's a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) example with actions?**

    > Rejecting this does not block the flow.
    
    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Approve the task? | > No
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ You rejected the task.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 How about the other?
    |

    <br/>

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    # 😃 Talker
    - CONFIRM: Approve the task?
    - THEN: 
        INFO: You approved the task.
    - ELSE: 
        INFO: You rejected the task.
        
    - CONFIRM: How about the other?
    ```
    Uses: [`THEN`](<../../../📃 Commands ⌘/⌘ for control ▶️/THEN ⤵️/⤵️ THEN ⌘ cmd.md>) [`ELSE`](<../../../📃 Commands ⌘/⌘ for control ▶️/ELSE ⤵️/⤵️ ELSE ⌘ cmd.md>)

    ---
    <br/>
