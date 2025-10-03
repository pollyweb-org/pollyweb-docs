# 🔁 Talker `REPEAT` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a REPEAT flow?**

    A `REPEAT` is a flow [Command](<10 Command.md>) that repeats it's enclosing [Procedure](<20 ⚙️ Procedure block.md>) if confirmed.

    ---
    <br/>

2. **What's the syntax?**

    ```yaml
    - REPEAT|<message>
    ```

    | Argument| Purpose
    |-|-
    | `<message>`| Optional message for a [CONFIRM 👍 prompt](<../13 🤔 Prompts/24 👍 CONFIRM prompt.md>)
    
    ---
    <br/>


3. **What's an example of a REPEAT with a message?**

    ```yaml
    💬|[Order] a list of items:
    - RUN|AddItems
    - SUCCESS|Order submitted!

    AddItems:
    - INT|What's the item code? >> code
    - REPEAT|Add another?
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Hi! What do you need? <br/>- [Order] a list of items | > Order
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the item code?  | 🔢 123
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Add another? [Yes, No] | > Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 What's the item code?  | 🔢 456
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Add another? [Yes, No] | > No
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ Order submitted!

    ---
    <br/>

4. **What's an example of a repeat without a message?**

    ```yaml
    💬 Play:
    - CONFIRM|Let's play?
    - RUN|Play

    Play:
    - QUANTITY|Guess a number >> n
    - CASE|{IsCorrect($n)}:
        TRUE: WIN
        FALSE: LOSE
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

-->