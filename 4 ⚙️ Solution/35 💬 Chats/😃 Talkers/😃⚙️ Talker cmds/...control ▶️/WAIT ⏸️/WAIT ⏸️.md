# 😃⏸️ Talker `WAIT` flow 

> Part of [Talker 😃](<../../../😃 Talker role.md>)

> Referenced by the [😃⏩🧑‍💻 Wait ⏸️](<../../../😃⏩ Talker flows/😃⏩🧑‍💻 Wait ⏸️.md>) flow

<br/>



1. **What's a WAIT flow command?**

    A [`WAIT` ⏸️](<WAIT ⏸️.md>)
    * is a flow [Command ⌘](<../../...commands ⌘/⌘ Command.md>) 
    * that pauses the flow for a period of time 
    * or until triggered by an external signal.

    ---
    <br/>


1. **What's the WAIT syntax?**

    
    ```yaml
    # Listen to two triggers in parallel: 
    #   placeholder change and timeout.

    - WAIT >> $expired:
        Signal: $signal
        Timeout: <period>
    ```

    | Argument| Purpose
    |-|-
    | `$expired` | Boolean return if the wait has time out.
    | `Signal`   | Placeholder that stops the wait if changed.
    | `Timeout`  | Time to wait, evaluated by the [`.Add`](<../../...functions 🐍/🔩 {.Add}.md>) function.

    ```yaml
    # Listen to only one trigger:
    #   either a placeholder change, or a timeout.

    - WAIT|<something> >> $expired
    ```

    | Argument| Purpose 
    |-|-
    | `<something>` | Either a `Timeout` or a `Signal`

    ---
    <br/>

1. **How to build a clock?**

    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🕙 Clock | ⏳ It's 17:01
    | 🕙 Clock | ⏳ It's 17:02

    ```yaml
    # 😃 Talker 
    💬 Clock:
    - TEMP|It's {.Now}
    - WAIT|00:00:01 
    - REPEAT
    ```

    Commands: [`.Now`](<../../...functions 🐍/🔩 {.Now}.md>) [`REPEAT`](<../REPEAT/REPEAT 🔁.md>) [`TEMP`](<../../../../🤔 Prompts/🤔📢 Prompt status/TEMP ⏳ prompt.md>) [`WAIT`](<WAIT ⏸️.md>)
    

    
    ---
    <br/>



1. **How to wait for a task to complete?**

    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🍕 Pizza | ℹ️ Order submitted 
    | 🍕 Pizza | ⏳ Step `1/3` Order in the queue...
    | 🍕 Pizza | ⏳ Step `2/3` Order being cooked...
    | 🍕 Pizza | ⏳ Step `3/3` Just finishing up...
    | 🍕 Pizza | ✅ Order ready!
    |

    Here's the [Script 📃](<../../...commands ⌘/📃 Script.md>).

    ```yaml
    # 😃 Talker 

    💬 Test:
    - EVAL|Submit >> $status     # Send
    - INFO|Order submitted       # Inform sent
    - RUN|WaitForReady           # Wait...
    - SUCCESS|Order ready!       # Inform ready

    WaitForReady:
    - TEMP|$status.Message       # Show status
    - WAIT|$status               # Wait
    - IF|$status.Ready:          # Signalled
        Then: RETURN             # End if ready
    - REPEAT                     # Repeat
    ```


    | [Command ⌘](<../../...commands ⌘/⌘ Command.md>) | Purpose
    |-|-
    | ⬇️ [`EVAL`](<../../...placeholders 🧠/EVAL ⬇️ flow.md>) | to assess the backend queue length.
    | ℹ️ [`INFO`](<../../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️ prompt.md>) | To show the initial message.
    | 🔁 [`REPEAT`](<../REPEAT/REPEAT 🔁.md>) | To re-assess the queue periodically.
    | 🔁 [`RETURN`](<../REPEAT/REPEAT 🔁.md>) | To exit the loop when it's the user's turn.
    | ▶️ [`RUN`](<../RUN ▶️.md>) | To start the waiting loop.
    | ✅ [`SUCCESS`](<../../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>) | To say that it's ready.
    | ⏳ [`TEMP`](<../../../../🤔 Prompts/🤔📢 Prompt status/TEMP ⏳ prompt.md>) | To show work in progress.

    ---
    <br/>


1. **How to wait in a queue?**

    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🏦 Bank | ⏳ There are 21 people ahead of you.
    | 🏦 Bank | ⏳ There are 7 people ahead of you.
    | 🏦 Bank | ⏳ You're next, get ready!
    | 🏦 Bank | 💬 What do you need? | `I need...`
    |

    Here's the [Script 📃](<../../...commands ⌘/📃 Script.md>).

    ```yaml
    # 😃 Talker 

    💬 Check-in:
    - RUN|WaitInLine
    - TEXT|What do you need?

    WaitInLine:

    # Check the status of the queue.
    - GET|Queues|MyQueue >> $len

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

    | [Command ⌘](<../../...commands ⌘/⌘ Command.md>) | Purpose
    |-|-
    | ⏯️️ [`CASE`](<../CASE/CASE ⏯️.md>) | To show the human-friendly message.
    | ⬇️ [`EVAL`](<../../...placeholders 🧠/EVAL ⬇️ flow.md>) | to assess the backend queue length.
    | ⏬ [`GET`](<../../...datasets 🪣/GET/GET ⏬ item.md>) | To get the queue length from resources.
    | 🔁 [`REPEAT`](<../REPEAT/REPEAT 🔁.md>) | To re-assess the queue periodically.
    | 🔁 [`RETURN`](<../REPEAT/REPEAT 🔁.md>) | To exit the loop when it's the user's turn.
    | ▶️ [`RUN`](<../RUN ▶️.md>) | To start the waiting loop.
    | ⏳ [`TEMP`](<../../../../🤔 Prompts/🤔📢 Prompt status/TEMP ⏳ prompt.md>) | To show work in progress.

    ---
    <br/>



1. **How to signal a WAIT placeholder?**

    Consider the following [`WAIT` ⏸️](<WAIT ⏸️.md>) command.

    ```yaml
    # 😃 Talker 
    - WAIT|24:00:00|$signal:
        OnSignal: SUCCESS|Signalled!
        OnTimeout: FAILURE|Timed out!
    ```

    To trigger it, a developer needs to call [`Write@Talker`](<../../../😃🅰️ Talker methods/🧑‍💻🚀😃 Place.md>).

    ```python
    # 🐍 Python

    def talkerHandler(args):
        TALKER.Write({
            'Chat': CHAT_ID,
            'Placeholder': 'signal',
            'Value': 'READY'
        })
    ```    

    The full interaction is described in the [😃⏩🧑‍💻 Wait ⏸️](<../../../😃⏩ Talker flows/😃⏩🧑‍💻 Wait ⏸️.md>) flow 

    ---
    <br/>