# Talker `REPEAT` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a REPEAT flow?**

    A `REPEAT` is a [Command](<10 Command.md>) that repeats it's enclosing [Procedure](<12 Procedure block.md>) if confirmed.

    ---
    <br/>

2. **What's the syntax?**

    ```yaml
    - REPEAT|<message>
    ```

    | Argument| Purpose
    |-|-
    | `message>`| Optional message for a [CONFIRM 👍 prompt](<../13 🤔 Prompts/24 👍 CONFIRM prompt.md>)
    
    ---
    <br/>

3. **What's an example with a message?**


    ```yaml
    💬|The [menu]:
    - RUN|ShowMenu

    ShowMenu:
    - ONE|Which menu?|Drinks,Mains,Desserts >> menu
    - INFO|Here's the menu.|{get-menu($menu)}
    - REPEAT|Another menu?


    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- The [menu] | > menu
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Ready to order? [Yes, No] | > Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Hi David! I'm sad.

    ---
    <br/>

4. **What's an example without a message?**

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

