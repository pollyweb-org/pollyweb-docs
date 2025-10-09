# ⚙️ Talker `<procedure>:`

> Part of [Talker 😃](<../10 📘 Talker specs/01 😃 Talker.md>)

<br/>

1. **What's a Talker Procedure?**

    A [Procedure ⚙️](<10 ⌘ Command.md>) executed sequentially.

    ---
    <br/>

1. **What's the syntax of a Procedure?**
   
    ```yaml
    <procedure>:
    - <command-1>
    - <command-n>
    ```

    | Argument| Purpose
    |-|-
    | `<procedure>` | The name of the [Procedure ⚙️](<11 ⚙️ Procedure.md>).
    | `<command-n>` | A [Command ⌘](<10 ⌘ Command.md>)  to be executed.
    
    ```yaml
    ExampleProcedure:
    - INFO|Hi!
    - CONFIRM|Are you OK? >> $answer
    ```
    
    ---
    <br/>


1. **How to invoke a Procedure?**

    |Context|Syntax
    |-|-
    |▶️ [`RUN`](<24 ▶️ RUN flow.md>)| Calls a procedure by name, then returns.
    |⤵️ [`IF`](<21 ⤵️ IF flow.md>) | Runs procedures for `True` and `False` evaluations.
    | 🔀 [`CASE`](<22 🔀 CASE flow.md>) | Runs procedures for matching evaluations.
    | ⏸️ [`WAIT`](<28 ⏸️ WAIT flow.md>) | Runs procedures on signalled and timed out.

    ---
    <br/>

1. **What's the syntax of a Procedure name?**

    No emojis nor special characters except dashes `-`, underscores `_`, and spaces ` `.
    * Emojis and special characters are reserved for current and future use.
    * Spaces are OK because only commas and pipes are used as separators.

    |Type|Example|
    |-|-
    |✅ Valid | `MyP` `My P` `myP` `my-p` `p2` `my_p`  `my--p` 
    |❌ Invalid | `{p}` `my$p` `$` `my-p!` `my/p` `my\|p` `my>p` `my,p` `👋`

    ---
    <br/>
