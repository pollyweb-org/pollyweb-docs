# 😃⏰ Talker `ALARM` command

> Part of [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>)

> Implemented by the [`.ALARM` 📃 script](<⏰ ALARM 📃 script.md>)

<br/>

1. **What is an ALARM command?**

    An `ALARM` 
    * is a [Command ⌘](<../../📃 basics/⌘ Command.md>) that schedules an alarm to be triggered at a specified time. 
    
    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    ALARM|$when:
        <script>:
            {params}
    ```

    Inputs | Purpose | Examples
    |-|-|-
    | `$when` | When to trigger the alarm | `2023-04-01` `1 day`
    | `<script>`| [Script 📃](<../../📃 commands ⌘/Script 📃/📃 Script.md>) to call | `MyHandler`
    | `{params}` | [Script 📃](<../../📃 commands ⌘/Script 📃/📃 Script.md>) input parameters  | `{A:1, B:2}`

    ---
    <br/>

1. **What's an example with absolute time?**

    ```yaml
    # Calculate the time into a holder
    - EVAL|.Add(Now, 1 day) >> $time

    # Pass the holder with the exact time
    - ALARM|$time:
        MyHandler: 
            A: 1
            B: 2
    ```
    Commands: [`.Add`](<../../📃 functions 🐍/🔩 {.Add}.md>) [`.Now`](<../../📃 functions 🐍/🔩 {.Now}.md>) [`EVAL`](<../../📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>)

    ---
    <br/>

1. **What's an example with relative time?**

    ```yaml
    # Same as .Add(.Now, 1 day)
    - ALARM|1 day:
        MyHandler: 
            A: 1
            B: 2
    ```

    This runs `.Add(.Now, 1 day)` under the hood.

    ---
    <br/>