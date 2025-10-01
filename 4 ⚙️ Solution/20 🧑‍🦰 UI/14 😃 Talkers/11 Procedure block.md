# Talker `<procedure>`

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What's a Talker procedure?**

    A procedure is a set of [Commands](<10 Command.md>) executed sequentially.

    ---
    <br/>

1. **What's the syntax of a procedure?**
   
    ```yaml
    <procedure>:
    - <command-1>
    - <command-n>
    ```

    | Argument| Purpose
    |-|-
    | `<procedure>` | The name of the procedure.
    | `<command-n>` | A [Command](<10 Command.md>)  to be executed.
    
    ```yaml
    ExampleProcedure:
    - INFO|Hi!
    - CONFIRM|Are you OK? >> answer
    ```
    
    ---
    <br/>


2. **How to invoke a procedure?**

    |Context|Syntax
    |-|-
    |[`RUN`](<23 RUN flow.md>)| `RUN\|<procedure>`
    |[`IF`](<21 IF flow.md>) | `IF\|{function}\|<procedure>`
    |[`CASE`](<22 CASE flow.md>) | `CASE\|{function}\|<procedure>`

    ---
    <br/>

3. **What's the syntax of a procedure name?**

    Rules:
    - Only letters, numbers, and single dashes.
    - Starts with a letter.

    |Example|OK?|Reason
    |-|-|-
    |`MyProc`| ✅ | Valid.
    |`my-proc`| ✅ | Valid.
    |`my-proc-2`| ✅ | Valid.
    |`$my-proc`| ❌ | Didn't start with a letter.  
    |`my$proc`| ❌ | Invalid character `$`.  
    |`my proc`| ❌ | Spaces not allowed.    
    |`my_proc`| ❌ | Underscores are not allowed.
    |`myProc`| ❌ | Upper-case letters are not allowed.
    |`2-my-proc`| ❌ | Didn't start with a letter.
    |`my--proc`| ❌ | Single dashes only.
    |`my-proc!`| ❌ | Special characters are not allowed.

    ---
    <br/>
