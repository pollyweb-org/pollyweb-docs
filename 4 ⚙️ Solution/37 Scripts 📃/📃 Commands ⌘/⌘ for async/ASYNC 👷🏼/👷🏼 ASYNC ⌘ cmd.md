# 😃👷🏼 Talker `ASYNC` command

> About
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* Used by the [`CALL` 🧮 command](<../CALL 🧮/🧮 CALL ⌘ cmd.md>) 
* Implements the [`Async` ⏩ flow](<../../../../35 💬 Chats/Talkers 😃/😃⏩ Talker flows/Long Async Tasks 😃⏩📦/😃 Async ⏩ flow.md>)
* Calls a [`{code}` 🐍  function](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>) implemented in a [Hosted 📦 domain](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>)

<br/>

## FAQ

1. **What's an ASYNC command?**

    An `ASYNC`
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)
    * that calls the [`Handle@Hosted` 🐌 msg](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Handle 😃🐌📦/📦 Handle 🐌 msg.md>)
    * has an asynchronous background task
    * i.e, it continues the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>), unlike [`CALL`](<../CALL 🧮/🧮 CALL ⌘ cmd.md>).

    ---
    <br/>


1. **What's the syntax of ASYNC?**

    ```yaml
    # Comprehensive syntax
    ASYNC:
        Hook: <hook-uuid>  # Placed@, Place@, Handled@ hook
        Name: <name>       # Hosted function name
        Inputs: {inputs}   # Hosted function inputs
    ```

    ```yaml
    # With an auto-generated hook
    ASYNC <name> >> $hook: 
        {inputs}
    ```

    | Input | Purpose | Examples
    |-|-|-
    | `Name` | [Hosted 📦](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) function to execute | `Build`
    | `Inputs` | Optional inputs for the function | `A` `[A,B]` `{A:1}`
    | `Hook` | Optional [`WAIT`](<../WAIT 🧘/🧘 WAIT ⌘ cmd.md>) hook [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | `$hook`

    ---
    <br/>

1. **What are examples of ASYNC?**

    ```yaml
    # Task without a inputs and outputs
    - ASYNC: MyTask
    ```

    ```yaml
    # Task with only inputs
    - ASYNC MyTask:
        A: 1
        B: 2
    ```

    ---
    <br/>

1. **How to wait for the result?**

    To wait for the result, use the blocking [`CALL` 🧮 command](<../CALL 🧮/🧮 CALL ⌘ cmd.md>) instead.

    ---
    <br/>

1. **How to wait for the result with periodic user feedback?**

    To wait for the result, 
    * ask the [`WAIT`](<../WAIT 🧘/🧘 WAIT ⌘ cmd.md>) command 
    * to wait for a change on the `$output` [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>), 
    * which will be triggered by the [`Handled@Talker` 🐌 msg](<../../../../35 💬 Chats/Talkers 😃/😃📨 Talker msgs/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>).

    ```yaml
    📃 Example: 
    
    # Task with an output
    - ASYNC MyTask >> $hook:
        A: 1

    # Wait for the output
    - WAIT: $hook >> $output
    ```
    Uses: [`WAIT`](<../WAIT 🧘/🧘 WAIT ⌘ cmd.md>)

    ---
    <br/>

1. **How to have access to the [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)?**

    To have access to the [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>),
    * use the [`IMPRINT` 🦶 command](<../IMPRINT 🦶/🦶 IMPRINT ⌘ cmd.md>) to snapshot them 
    * then access them with [`Placed@Talker` 📨 msg](<../../../../35 💬 Chats/Talkers 😃/😃📨 Talker msgs/Placed 🧑‍💻🚀😃/😃 Placed 📃 handler.md>) 
    * from the [Hosted 📦 domain](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>).

    ```yaml
    📃 Example: 

    # Generate a common hook
    - PUT >> $hook: .UUID 

    # Imprint holders before ASYNC
    - IMPRINT: $hook

    # Call ASYNC
    - ASYNC:
        Hook: $hook
        Name: MyTask 
        Inputs: 
            A: 1
    ```
    Uses: [`IMPRINT`](<../IMPRINT 🦶/🦶 IMPRINT ⌘ cmd.md>) [`PUT`](<../../⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>)
    
    ---
    <br/>


1. **How to update [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with a feedback loop?**

    To update [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) in a feedback loop,
    * update them with the [`Place@Talker` 📨 msg](<../../../../35 💬 Chats/Talkers 😃/😃📨 Talker msgs/Placed 🧑‍💻🚀😃/😃 Placed 📃 handler.md>)
    * from the [Hosted 📦 domain](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>)
    * them call the [`RECALL`](<../RECALL 🪶/🪶 RECALL ⌘ cmd.md>) command after the [`WAIT`](<../WAIT 🧘/🧘 WAIT ⌘ cmd.md>) command.

    ```yaml
    📃 Example: 

    # Generate a common hook
    - PUT >> $hook: .UUID 

    # Imprint holders before ASYNC
    - IMPRINT: $hook

    # Call ASYNC
    - ASYNC:
        Hook: $hook
        Name: MyTask 
        Inputs: 
            A: 1

    # Wait for the output
    - WAIT: $hook >> $output

    # Recall holders after ASYNC
    - RECALL: $hook
    ```
    Uses: [`IMPRINT`](<../IMPRINT 🦶/🦶 IMPRINT ⌘ cmd.md>) [`PUT`](<../../⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`WAIT`](<../WAIT 🧘/🧘 WAIT ⌘ cmd.md>) [`RECALL`](<../RECALL 🪶/🪶 RECALL ⌘ cmd.md>)
    
    ---
    <br/>

