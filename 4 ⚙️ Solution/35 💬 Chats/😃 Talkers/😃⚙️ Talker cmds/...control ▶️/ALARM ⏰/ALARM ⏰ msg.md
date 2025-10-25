# 😃⏰ Talker `ALARM` command

> Implemented by the [`.ALARM` 📃 script](<.📎 Assets/ALARM 📃 script.md>)

<br/>

1. **What is an ALARM command?**

    An `ALARM` 
    * is a [Command ⌘](<../../...commands ⌘/⌘ Command.md>) that schedules an alarm to be triggered at a specified time. 
    
    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    ALARM|$when:
        <script>:
            {params}
    ```

    Args | Purpose | Examples
    |-|-|-
    | `$when` | When to trigger the alarm | `2023-04-01` `1 day`
    | `<script>`| [Script 📃](<../../...commands ⌘/📃 Script.md>) to call | `MyHandler`
    | `{params}` | [Script 📃](<../../...commands ⌘/📃 Script.md>) input parameters  | `{A:1, B:2}`

    ---
    <br/>

1. **What's an example with absolute time?**

    ```yaml
    # Calculate the time into a placeholder
    - EVAL|.Add(Now, 1 day) >> $time

    # Pass the placeholder with the exact time
    - ALARM|$time$:
        MyHandler: 
            A: 1
            B: 2
    ```
    Commands: [`.Add`](<../../...functions 🐍/🔩 {.Add}.md>) [`.Now`](<../../...functions 🐍/🔩 {.Now}.md>) [`EVAL`](<../../...placeholders 🧠/EVAL ⬇️ flow.md>)

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