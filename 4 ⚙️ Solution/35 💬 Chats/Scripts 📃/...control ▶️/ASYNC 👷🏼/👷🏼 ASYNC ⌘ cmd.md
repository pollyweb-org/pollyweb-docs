# 😃👷🏼 Talker `ASYNC` command

> Part of [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>)

> Implements the [`Async` ⏩ flow](<../../../Talkers 😃/😃⏩ Talker flows/Async Tasks 😃⏩📦/😃 Async ⏩ flow.md>)

<br/>

1. **What's an ASYNC command?**

    An `ASYNC`
    * is a [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>)
    * that calls the [`Handle@Hosted` 🅰️ method](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Handle 😃🐌📦/📦 Handle 🐌 msg.md>)
    * has an asynchronous background task
    * i.e, it continues the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>), unlike [`EVAL`](<../../../Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>).

    ---
    <br/>


1. **What's the syntax of ASYNC?**

    ```yaml
    ASYNC|<task> >> $output:
        {input}
    ```

    | Input | Purpose | Examples
    |-|-|-
    | `<task>` | The name of the task to execute | `Build`
    | `$input` | Optional inputs for the task | `A` `[A,B]` `{A:1}`
    | `$output` | Optional [Holder 🧠](<../../../Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/$Holder 🧠.md>) for results | `$result`

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
    * to wait for a change on the `$output` [Holder 🧠](<../../../Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/$Holder 🧠.md>), 
    * which will be triggered by the [`Handled@Talker` 🅰️ method](<../../../Talkers 😃/😃🅰️ Talker methods/Handled 🧑‍💻🐌😃/😃 Handled 🐌 msg.md>).

    ```yaml
    # Task with an output
    - ASYNC|MyTask >> $hook:
        {A:1}

    # Wait for the output
    - WAIT|$hook >> $output
    ```
    Commands: [`WAIT`](<../WAIT 🧘/🧘 WAIT ⌘ cmd.md>)

    ---
    <br/>