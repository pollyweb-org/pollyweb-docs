<!-- -->

# 😃🍂 Talker `ASYNC` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

<br/>

1. **What's an ASYNC command?**

    An `ASYNC`
    * is a [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>)
    * to trigger an asynchronous background task.

    ---
    <br/>


1. **What's the syntax of ASYNC?**

    ```yaml
    ASYNC|<task> >> $output:
        {input}
    ```

    | Argument | Purpose | Examples
    |-|-|-
    | `<task>` | The name of the task to execute | `Build`
    | `$input` | Optional inputs for the task | `A` `[A,B]` `{A:1}`
    | `$output` | Optional [Placeholder 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) for results | `$result`

    ---
    <br/>

1. **What's an example of ASYNC?**

    ```yaml
    ASYNC|Task >> $output:
        {input}
    ```