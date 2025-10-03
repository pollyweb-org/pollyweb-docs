# ⤵️ Talker `IF` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's an IF flow?**

    An `IF` is a flow [Command](<10 Command.md>)  that runs a [Procedure](<20 ⚙️ Procedure block.md>) or [Command](<10 Command.md>) based on the evaluation of a boolean [{Function}](<11 {Function} command.md>).

    ---
    <br/>

2. **What's the inline syntax?**

    > Note: this option only allows [Procedures](<20 ⚙️ Procedure block.md>), not [Commands](<10 Command.md>).
   
    ```yaml
    - IF|{function}|<true-procedure>|<false-procedure>
    ```

    | Argument| Purpose
    |-|-
    | `{function}` | Boolean evaluation [{Function}](<11 {Function} command.md>) name
    | `<true-procedure>` | Required [Procedure](<20 ⚙️ Procedure block.md>) to execute when `True`
    | `<false-procedure>`| Optional [Procedure](<20 ⚙️ Procedure block.md>) to execute when `False`
    
    ---
    <br/>

1. **What are examples of inline syntax?**

    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['function']:
        case 'code-is-correct':
          return True
    ```

    ```yaml
    # 😃 Talker with inline IF-THEN (no ELSE).

    💬 If-then example:
    - INFO|Test started
    - IF|{code-is-correct}|CorrectCode
    - INFO|Test finished

    CorrectCode:
    - SUCCESS|Code is correct!
    ```

    ```yaml
    # 😃 Talker with inline IF-THEN-ELSE.

    💬 If-then-else example:
    - INFO|Test started
    - IF|{code-is-correct}|CorrectCode|WrongCode
    - INFO|Test finished

    CorrectCode:
    - SUCCESS|Code is correct!

    WrongCode:
    - FAILURE|Code is wrong!
    ```

    | Domain | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test started
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Code is correct!
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test finished

    ---
    <br/>


2. **What's the multi-line syntax?**

    > This option allows both [Procedures](<20 ⚙️ Procedure block.md>) and [Commands](<10 Command.md>).
   
    ```yaml
    - IF|{function}:
        Then: <true-action>
        Else: <false-action>
    ```

    | Argument| Purpose
    |-|-
    | `{function}` | Name of a [{Function}](<11 {Function} command.md>) that returns `True` or `False`.
    | `<true-action>` | Required [Procedure](<20 ⚙️ Procedure block.md>) or [Command](<10 Command.md>) to execute when `True`
    | `<false-action>`| Optional [Procedure](<20 ⚙️ Procedure block.md>) or [Command](<10 Command.md>)  to execute when `False`

    ---
    <br/>

2. **What are examples of multi-line syntax?**

    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['function']:
        case 'code-is-correct':
          return True
    ```
       
    ```yaml
    # 😃 Talker with multi-line IF-THEN (no ELSE).
    
    💬 If-them example:
    - INFO|Test started
    - IF|{code-is-correct}:
        Then: SUCCESS|Code is correct!
    - INFO|Test finished
    ```

    ```yaml
    # 😃 Talker with multi-line IF-THEN-ELSE.

    💬 If-then-else example:
    - INFO|Test started
    - IF|{code-is-correct}:
        Then: SUCCESS|Code is correct!
        Else: ErrorHandlingProcedure
    - INFO|Test finished
        
    ErrorHandlingProcedure:
    - FAILURE|Code is wrong!
    ```

    | Domain | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test started
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Code is correct!
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test finished

    ---
    <br/>

