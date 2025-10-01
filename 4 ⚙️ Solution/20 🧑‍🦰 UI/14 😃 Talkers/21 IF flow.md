# Talker `IF` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's an IF flow?**

    An `IF` is a command that runs a [Procedure](<11 Procedure block.md>) based on a [Function](<12 Function block.md>).

    ---
    <br/>

1. **What's the syntax for procedures?**
   
    ```yaml
    IF|{function}|<true-procedure>|<false-procedure>
    ```

    | Argument| Purpose
    |-|-
    | `{function}` | Boolean evaluation [Function](<12 Function block.md>) name
    | `<true-procedure>` | Required [Procedure](<11 Procedure block.md>) to execute when `True`
    | `<false-procedure>`| Optional [Procedure](<11 Procedure block.md>) to execute when `False`
    

    ```yaml
    💬 If-them example:
    - IF|{code-is-correct}|correct-code

    correct-code:
    - SUCCESS|Code is correct!
    ```

    ```yaml
    💬 If-then-else example:
    - IF|{code-is-correct}|correct-code|wrong-code

    correct-code:
    - SUCCESS|Code is correct!

    wrong-code:
    - FAILURE|Code is wrong!
    ```

    ---
    <br/>


1. **What's the syntax for single commands?**
   
    ```yaml
    IF|{function}:
        Then: <true-command>
        Else: <false-command>
    ```

    | Argument| Purpose
    |-|-
    | `{function}` | Boolean evaluation [Function](<12 Function block.md>) name
    | `<true-command>` | Required [Procedure](<11 Procedure block.md>) to execute when `True`
    | `<false-command>`| Optional [Procedure](<11 Procedure block.md>) to execute when `False`
    
    ```yaml
    💬 If-them example:
    - IF|{code-is-correct}:
        Then: SUCCESS|Code is correct!
    ```

    ```yaml
    💬 If-then-else example:
    - IF|{code-is-correct}:
        Then: SUCCESS|Code is correct!
        Else: FAILURE|Code is wrong!
    ```

    ---
    <br/>

