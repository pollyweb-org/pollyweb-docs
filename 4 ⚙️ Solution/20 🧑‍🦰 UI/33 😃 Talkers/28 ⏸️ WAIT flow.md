# ⏸️ Talker `WAIT` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>



1. **What's a WAIT flow command?**

    A `WAIT` ⏸️
    * is a flow [Command ⌘](<10 ⌘ Command.md>) 
    * that pauses the flow for a period of time 
    * or until triggered by an external signal.

    ---
    <br/>


1. **What's the WAIT syntax?**

    
    ```yaml
    # Comprehensive
    - WAIT >> $expired:
        Signal: $signal
        Timeout: <period>
    ```

    | Argument| Purpose
    |-|-
    | `<period>`        | Time before it times out.
    | `$placeholder`   | Signal placeholder to trigger before timeout.
    | `<on-signal>`        | Run [Procedure ⚙️](<11 ⚙️ Procedure.md>) or [Command ⌘](<10 ⌘ Command.md>) when signaled.
    | `<on-timeout>`        | Run [Procedure ⚙️](<11 ⚙️ Procedure.md>) or [Command ⌘](<10 ⌘ Command.md>) when times out.

    ```yaml
    # Simpler
    - WAIT|$signal >> $expired
    ```

    ---
    <br/>

1. **How to build a clock?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🕙 Clock | ⏳ It's 17:01
    | 🕙 Clock | ⏳ It's 17:02

    ```yaml
    # 😃 Talker 
    💬 Clock:
    - TEMP|It's {.Time(HH:MM:SS)}
    - WAIT|00:00:01 
    - REPEAT
    ```
    

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | ⏳ [`TEMP`](<../31 🤔 Prompts/25 ⏳ TEMP prompt.md>) | Show the temporary message.
    | 🔁 [`REPEAT`](<23 🔁 REPEAT flow.md>) | To update the message.

    ---
    <br/>


1. **How to wait in a queue?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🏦 Bank | ⏳ There are 21 people ahead of you.
    | 🏦 Bank | ⏳ There are 7 people ahead of you.
    | 🏦 Bank | ⏳ You're next, get ready!
    | 🏦 Bank | 💬 What do you need? | `I need...`
    |

    Here's the [Talker 😃](<01 😃 Talker.md>).

    ```yaml
    # 😃 Talker 

    💬 Check-in:
    - RUN|WaitInLine
    - TEXT|What do you need?

    WaitInLine:

    # Check the status of the queue.
    - EVAL|{queue-length} >> $len

    # Show the status in a human-friendly wait.
    - CASE|{$len}:
        $: TEMP|There are {$len} people ahead of you.
        1: TEMP|You're next, get ready!
        0: RETURN
    
    # Wait 1 minute or until signalled.
    - WAIT:
        Signal: $your-turn
        Period: 00:01:00

    # Jump off if signalled.
    - IF|$your-turn:
        Then: RETURN

    # Check the queue length again.
    - REPEAT
    ```

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | ▶️ [`RUN`](<24 ▶️ RUN flow.md>) | To start the waiting loop.
    | ⬇️ [`EVAL`](<20 ⬇️ EVAL flow.md>) | to assess the backend queue length.
    | 🔀 [`CASE`](<22 🔀 CASE flow.md>) | To show the human-friendly message.
    | 🔁 [`RETURN`](<23 🔁 REPEAT flow.md>) | To exit the loop when it's the user's turn.
    | 🔁 [`REPEAT`](<23 🔁 REPEAT flow.md>) | To re-assess the queue periodically.

    ---
    <br/>


1. **How to wait for a task to complete?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🍕 Pizza | ℹ️ Order submitted 
    | 🍕 Pizza | ⏳ Step `1/3` Order in the queue...
    | 🍕 Pizza | ⏳ Step `2/3` Order being cooked...
    | 🍕 Pizza | ⏳ Step `3/3` Just finishing up...
    | 🍕 Pizza | ✅ Order ready!
    |

    Here's the [Talker 😃](<01 😃 Talker.md>).

    ```yaml
    # 😃 Talker 

    💬 Test:
    - EVAL|{Submit} >> $status:  # Send
    - INFO|Order submitted       # Inform sent
    - RUN|WaitForReady           # Wait...
    - SUCCESS|Order ready!       # Inform ready

    WaitForReady:
    - TEMP|$status.Message       # Show temp...
    - WAIT|$status               # Wait
    - IF|$status.Ready:          # Signalled
        Then: RETURN             # End if ready
    - REPEAT
    ```

    ---
    <br/>


1. **How to signal a WAIT placeholder?**

    Consider the following `WAIT` command.

    ```yaml
    # 😃 Talker 
    - WAIT|24:00:00|$for-something:
        OnSignal: SUCCESS|Signalled!
        OnTimeout: FAILURE|Timed out!
    ```

    <!-- 
    TODO: Add HOSTER.Signal() documentation.
    -->

    To trigger it, a developer needs to invoke the [Hoster ☁️ helper](<../35 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>) SDK.

    ```python
    # 🐍 Python
    def talkerHandler(args):
        HOSTER.Signal({
            Signal: 'for-something',
            ChatID: '<chat-uuid>',
            Broker: 'any-broker.com'
        })
    ```    

    ---
    <br/>