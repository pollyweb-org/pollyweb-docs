# 😃👷🏼 Talker `ASYNC` command

> About
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* Implements the [`Async` ⏩ flow](<../../../../35 💬 Chats/Talkers 😃/😃⏩ Talker flows/Run Async Tasks 😃⏩📦/😃 Async ⏩ flow.md>)


## FAQ

1. **What's an ASYNC command?**

    An `ASYNC`
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)
    * that calls the [`Handle@Hosted` 🅰️ method](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Handle 😃🐌📦/📦 Handle 🐌 msg.md>)
    * has an asynchronous background task
    * i.e, it continues the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>), unlike [`CALL`](<../../⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>).

    ---
    <br/>


1. **What's the syntax of ASYNC?**

    ```yaml
    ASYNC|<task> >> $hook:
        {input}
    ```

    | Input | Purpose | Examples
    |-|-|-
    | `<task>` | The name of the task to execute | `Build`
    | `$input` | Optional inputs for the task | `A` `[A,B]` `{A:1}`
    | `$hook` | Optional [`WAIT`](<../WAIT 🧘/🧘 WAIT ⌘ cmd.md>) hook [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | `$hook`

    ---
    <br/>

1. **What are examples of ASYNC?**

    ```yaml
    # Task without a inputs and outputs
    - ASYNC|MyTask
    ```

    ```yaml
    # Task with only inputs
    - ASYNC|MyTask:
        A: 1
        B: 2
    ```

    ---
    <br/>

1. **How to wait for the result?**

    To wait for the result, 
    * ask the [`WAIT`](<../WAIT 🧘/🧘 WAIT ⌘ cmd.md>) command 
    * to wait for a change on the `$output` [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>), 
    * which will be triggered by the [`Handled@Talker` 🅰️ method](<../../../../35 💬 Chats/Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>).

    ```yaml
    # Task with an output
    - ASYNC|MyTask >> $hook:
        {A:1}

    # Wait for the output
    - WAIT|$hook >> $output
    ```
    Uses: [`WAIT`](<../WAIT 🧘/🧘 WAIT ⌘ cmd.md>)

    ---
    <br/>