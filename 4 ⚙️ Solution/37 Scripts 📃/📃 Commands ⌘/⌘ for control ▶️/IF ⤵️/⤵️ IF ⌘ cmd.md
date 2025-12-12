# 😃⤵️ Talker `IF` flow 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ


1. **What's an IF flow?**

    An `IF` ⤵️
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  
    * that evaluates of a holder or [{Function}](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
    * then either runs a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) or [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)
    * or delegates them to the [`THEN`](<../THEN ⤵️/⤵️ THEN ⌘ cmd.md>) and [`ELSE`](<../ELSE ⤵️/⤵️ ELSE ⌘ cmd.md>) commands.

    ---
    <br/>

1. **What's the IF syntax for then-only IFs?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    ```yaml
    IF:
        [assertions...] 
    ```

    | Input| Purpose | Example
    |-|-|-
    | `assertions` | List of inputs to [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>)  | `$h` `.f(*)`

    ```yaml
    IF <assertion>:
        [commands...]
    ```

    | Input| Purpose | Example
    |-|-|-
    | `commands...` | List of [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) if `True` | [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)` 123`
    

    ---
    <br/>

1. **What are alternative syntaxes?**
    
    ```yaml
    - IF: 
        <assertions...>
    ```

    ```yaml
    - IF <assertion>: <then>
    ```
    
    ```yaml
    - IF <assertion>:
        - <then-1>
        - <then-n>
    ```

    ```yaml
    - IF: <assertion>
    - THEN: <then-script>
    - ELSE: <else-script>
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
    - INFO: Test started
    - IF code-is-correct:
        RUN: CorrectCode
    - INFO: Test finished

    CorrectCode:
    - DONE: Code is correct!
    ```
    
    Uses: [`DONE`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`RUN`](<../RUN 🏃/🏃 RUN ⌘ cmd.md>)

    <br/>

    ```yaml
    # 😃 Talker with inline IF-THEN-ELSE.

    💬 If-then-else example:
    - INFO: Test started
    - IF: code-is-correct
    - THEN: RUN CorrectCode
    - ELSE: RUN WrongCode
    - INFO: Test finished

    CorrectCode:
    - DONE: Code is correct!

    WrongCode:
    - FAIL: Code is wrong!
    ```
    
    Uses: [`DONE`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) [`ELSE`](<../ELSE ⤵️/⤵️ ELSE ⌘ cmd.md>) [`FAIL`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`RUN`](<../RUN 🏃/🏃 RUN ⌘ cmd.md>) [`THEN`](<../THEN ⤵️/⤵️ THEN ⌘ cmd.md>)

    <br/>

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
    - INFO: Test started
    - IF code-is-correct:
        - DONE: Code is correct!
        - INFO: Test finished
    ```

    ```yaml
    # 😃 Talker with multi-line IF-THEN-ELSE.

    💬 If-then-else example:
    - INFO: Test started
    - IF: code-is-correct
    - THEN:
        DONE: Code is correct!
    - ELSE:
        RUN: ErrorHandlingProcedure
    - INFO: Test finished
        
    ErrorHandlingProcedure:
    - FAIL: Code is wrong!
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
