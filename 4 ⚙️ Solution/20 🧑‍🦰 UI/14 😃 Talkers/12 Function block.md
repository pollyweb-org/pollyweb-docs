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

3. **What's syntax for equal comparisons?**

    ```yaml
    {:var==value} 
    ```

    | Argument| Purpose
    |-|-
    | `var` | The name of a variable.
    | `value`| The value to be compared with.

    ```yaml
    💬 Example:
    - ONE|Select an option.|A,B,C >> my-var
    - IF|{:my-var==B}:
        Then: INFO|You selected option B
        Else: INFO|You selected something else
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Select an option. <br/> - [ A ] <br/> - [ B ] <br/> - [ C ] | > B
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You selected option B
    
    ---
    <br/>