# Talker `{function}` 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What's a Talker {function}?**

    It's a string encapsulated in brackets that calculates a value.

    ---
    <br/>
    

2. **What's the syntax for code handlers?**

    ```yaml
    {function} 
    ```

    | Argument| Purpose
    |-|-
    | `function` | Key for the code handler.

    ```yaml
    # Talker configuration
    💬 Example:
    - INFO|{return-some-text}:
    ```

    ```python
    # Python handler
    def talkerHandler(args):
        if args['function'] == 'return-some-text':
            return "Some text"
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Some text 

    ---
    <br/>

3. **What's syntax for placeholder values?**

    ```yaml
    {$placeholder} 
    ```

    | Argument| Purpose
    |-|-
    | `placeholder` | The name of a placeholder.

    ```yaml
    💬 Example:
    - QUANTITY|Give me a number. >> my-var
    - INFO|You gave me number {$my-var}
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Give me a number.  | 🔄 27
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You gave me number 27

    ---
    <br/>
   