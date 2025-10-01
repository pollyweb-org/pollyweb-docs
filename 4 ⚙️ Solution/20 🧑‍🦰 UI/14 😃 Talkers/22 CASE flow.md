* `CASE|{function}`	
    * Calculates something to be used in cases.
    * Without a function, uses the last answer.
    * Without cases, evaluates and discards.
* `CASE|<eval>|<anchor>`	
    * Runs a procedure when the eval is matched 
        ```yaml
        # Example
        💬| I need a table:
        - INT|How many people? >> qt
        - EVAL|{availability}
        - CASE|AVAILABLE|Available
        - CASE|WAIT|Wait
        - CASE|FULL|Full
        ```

    ---
    <br/>

4. **What's syntax for equal comparisons?**

    ```yaml
    CASE {function}|<default-procedure>:
        <value-1>: <procedure-1>
        <value-n>: <procedure-n>
    ```

    | Argument| Purpose
    |-|-
    | `{function}` | Required [Function](<12 Function block.md>) to evaluate.
    | `<default-procedure>` | Optional [Procedure](<11 Procedure block.md>) to execute when not matched.
    | `<value-n>`| Static value to be compared with.
    | `<procedure-n>`| [Procedure](<11 Procedure block.md>) to execute when matched.

    ```yaml
    💬 Example:
    - ONE|Select an option.|A,B,C >> my-var
    - CASE|{$my-var==B}:
        Then: INFO|You selected option B
        Else: INFO|You selected something else
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Select an option. <br/> - [ A ] <br/> - [ B ] <br/> - [ C ] | > B
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You selected option B
    
    ---
    <br/>