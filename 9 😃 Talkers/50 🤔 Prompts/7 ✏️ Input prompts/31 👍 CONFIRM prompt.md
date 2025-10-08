# 👍 CONFIRM prompt

> Part of [blocking input prompts 🤔](<../1 📘 Prompt specs/09 ✏️ as Input.md>)

<br/>

1. **What's a `CONFIRM` prompt?**

    A `CONFIRM`
    * is a [blocking input prompt 🤔](<../1 📘 Prompt specs/09 ✏️ as Input.md>)
    * that asks a simple `Yes` or `No` to user,
    * typically to progress with a workflow.

    ---
    <br/>

1. **What's the syntax of a `CONFIRM`?**

    ```yaml
    # Simplest
    CONFIRM|<message>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<message>` |  Message to show to the user. | `Sure?`

    ```yaml
    # Comprehensive
    CONFIRM:
        Message: <message>
        
        # Specific optional properties
        Then: Procedure|Command
        Else: Procedure|Command

        # Generic optional properties
        Emoji: emoji
        Details: string
        Appendix: {function}
    ```
    
    | Argument| Purpose | Example
    |-|-|-
    | `Then` | [Procedure ⚙️](<../../../9 😃 Talkers/20 🌊 Talker flows/11 ⚙️ Procedure.md>) or [Command ⌘](<../../../9 😃 Talkers/20 🌊 Talker flows/10 ⌘ Command.md>) on `True` | `INFO\|OK`
    | `Else` | [Procedure ⚙️](<../../../9 😃 Talkers/20 🌊 Talker flows/11 ⚙️ Procedure.md>) or [Command ⌘](<../../../9 😃 Talkers/20 🌊 Talker flows/10 ⌘ Command.md>) on `False` | `INFO\|NOK`
    | `Emoji` | Optional [alternative emoji 😶](<../2 ✏️ Input specs/14 😶 Input emojis.md>) | `😶`
    | `Details` | Optional [expandable details ⊕](<../1 📘 Prompt specs/03 ⊕ with Details.md>) | `Hint...`
    | `Appendix` | Optional [file attachment 📎](<../1 📘 Prompt specs/05 📎 with Appendix.md>) | `{/...}`
       
    ---
    <br/>

1. **What's a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) example without actions?**

    > Rejecting this stops the flow.

    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../1 📘 Prompt specs/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Confirm first? | > Yes
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Confirm second? | > No
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | (none)
    |

    <br/>
    

    Here's the [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/01 😃 Talker.md>).

    ```yaml
    # 😃 Talker
    - CONFIRM|Confirm first?
    - CONFIRM|Confirm second?
    - CONFIRM|Confirm third? # Never gets here.
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: CONFIRM
    Statement: 😃 Confirm first?
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    # Returns: Yes|No|(empty)
    Answer: Yes
    ```

    ---
    <br/>

1. **What's a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) example with actions?**

    > Rejecting this does not block the flow.
    
    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../1 📘 Prompt specs/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Approve the task? | > No
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You rejected the task.
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How about the other?
    |

    <br/>

    Here's the [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/01 😃 Talker.md>).

    ```yaml
    # 😃 Talker
    - CONFIRM|Approve the task?:
        Then: INFO|You approved the task.
        Else: INFO|You rejected the task.
    - CONFIRM|How about the other?
    ```

    ---
    <br/>
