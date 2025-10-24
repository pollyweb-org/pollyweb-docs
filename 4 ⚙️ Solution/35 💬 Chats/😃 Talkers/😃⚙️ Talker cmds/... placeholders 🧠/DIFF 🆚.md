# 😃🆚 Talker `DIFF` command

> Part of [{Function} 🐍](<../...functions 🐍/{Function} 🐍.md>)

<br/>


1. **What is a DIFF command?**

    A `DIFF` 
    * is a [Command ⌘](<../...commands ⌘/⌘ Command.md>) 
    * that outputs the the difference between [Placeholders 🧠](<$Placeholder 🧠.md>).

    ---
    <br/>

1. **What's the DIFF syntax?**

    ```yaml
    # Single line
    DIFF|<from>|<to> >> $diff
    ```

    ```yaml
    # Multiline
    DIFF >> $diff:
        From: <from>
        To: <to>
    ```

    | Arguments | Purpose | Examples
    |-|-|-
    | `<from>`  | Base value    | `1` `ABC` `.Today` 
    | `<to>`    | Changed value | `5` `ABE` `.Now` 
    | `$diff`   | Changes       | -

    ---
    <br/>

1. **What's an example of DIFF?**

    Here's a [Script 📃](<../...commands ⌘/📃 Script.md>)

    ```yaml
    # Process the period
    - PERIOD|.Today|.Now >> $period
    
    # Show the total number of seconds since midnight
    - INFO|{$period.TotalSeconds} seconds from midnight:
    ```
    Commands: [`.Today`](<../...functions 🐍/🔩 {.Today}.md>) [`.Now`](<../...functions 🐍/🔩 {.Now}.md>) [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️ prompt.md>)

    ---
    <br/>

1. **What's the DIFF output for time?**

    Here's the `$diff`  [Placeholder 🧠](<$Placeholder 🧠.md>) when comparing times;
    * e.g. [`.Today`](<../...functions 🐍/🔩 {.Today}.md>), [`.Now`](<../...functions 🐍/🔩 {.Now}.md>), or an [Item 🛢](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) from [`GET`](<../...datasets 🪣/GET ⏬ item.md>);
    * note: `.Verbose` receives the maximum number or parts.

    | Property | Type | Example 
    |-|-|-
    | `.Verbose(n)` | str | `1 month, 3 days, and 6 hours` 
    | `.Time`       | str | `352h 42m 06s`
    | `.Seconds`  | int |  `264473`
    | `.Minutes`  | int | `123`
    | `.Hours`    | int | `123`
    | `.Days`     | int |  `123`
    | `.Months`   | int | `123`
    | `.Years`    | int | `123345`
    | `.Weeks`    | int | `123`
    
    
    ---
    <br/>

1. **What's the DIFF output for arrays?**

    <!-- TODO: -->

    ---
    <br>

1. **What's the DIFF output for objects?**

    <!-- TODO: -->
    
    ---
    <br>