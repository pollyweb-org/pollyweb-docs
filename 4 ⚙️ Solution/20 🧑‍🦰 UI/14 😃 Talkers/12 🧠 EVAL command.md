# 😃 Talker `EVAL` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's an EVAL command?**

    An `EVAL` is a [Command](<10 Command.md>) that evaluates a [{Function}](<11 {Function} command.md>) into a placeholder.

    ---
    <br/>

2. **What's the syntax?**

    ```yaml
    - EVAL|{function} >> <placeholder>
    ```

    | Argument| Purpose
    |-|-
    | `{function}`| The [{Function}](<11 {Function} command.md>) to be evaluated.
    | `<placeholder>`| The placeholder to store the evaluation result.
    
    ---
    <br/>


2. **What's an example?**

    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['function']:
        case 'get-time':
          return True
    ```
       
    ```yaml
    # 😃 Talker.
    - EVAL|{get-time} >> time
    - INFO|It's {time}
    ```

    ---
    <br/>
