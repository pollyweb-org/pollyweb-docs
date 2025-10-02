# Talker `{function}` 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What's a Talker {function}?**

    It's a string encapsulated in brackets that calculates a value:
    - either from a input placeholders;
    - or from code handlers (e.g., python).

    ---
    <br/>
    


3. **What's syntax for input placeholders?**

    ```yaml
    {$placeholder} 
    ```

    | Argument| Purpose
    |-|-
    | `placeholder` | The name of a placeholder.

    ```yaml
    💬 Example:
    - QUANTITY|Give me a number. >> my-var
    - INFO|You gave me the number {$my-var}.
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Give me a number.  | 🔄 5
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You gave me the number 5.

    ---
    <br/>
   


2. **What's the syntax for code handlers?**

    ```yaml
    {function[(param-1[,param-n])]}
    ```

    | Argument| Purpose
    |-|-
    | `function` | Key for the code handler.
    | `param-1`  | Optional parameter.
    | `param-n`  | Additional comma-separated parameters.

    ---
    <br/>

2. **What are examples of code invocations?**
   
    | Example | Details
    |-|-
    | `{f}` | Evaluates a function named `f`.
    | `{f(Alice)}` | Evaluates `f`, passing the string `Alice`.
    | `{f($name)}` | Passes the value of the `name` placeholder.
    | `{f($x,$y,$z)}` | Passes `x`, `y`, and `z` placeholder values.

    ---
    <br/> 


4. **How to code function handlers?**

    ```python
    # Python handler
    def talkerHandler(args):
      match args['function']:
        case 'Sum':
          return sum(args['parameters'])
    ```

    ```yaml
    # Talker configuration
    💬 Example:
    - INFO|No numbers equals {Sum}
    - INFO|1+2+3 equals {Sum(1,2,3)}
    - QUANTITY|Give me a number >> n
    - INFO|{$n}+{$n} equals {Sum($n,$n)}
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ No numbers equals 0
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ 1+2+3 equals 6
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Give me a number |  🔄 4
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ 4+4 equals 8

    ---
    <br/>


3. **What is passed down to code handlers?**

    | Component | Details | Example
    |-|-|-
    |`function`  | Function name  | `f` in `{f(1,2,3)}`
    |`parameters`| Parameter list | `[1,2,3]` in `{f(1,2,3)}`


    ---
    <br/>