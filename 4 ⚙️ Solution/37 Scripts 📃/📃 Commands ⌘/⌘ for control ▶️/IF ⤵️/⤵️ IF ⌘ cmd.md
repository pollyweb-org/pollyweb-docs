# 😃⤵️ Talker `IF` flow 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<br/>


1. **What's an IF flow?**

    An `IF` ⤵️
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  
    * that runs a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) or [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)
    * based on the evaluation of a holder or [{Function}](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>).

    ---
    <br/>

1. **What's the IF syntax for then-only IFs?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    ```yaml
    IF:
        Assert: assertions... # Optionally, last user input
        Then: commands...     # Optional
        Else: commands...     # Optional
    ```

    | Input| Purpose | Example
    |-|-|-
    | `Assert` | List of inputs to [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>)  | `$h` `.f(*)`
    || Defaults to last [input prompt ✏️](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>) | [`CONFIRM`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) [`TEXT`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 💬/🔠 TEXT ⌘ cmd.md>)
    | `Then` | List of [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) if `True` | [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)` 123`
    | | Or a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) name to [`RUN`](<../RUN 🏃/🏃 RUN ⌘ cmd.md>) | `If-True-Script`
    | `Else` | List of [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) if `False` | [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)` 456`
    | | Or a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) name to [`RUN`](<../RUN 🏃/🏃 RUN ⌘ cmd.md>) | `If-False-Script`
    

    ---
    <br/>

1. **What are alternative syntaxes?**
    
    ```yaml
    # Inline then 
    - IF|<assertion>|<then-script>
    ```

    ```yaml
    # Inline then else
    - IF|<assertion>|<then-script>|<else-script>
    ```

    ```yaml
    # Broken-line single then (a text)
    - IF|<assertion>:
        <then>
    ```

    ```yaml
    # Multiple then-actions (a list)
    - IF|<assertion>:
        - <then-1>
        - <then-n>
    ```
    
    ---
    <br/>



1. **What are examples of inline syntax?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Test started
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Code is correct!
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Test finished


    ```yaml
    # 😃 Talker with inline IF-THEN (no ELSE).

    💬 If-then example:
    - INFO|Test started
    - IF|{code-is-correct}|CorrectCode
    - INFO|Test finished

    CorrectCode:
    - DONE|Code is correct!
    ```

    ```yaml
    # 😃 Talker with inline IF-THEN-ELSE.

    💬 If-then-else example:
    - INFO|Test started
    - IF|{code-is-correct}|CorrectCode|WrongCode
    - INFO|Test finished

    CorrectCode:
    - DONE|Code is correct!

    WrongCode:
    - FAIL|Code is wrong!
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

    
    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Test started
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Code is correct!
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Test finished


    ```yaml
    # 😃 Talker with multi-line IF-THEN (no ELSE).
    
    💬 If-them example:
    - INFO|Test started
    - IF|{code-is-correct}:
        Then: 
          - DONE|Code is correct!
          - INFO|Test finished
    ```

    ```yaml
    # 😃 Talker with multi-line IF-THEN-ELSE.

    💬 If-then-else example:
    - INFO|Test started
    - IF|{code-is-correct}:
        Then: DONE|Code is correct!
        Else: ErrorHandlingProcedure
    - INFO|Test finished
        
    ErrorHandlingProcedure:
    - FAIL|Code is wrong!
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
