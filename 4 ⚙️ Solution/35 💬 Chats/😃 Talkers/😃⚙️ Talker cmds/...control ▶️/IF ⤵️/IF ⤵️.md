# 😃⤵️ Talker `IF` flow 

> Part of [Talker 😃](<../../../😃 Talker role.md>)

<br/>


1. **What's an IF flow?**

    An `IF` ⤵️
    * is a flow [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>)  
    * that runs a [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) or [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>)
    * based on the evaluation of a placeholder or [{Function}](<../../...functions 🐍/{Function} 🐍.md>).

    ---
    <br/>

1. **How are values evaluated to booleans?**

    Type| ❌ False | Example | ✅ True | Example
    |-|-|-|-|-
    Boolean | false | `False` | true | `True`
    String   | empty | ` ` | non-empty | `.` `bla` 
    Number  | zero | `0` | non-zero | `1` `-1`
    Array | empty | `[]` | non-empty | `[1,A]`
    [Confirm 👍](<../../../../🤔 Prompts/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) |  no | `No` | yes | `Yes`|
    [Share 💼](<../../...methods 🤵/SHARE 💼/SHARE 💼 msg.md>) | empty | `{}`| non-empty | `{A:1}`
    

    ---
    <br/>

1. **What's the IF syntax for one-line thens?**
    
    ```yaml
    # In-line 
    - IF|{function}|<true-script>

    # Multi-line 
    - IF|{function}:
        <true-action>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `{function}` | Boolean [{Function}](<../../...functions 🐍/{Function} 🐍.md>) to evaluate  | `{f}` `{$o}`
    || Allows for missing `{}` in functions | `f()` `$p`
    || Defaults to the last [input prompt ✏️](<../../../../🤔 Prompts/🤔⚙️ Prompt features/9 ✏️ as Input.md>) | `TEXT\|Id?`
    | `<true-script>` | [Script 📃](<../RUN ▶️/RUN ▶️.md>) when `True` | `IfTrue`
    
    
    ---
    <br/>


1. **What's the IF syntax for one-line scripts?**
    
    ```yaml
    # One-line Scripts
    - IF|{function}|<true-script>|<false-script>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `{function}` | Boolean [{Function}](<../../...functions 🐍/{Function} 🐍.md>) to evaluate  | `{f}` `{$o}`
    || Allows for missing `{}` in functions | `f()` `$p`
    || Defaults to the last [input prompt ✏️](<../../../../🤔 Prompts/🤔⚙️ Prompt features/9 ✏️ as Input.md>) | `TEXT\|Id?`
    | `<true-script>` | [Script 📃](<../RUN ▶️/RUN ▶️.md>) when `True` | `IfTrue`
    | `<false-script>`| [Script 📃](<../RUN ▶️/RUN ▶️.md>) when `False` | `IfFalse(X)`
    
    ---
    <br/>

1. **What's the IF syntax for multi-line actions?**

    ```yaml
    # Multi-line actions: 
    #   i.e., Script or one-line Command

    - IF: 
        Function: {function} # (empty) → last input
        Then: <true-action>
        Else: <false-action>
    ```

    | Argument| Purpose
    |-|-
    | `<true-action>` | [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) or one-lin⌘ [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) on `True`
    | `<false-action>`| [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) or one-line [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) on `False`

    ---
    <br/>

1. **What's the IF syntax for multi-line command lists?**

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
    | `<true-cmd-n>` | List of multi-line [Commands ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) to run on `True`
    | `<false-cmd-n>` | List of multi-line [Commands ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) to run on `False`

    ---
    <br/>


1. **What are examples of inline syntax?**


    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Test started
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ Code is correct!
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Test finished


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

    
    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Test started
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ Code is correct!
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Test finished


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

