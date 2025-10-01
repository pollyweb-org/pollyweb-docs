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
    | `<procedure>` | The name of the procedure, with lower-case dashes.
    | `<command-n>` | A [Command](<10 Command.md>)  to be executed.
    
    ```yaml
    example-procedure:
    - INFO|Hi!
    - CONFIRM|Are you OK? >> answer
    ```
    


    ---
    <br/>

1. **How to invoke a procedure?**

    |Context|Syntax
    |-|-
    |[Commands](<10 Command.md>)| `RUN\|<procedure>`
    |[`IF` flows](<21 IF flow.md>) | `IF\|{function}\|<procedure>`
    |[`CASE` flows](<22 CASE flow.md>) | `CASE\|{function}\|<procedure>`

    ---
    <br/>