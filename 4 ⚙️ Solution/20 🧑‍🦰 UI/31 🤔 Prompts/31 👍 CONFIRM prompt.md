# 👍 CONFIRM prompt

> Part of [blocking input prompts 🤔](<11 ✏️ Input behavior.md>)

<br/>

1. **What's a `CONFIRM` prompt?**

    A `CONFIRM`
    * is a [blocking input prompt 🤔](<11 ✏️ Input behavior.md>)
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
        Then: <true-action>
        Else: <false-action>
    ```
    
    | Argument| Purpose 
    |-|-
    | `<true-action>` | [Procedure ⚙️](<../33 😃 Talkers/11 ⚙️ Procedure.md>) or one-line [Command ⌘](<../33 😃 Talkers/10 ⌘ Command.md>) on `True`
    | `<false-action>`| [Procedure ⚙️](<../33 😃 Talkers/11 ⚙️ Procedure.md>) or one-line [Command ⌘](<../33 😃 Talkers/10 ⌘ Command.md>) on `False`
       
    ---
    <br/>

1. **What's a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) example without actions?**

    > Rejecting this stops the flow.

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Confirm first? | > Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Confirm second? | > No
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | (none)
    |

    <br/>
    

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).

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
    Message: 😃 Confirm first?
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    # Returns: Yes|No|(empty)
    Answer: Yes
    ```

    ---
    <br/>

1. **What's a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) example with actions?**

    > Rejecting this does not block the flow.
    
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Approve the task? | > No
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You rejected the task.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How about the other?
    |

    <br/>

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).

    ```yaml
    # 😃 Talker
    - CONFIRM|Approve the task?:
        Then: INFO|You approved the task.
        Else: INFO|You rejected the task.
    - CONFIRM|How about the other?
    ```

    ---
    <br/>
