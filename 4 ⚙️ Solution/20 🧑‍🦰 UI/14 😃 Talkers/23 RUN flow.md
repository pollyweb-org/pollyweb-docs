# Talker `RUN` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a RUN flow?**

    A `RUN` is a [Command](<10 Command.md>) that runs a  [Procedure](<11 Procedure block.md>).

    ---
    <br/>

2. **What's the syntax?**

    ```yaml
    - RUN|<procedure>|<arguments>
    ```

    | Argument| Purpose
    |-|-
    | `procedure>`| [Procedure](<11 Procedure block.md>) to run.
    | `arguments`| Optional comma-separated arguments <br/>referenced by `{$position}`
    
    ---
    <br/>

3. **What's an example with arguments?**


    ```yaml
    💬 Example:
    - RUN|Great|Alice,happy
    - RUN|Great|David,sad

    Great:
    - INFO|Hi, {$1}! I'm {$2}.

    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Hi, Alice! I'm happy.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Hi David! I'm sad.

    ---
    <br/>

4. **What's an example with placeholders?**

    ```yaml
    💬 Example:
    - QUANTITY|Give me a number >> n
    - RUN|ShowNumber
    - QUANTITY|Give me another >> n
    - RUN|ShowNumber

    ShowNumber:
    - INFO|You gave me number {$n}.
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Give me a number | 🔄 12
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You gave me number 12
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Give me another | 🔄 34
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You gave me number 34
    
    ---
    <br/>



5. **What's an example with code?**

    ```yaml
    💬 Example:
    - EVAL|{get-random-number}
    - RUN|ShowNumber
    - EVAL|{get-random-number}
    - RUN|ShowNumber

    ShowNumber:
    - INFO|Here's number {$n}.
    ```

    ```python
    # Python handler
    def talkerHandler(args):
        match args['function']:
            case 'get-random-number':
                placeholders['n'] = randomNumber()
    ```


    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) |  ℹ️ Here's number  3512596
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) |  ℹ️ Here's number  523
    

    ---
    <br/>