# Talker `IF` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's an IF flow?**

    An `IF` is a [Command](<10 Command.md>)  that runs a [Procedure](<12 Procedure block.md>) or [Command](<10 Command.md>) based on the evaluation of a boolean [Function](<15 Function block.md>).

    ---
    <br/>

2. **What's the inline syntax?**

    > Note: this option only allows [Procedures](<12 Procedure block.md>), not [Commands](<10 Command.md>).
   
    ```yaml
    - IF|{function}|<true-procedure>|<false-procedure>
    ```

    | Argument| Purpose
    |-|-
    | `{function}` | Boolean evaluation [Function](<15 Function block.md>) name
    | `<true-procedure>` | Required [Procedure](<12 Procedure block.md>) to execute when `True`
    | `<false-procedure>`| Optional [Procedure](<12 Procedure block.md>) to execute when `False`
    

    ```yaml
    💬 If-then example:
    - IF|{code-is-correct}|CorrectCode

    CorrectCode:
    - SUCCESS|Code is correct!
    ```

    ```yaml
    💬 If-then-else example:
    - IF|{code-is-correct}|CorrectCode|WrongCode

    CorrectCode:
    - SUCCESS|Code is correct!

    WrongCode:
    - FAILURE|Code is wrong!
    ```

    ---
    <br/>


3. **What's the multiline syntax?**

    > This option allows both [Procedures](<12 Procedure block.md>) and [Commands](<10 Command.md>).
   
    ```yaml
    - IF|{function}:
        Then: <true-action>
        Else: <false-action>
    ```

    | Argument| Purpose
    |-|-
    | `{function}` | Boolean evaluation [Function](<15 Function block.md>) name
    | `<true-action>` | Required [Procedure](<12 Procedure block.md>) or [Command](<10 Command.md>) to execute when `True`
    | `<false-action>`| Optional [Procedure](<12 Procedure block.md>) or [Command](<10 Command.md>)  to execute when `False`
    
    ```yaml
    💬 If-them example:
    - IF|{code-is-correct}:
        Then: SUCCESS|Code is correct!
    ```

    ```yaml
    💬 If-then-else example:
    - IF|{code-is-correct}:
        Then: SUCCESS|Code is correct!
        Else: ErrorHandlingProcedure
        
    ErrorHandlingProcedure:
    - FAILURE|Code is wrong!
    ```

    ---
    <br/>

