# 😃 Talker `CASE` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a CASE flow?**

    A `CASE` is a flow [Command](<10 Command.md>)  that runs a matching [Procedure](<12 Procedure block.md>) or [Command](<10 Command.md>) based on the evaluation of a [{Function}](<15 Function command.md>).

    ---
    <br/>

4. **What's the syntax?**

    ```yaml
    - CASE|{function}:
        <value-1>: <action-1>
        <value-n>: <action-n>
        *: <default-action>
    ```

    | Argument| Purpose
    |-|-
    | `{function}` | Optional [Function](<15 Function command.md>) to evaluate; <br/>- defaults to the last input.
    | `<value-n>`| Static value to be compared with.
    | `<action-n>`| Run [Procedure](<12 Procedure block.md>) or [Command](<10 Command.md>) when matched.
    | `<default-action>` | Run [Procedure](<12 Procedure block.md>) or [Command](<10 Command.md>) if unmatched.
    

    ---
    <br/>

4. **What's an example with function logic?**


    ```yaml
    💬 Example:
    - CASE|{customer-type}:
        STANDARD: ShowStandardOptions
        ADVANCED: ShowAdvancedOptions
        PREMIUM: ShowPremiumOptions

    ShowPremiumOptions:
    - INFO|Hi, premium customer!
    ```


    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['function']:
        case 'customer-type':
          return context.CustomerType
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Hi, premium customer!

    ---
    <br/>

5. **What's an example with inputs?**

    > The `{function}` defaults to the last input.
   
    ```yaml
    💬 Example:
    - ONE|Select an option.|A,B,C >> my-var
    - CASE:
        B: INFO|You selected option B.
        *: WhenUnmatched

    WhenUnmatched:
    - INFO|You selected option {$my-var}.
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Select an option. <br/> - [ A ] <br/> - [ B ] <br/> - [ C ] | > B
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You selected option B.
    
    ---
    <br/>