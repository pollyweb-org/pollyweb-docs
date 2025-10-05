# ⤵️ Talker `IF` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's an IF flow?**

    An `IF` ⤵️
    * is a flow [Command ⌘](<10 ⌘ Command.md>)  
    * that runs a [Procedure ⚙️](<11 ⚙️ Procedure.md>) or [Command ⌘](<10 ⌘ Command.md>) 
    * based on the evaluation of a placeholder or [{Function}](<12 🐍 {Function}.md>).

    ---
    <br/>

1. **How are values evaluated to booleans?**

    Type| ❌ False | Example | ✅ True | Example
    |-|-|-|-|-
    Boolean | false | `False` | true | `True`
    String   | empty | ` ` | non-empty | `.` `bla` 
    Number  | zero | `0` | non-zero | `1` `-1`
    Array | empty | `[]` | non-empty | `[1,A]`
    [Confirm 👍](<../31 🤔 Prompts/24 👍 CONFIRM prompt.md>) |  no | `No` | yes | `Yes`|
    [Share 💼](<46 💼 SHARE msg.md>) | empty | `{}`| non-empty | `{A:1}`
    

    ---
    <br/>

2. **What's the inline syntax?**

    > Note: this syntax only allows for [Procedures](<11 ⚙️ Procedure.md>), not [Commands](<10 ⌘ Command.md>).
   
    ```yaml
    - IF|{function}|<true-procedure>|<false-procedure>
    ```

    | Argument| Purpose
    |-|-
    | `{function}` | Boolean evaluation [{Function}](<12 🐍 {Function}.md>) name
    | `<true-procedure>` | Required [Procedure ⚙️](<11 ⚙️ Procedure.md>) to execute when `True`
    | `<false-procedure>`| Optional [Procedure ⚙️](<11 ⚙️ Procedure.md>) to execute when `False`
    
    ---
    <br/>

3. **What are examples of inline syntax?**


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test started
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Code is correct!
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test finished


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


    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['Function']:
        case 'code-is-correct':
          return True
    ```
    ---
    <br/>


2. **What's the multi-line syntax?**

    > This option allows both [Procedures](<11 ⚙️ Procedure.md>) and [Commands](<10 ⌘ Command.md>).
   
    ```yaml
    - IF|{function}:
        Then: <true-action>
        Else: <false-action>
    ```

    | Argument| Purpose
    |-|-
    | `{function}` | Name of a [{Function}](<12 🐍 {Function}.md>) that returns `True` or `False`.
    | `<true-action>` | Required [Procedure ⚙️](<11 ⚙️ Procedure.md>) or [Command ⌘](<10 ⌘ Command.md>) to execute when `True`
    | `<false-action>`| Optional [Procedure ⚙️](<11 ⚙️ Procedure.md>) or [Command ⌘](<10 ⌘ Command.md>)  to execute when `False`

    ---
    <br/>

2. **What are examples of multi-line syntax?**

    
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test started
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Code is correct!
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test finished


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


    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['Function']:
        case 'code-is-correct':
          return True
    ```

    ---
    <br/>

