# ▶️ Talker `RETURN` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a RETURN flow?**

    A `RETURN` 
    * is a flow [Command](<10 Command.md>) 
    * that exists a [Procedure](<20 ⚙️ Procedure block.md>) to its parent, 
    * and returns one of the following expressions.
    
    |Expression|Examples
    |-|-
    |`<string>`| `3` `Alice`
    [`{Function}`](<11 {Function} command.md>) | `{$placeholder}` `{handler(1)}` `{.helper(1)}` 

    ---
    <br/>





2. **What's the RETURN syntax?**

    ```yaml
    - RETURN[|<expression>]
    ```

    | Argument| Purpose
    |-|-
    | `<expression>`| Optional string or [{Function}](<11 {Function} command.md>) to be evaluated.
    
    ---
    <br/>



2. **What happens after a RETURN?**

    Nothing runs on a [Procedure](<20 ⚙️ Procedure block.md>) after the `RETURN`.

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ No failure occurred.
    

    ```yaml
    # 😃 Talker 

    💬 Example:
    - RUN|Test 
    - SUCCESS|No failure occurred.
    
    Test:
    - RETURN
    - FAILURE|This command never runs.
    ```

    ---
    <br/>


2. **How to read the result from a RETURN?**



    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ String return `Bla Bla`
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Placeholder return `123`
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Function return 1+2+3= `6`
    

    ```yaml
    # 😃 Talker 

    💬 Example:
    - RUN|StringProc >> result
    - INFO|String return `{$result}`
    - RUN|PlaceholderProc(123) >> result
    - INFO|Placeholder return `{$result}`
    - RUN|FunctionProc(1,2,3) >> result
    - INFO|Function return 1+2+3= {$result}

    StringProc:
    - RETURN|Bla Bla

    PlaceholderProc:
    - RETURN|{$1}

    FunctionProc:
    - RETURN|{.Sum($1,$2,$3)}
    ```

    ---
    <br/>

