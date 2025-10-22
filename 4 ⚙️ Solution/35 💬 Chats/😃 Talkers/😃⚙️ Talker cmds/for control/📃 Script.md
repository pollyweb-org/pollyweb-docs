# 😃📃 Talker `Script:`

> Part of [Talker 😃](<../../😃 Talker role.md>)

<br/>

1. **What's a Talker Script?**

    A [Script 📃]() 
    * is a set of [Commands ⌘](<⌘ Command.md>) 
    * executed sequentially in a block.

    ---
    <br/>

1. **What's the syntax of a Script?**
   
    ```yaml
    <script>:
    - <command-1>
    - <command-n>
    ```

    | Argument| Purpose
    |-|-
    | `📃 <script>` | The name of the [Script 📃](<📃 Script.md>).
    |            | The 📃 emoji is optional, and will be ignored.
    | `<command-n>` | A [Command ⌘](<⌘ Command.md>)  to be executed.
    
    ```yaml
    TestScript:
    - INFO|Hi!
    - CONFIRM|Are you OK? >> $answer
    ```
    
    ---
    <br/>


1. **How to invoke a Script?**

    |Context|Syntax
    |-|-
    |▶️ [`RUN`](<RUN ▶️.md>)| Calls a [Script 📃](<📃 Script.md>) by name, then returns.
    |⤵️ [`IF`](<IF ⤵️.md>) | Runs [Scripts 📃](<📃 Script.md>) for `True` and `False` evaluations.
    | ⏯️️ [`CASE`](<CASE ⏯️.md>) | Runs [Scripts 📃](<📃 Script.md>) for matching evaluations.
    | ⏸️ [`WAIT`](<WAIT ⏸️.md>) | Runs [Scripts 📃](<📃 Script.md>) on signalled and timed out.

    ---
    <br/>

1. **What's the syntax of a Script name?**

    No emojis nor special characters except dashes `-`, underscores `_`, and spaces ` `.
    * Emojis and special characters are reserved for current and future use.
    * Spaces are OK because only commas and pipes are used as separators.

    |Type|Example|
    |-|-
    |✅ Valid | `MyP` `My P` `myP` `my-p` `p2` `my_p`  `my--p` 
    |❌ Invalid | `{p}` `my$p` `$` `my-p!` `my/p` `my\|p` `my>p` `my,p` `👋`

    ---
    <br/>
