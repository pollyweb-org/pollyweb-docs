# ⤵️ Talker `IF` flow 

> Part of [Talker 😃](<../../33 😃 Talkers/01 😃 Talker.md>)

<br/>


1. **What's an IF flow?**

    An `IF` ⤵️
    * is a flow [Command ⌘](<10 ⌘ Command.md>)  
    * that runs a [Procedure ⚙️](<../../33 😃 Talkers/11 ⚙️ Procedure.md>) or [Command ⌘](<10 ⌘ Command.md>) 
    * based on the evaluation of a placeholder or [{Function}](<../../33 😃 Talkers/12 🐍 {Function}.md>).

    ---
    <br/>

1. **How are values evaluated to booleans?**

    Type| ❌ False | Example | ✅ True | Example
    |-|-|-|-|-
    Boolean | false | `False` | true | `True`
    String   | empty | ` ` | non-empty | `.` `bla` 
    Number  | zero | `0` | non-zero | `1` `-1`
    Array | empty | `[]` | non-empty | `[1,A]`
    [Confirm 👍](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/31 👍 CONFIRM prompt.md>) |  no | `No` | yes | `Yes`|
    [Share 💼](<../60 Messages/45 💼 SHARE msg.md>) | empty | `{}`| non-empty | `{A:1}`
    

    ---
    <br/>


1. **What's the `IF` syntax?**
    
    ```yaml
    # One-line Procedures
    - IF|{function}|<true-proc>|<false-proc>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `{function}` | Boolean [{Function}](<../../33 😃 Talkers/12 🐍 {Function}.md>) to evaluate  | `{f}` `{$o}`
    || Allows for missing `{}` in functions | `f()` `$p`
    || Defaults to the last [input prompt ✏️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/11 ✏️ Input behavior.md>) | `TEXT\|Id?`
    | `<true-proc>` | [Procedure ⚙️](<../../33 😃 Talkers/11 ⚙️ Procedure.md>) to [Run ▶️](<24 ▶️ RUN flow.md>) when `True` | `IfTrue`
    | `<false-proc>`| [Procedure ⚙️](<../../33 😃 Talkers/11 ⚙️ Procedure.md>) to [Run ▶️](<24 ▶️ RUN flow.md>) when `False` | `IfFalse(X)`
    
    ```yaml
    # Multi-line actions: 
    #   i.e., Procedure or one-line Command

    - IF: 
        Function: {function} # (empty) → last input
        Then: <true-action>
        Else: <false-action>
    ```

    | Argument| Purpose
    |-|-
    | `<true-action>` | [Procedure ⚙️](<../../33 😃 Talkers/11 ⚙️ Procedure.md>) or one-line [Command ⌘](<10 ⌘ Command.md>) on `True`
    | `<false-action>`| [Procedure ⚙️](<../../33 😃 Talkers/11 ⚙️ Procedure.md>) or one-line [Command ⌘](<10 ⌘ Command.md>) on `False`


    ```yaml
    # Multi-line Command lists
    - IF:
        Function: {function} # (empty) → last input
        Then: 
            - <true-cmd-1>
            - <true-cmd-n>
        Else: 
            - <false-cmd-1>
            - <false-cmd-n>
    ```

    | Argument| Purpose
    |-|-
    | `<true-cmd-n>` | List of multi-line [Commands ⌘](<10 ⌘ Command.md>) to run on `True`
    | `<false-cmd-n>` | List of multi-line [Commands ⌘](<10 ⌘ Command.md>) to run on `False`

    ---
    <br/>

1. **What are examples of inline syntax?**


    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test started
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Code is correct!
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test finished


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



1. **What are examples of multi-line syntax?**

    
    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test started
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Code is correct!
    | [🤗 Host](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Test finished


    ```yaml
    # 😃 Talker with multi-line IF-THEN (no ELSE).
    
    💬 If-them example:
    - INFO|Test started
    - IF|{code-is-correct}:
        Then: 
          - SUCCESS|Code is correct!
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

