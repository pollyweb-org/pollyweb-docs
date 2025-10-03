# 😃 Talker `{function}` 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What's a Talker {function}?**

    It's a string encapsulated in brackets that calculates one if the following values.

    |Format|Details
    |-|-
    | `{$placeholder}`| The result of a named user input.
    | `{/path/to/file}` | A file in the [Hoster 🧑‍💻](<../12 💬 Chats/05 🧑‍💻🛠️ Hoster helper.md>) file system.
    | `{function}`| Logic in a code handler - e.g., python.
    

    ---
    <br/>
    


2. **What's syntax for input placeholders?**

    ```yaml
    {$placeholder} 
    ```

    | Argument| Purpose
    |-|-
    | `placeholder` | The name of a placeholder.

    ---
    <br/>

2. **What's an example for input placeholders?**
   
    ```yaml
    # 😃 Talker configuration
    💬 Example:
    - QUANTITY|Give me a number. >> my-var
    - INFO|You gave me the number {$my-var}.
    ```

    | Domain | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Give me a number.  | 🔄 5
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You gave me the number 5.

    ---
    <br/>
   

3. **What's syntax for files?**

    ```yaml
    {/path/to/file} 
    ```

    | Argument| Purpose
    |-|-
    | `/path/to/file` | The location in the [Hoster 🧑‍💻](<../12 💬 Chats/05 🧑‍💻🛠️ Hoster helper.md>) file system.

    ---
    <br/>
   

3. **What's an example for files?**

    ```yaml
    # 😃 Talker configuration
    💬 Example:
    TEXT|Who is in the picture?:
        Attachment: {/photos/elvis.png}
    ```

    | Domain | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 💬 Who is in the picture? 🖼️ | `Elvis`

    ---
    <br/>

4. **What's the syntax for code handlers?**

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



4. **What's an example of code handlers?**

    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['function']:
        case 'Sum':
          return sum(args['parameters'])
    ```

    ```yaml
    # 😃 Talker configuration
    💬 Example:
    - INFO|No numbers equals {Sum}
    - INFO|1+2+3 equals {Sum(1,2,3)}
    - QUANTITY|Give me a number >> n
    - INFO|{$n}+{$n} equals {Sum($n,$n)}
    ```

    | Domain | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ No numbers equals 0
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ 1+2+3 equals 6
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Give me a number |  🔄 4
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ 4+4 equals 8

    ---
    <br/>


5. **What are examples of code invocations?**
   
    | Example | Details
    |-|-
    | `{f}` | Evaluates a function named `f`.
    | `{f(Alice)}` | Evaluates `f`, passing the string `Alice`.
    | `{f($name)}` | Passes the value of the `name` placeholder.
    | `{f($x,$y,$z)}` | Passes `x`, `y`, and `z` placeholder values.

    ---
    <br/> 

3. **What is passed down to code handlers?**

    | Component | Details | Example
    |-|-|-
    |`function`  | Function name  | `f` in `{f(1,2,3)}`
    |`parameters`| Parameter list | • `[]` in `{f}` (no parameters) <br/> • `[1,2,3]` in `{f(1,2,3)}`

    ---
    <br/>

3. **How to dump code handler invocations for debugging?**
   
    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      return "\n".join([
        f"You sent:",
        f"- Function: {args['function']}",
        f"- Parameters: {args['parameters']}"
      ])
    ```

    ```yaml
    # 😃 Talker configuration
    - INFO|{MyFunction(1,2,3)}
    ```
    | Domain | Prompt | User
    
    | Domain | [Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You sent:<br/>- Function: MyFunction <br>- Parameters: [1, 2, 3]
    

    ---
    <br/>


4. **What's the syntax of a Function name?**

    No emojis nor special characters except dashes `-`, underscores `_`, and spaces ` `.
    * Emojis and special characters are reserved for current and future use.
    * Spaces are OK because only commas and pipes are used as separators.

    |Type|Example|
    |-|-
    |✅ Valid | `MyF` `My F` `myF` `my-f` `f2` `my_f`  `my--f` 
    |❌ Invalid | `{f}` `my$f` `$` `my-f!` `my/f` `my\|f` `my>f` `my,p` `👋`

    ---
    <br/>