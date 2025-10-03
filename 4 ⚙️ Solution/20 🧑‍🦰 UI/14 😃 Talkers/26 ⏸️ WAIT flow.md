# ⏸️ Talker `WAIT` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>



1. **What's a WAIT flow command?**

    A `WAIT` 
    * is a flow [Command](<10 Command.md>) 
    * that pauses the flow for a period of time 
    * or until triggered by an external signal.

    ---
    <br/>


1. **What's the WAIT syntax?**

    ```yaml
    - WAIT|<period>|<placeholder>:
        OnSignal: <on-signal>
        OnTimeout: <on-timeout>
    ```

    | Argument| Purpose
    |-|-
    | `<period>`        | Time before it times out.
    | `<placeholder>`   | Signal placeholder to trigger before timeout.
    | `<on-signal>`        | Run [Procedure](<20 ⚙️ Procedure block.md>) or [Command](<10 Command.md>) when signalled.
    | `<on-timeout>`        | Run [Procedure](<20 ⚙️ Procedure block.md>) or [Command](<10 Command.md>) when times out.

    ---
    <br/>

2. **What's a simple WAIT example?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
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
    

    | Command | Purpose
    |-|-
    | [`REPEAT`](<23 🔁 REPEAT flow.md>) | To update the message.

    ---
    <br/>

3. **What's an example of verifying a queue length?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🏦 Bank | ⏳ There are 21 people ahead of you.
    | 🏦 Bank | ⏳ There are 7 people ahead of you.
    | 🏦 Bank | ⏳ You're next, get ready!
    | 🏦 Bank | 💬 What do you need? | `I need...`
    

    ```yaml
    # 😃 Talker 

    💬 Check-in:
    - RUN|WaitInLine
    - TEXT|What do you need?

    WaitInLine:

    # Check the status of the queue.
    - EVAL|{queue-length} >> len

    # Show the status in a human-friendly wait.
    - CASE|{$len}:
        *: TEMP|There are {$len} people ahead of you.
        1: TEMP|You're next, get ready!
        0: RETURN
    
    # Wait 1 minute or until signalled.
    - WAIT|00:01:00|signal:
        OnSignal: RETURN

    # Check the queue length again.
    - REPEAT
    ```

    | Command | Purpose
    |-|-
    | [`RUN`](<24 ▶️ RUN flow.md>) | To start the waiting loop.
    | [`EVAL`](<12 🧠 EVAL block.md>) | to assess the backend queue length.
    | [`CASE`](<22 🔀 CASE flow.md>) | To show the human-friendly message.
    | [`RETURN`](<23 🔁 REPEAT flow.md>) | To exit the loop when it's the user's turn.
    | [`REPEAT`](<23 🔁 REPEAT flow.md>) | To re-assess the queue periodically.

    ---
    <br/>


4. **How to signal a WAIT placeholder?**

    Consider the following `WAIT` command.

    ```yaml
    # 😃 Talker 
    - WAIT|24:00:00|for-something:
        OnSignal: SUCCESS|Signalled!
        OnTimeout: FAILURE|Timed out!
    ```

    <!-- 
    TODO: Add HOSTER.Signal() documentation.
    -->

    To trigger it, a developer needs to invoke the [Hoster 🧑‍💻 helper](<../12 💬 Chats/05 🧑‍💻🛠️ Hoster helper.md>) SDK.

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