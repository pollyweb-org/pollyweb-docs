# 😃👷🏼 Talker `WORK` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

> Implements the [`Async` ⏩ flow](<../../../😃⏩ Talker flows/Async Tasks 😃⏩📦/😃 Async ⏩ flow.md>)

<br/>

1. **What's an WORK command?**

    An `WORK`
    * is a [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>)
    * that calls the [`Handle@Hosted` 🅰️ method](<../../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Handle 😃🐌📦/📦 Handle 🐌 msg.md>)
    * has an asynchronous background task
    * i.e, it continues the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>), unlike [`EVAL`](<../../...placeholders 🧠/EVAL ⬇️ flow.md>).

    ---
    <br/>


1. **What's the syntax of WORK?**

    ```yaml
    WORK|<task> >> $output:
        {input}
    ```

    | Argument | Purpose | Examples
    |-|-|-
    | `<task>` | The name of the task to execute | `Build`
    | `$input` | Optional inputs for the task | `A` `[A,B]` `{A:1}`
    | `$output` | Optional [Placeholder 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) for results | `$result`

    ---
    <br/>

1. **What are examples of WORK?**

    ```yaml
    # Task without a inputs and outputs
    - WORK|MyTask
    ```

    ```yaml
    # Task with only inputs
    - WORK|MyTask:
        A: 1
        B: 2
    ```

    ---
    <br/>

1. **How to wait for the result?**

    To wait for the result, 
    * ask the [`WAIT`](<../WAIT ⏸️/WAIT ⏸️.md>) command 
    * to wait for a change on the `$output` [Placeholder 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>), 
    * which will be triggered by the [`Handled@Talker` 🅰️ method](<../../../😃🅰️ Talker methods/Handled/🧑‍💻🐌😃 Handled.md>).

    ```yaml
    # Task with an output
    - WORK|MyTask >> $output:
        {A:1}

    # Wait for the output
    - WAIT|$output
    ```
    Commands: [`WAIT`](<../WAIT ⏸️/WAIT ⏸️.md>)

    ---
    <br/>