# 🐍 Talker `{Function}` 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What's a Talker {Function}?**

    A [{Function}](<12 🐍 {Function}.md>) 
    * is a string encapsulated in brackets 
    * that calculates one if the following values.

    |Format|Details
    |-|-
    | `{$placeholder}`| The result of a named user input.
    | `{/path/to/file}` | A file in the [Hoster 🧑‍💻](<../12 💬 Chats/05 🧑‍💻🛠️ Hoster helper.md>) file system.
    | `{handler(args)}`| Logic in a code handler - e.g., python.
    | `{.helper(args)}`| Pre-built functions - e.g., `Sum()`
    

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
   
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Give me a number.  | 🔄 5
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You gave me the number 5.


    ```yaml
    # 😃 Talker configuration
    💬 Example:
    - QUANTITY|Give me a number. >> $n
    - INFO|You gave me the number {$n}.
    ```

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | 🔄 [`QUANTITY`](<../13 🤔 Prompts/21 🔄 QUANTITY prompt.md>) | To collect the number input.

    ---
    <br/>
   

3. **What's syntax for files?**

    ```yaml
    # Static paths
    {/path/to/file} 

    # Dynamic paths
    {{function}}
    ```

    | Argument| Purpose
    |-|-
    | `/path/to/file` | Path to a file in the [Hoster 🧑‍💻](<../12 💬 Chats/05 🧑‍💻🛠️ Hoster helper.md>) folders.
    | `{function}` | Function that evaluates to a path.

    ---
    <br/>
   

3. **What's an example for files?**


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 💬 [Who is in the picture?](<../13 🤔 Prompts/20 🔠 TEXT prompt.md>) 🖼️ | `Elvis`


    ```yaml
    # 😃 Talker configuration
    💬 Example:
    TEXT|Who is in the picture?:
        Attachment: {/photos/elvis.png}
    ```
    
    ---
    <br/>

4. **What's the syntax for code handlers?**

    ```yaml
    {handler[(param-1[,param-n])]}
    ```

    | Argument| Purpose
    |-|-
    | `handler`  | Name of the code handler.
    | `param-1`  | Optional parameter.
    | `param-n`  | Additional comma-separated parameters.

    ---
    <br/>



4. **What's an example of code handlers?**



    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ No numbers equals 0
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ 1+2+3 equals 6
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Give me a number |  🔄 4
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ 4+4 equals 8



    ```yaml
    # 😃 Talker configuration
    💬 Example:
    - INFO|No numbers equals {Sum}
    - INFO|1+2+3 equals {Sum(1,2,3)}
    - QUANTITY|Give me a number >> $n
    - INFO|{$n}+{$n} equals {Sum($n,$n)}
    ```

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | 🔄 [`QUANTITY`](<../13 🤔 Prompts/21 🔄 QUANTITY prompt.md>) | To collect the number input.


    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['Function']:
        case 'Sum':
          return sum(args['Inputs'])
    ```

    ---
    <br/>

6. **What are examples of code invocations?**
   
    | Example | Details
    |-|-
    | `{f}` | ✅ Evaluates a function named `f`.
    | `{f(C)}` | ✅ Evaluates `f` with constant `C`.
    | `{f($p)}` | ✅ Passes the `$p` placeholder.
    | `{f(C,$p)}` | ✅ Passes `C` and `$p` in positions.
    | `{f([C,$p])}` |  ✅ Passes `C` and `$p` as a list. 
    | `{f({a:1,b:$p}}` |  ✅ Passes `{a,b}` dictionary. 
    
    ---
    <br/> 

7. **What is passed down to code handlers?**

    | Component | Details | Example
    |-|-|-
    |`function`  | Function name  | `f` in `{f(1,2,3)}`
    |`inputs`| Parameter list | • `[]` in `{f}` (no parameters) <br/> • `[1,2,3]` in `{f(1,2,3)}`
    |`input`| The first parameter | `{a:1,b:2}` <br/> in `{f({a:1,b:2})}`

    ---
    <br/>

8. **How to dump code handler invocations for debugging?**
   
    

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You sent:<br/>- Function: MyFunction <br>- Inputs: [1, 2, 3] <br/>- Input: 1
    

    ```yaml
    # 😃 Talker configuration
    💬 Example:
    - INFO|{MyFunction(1,2,3)}
    ```
    
    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      return "\n".join([
        f"You sent:",
        f"- Function: {args['Function']}",
        f"- Inputs: {args['Inputs']}"
        f"- Input: {args['Input']}"
      ])
    ```


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



5. **What's the syntax for built-in helper functions?**

    ```yaml
    {.helper(params)}
    ```

    | Argument| Purpose
    |-|-
    | `.helper`  | Name of the built-in helper function.
    | `params`  | Optional comma-separated parameters.

    ---
    <br/>


5. **What are examples of built-in helper functions?**

    | Function | Details | Example
    |-|-|-
    | `.Sum` | Sums numbers | `{.Sum(1,2,3)}` → `6`
    | `.Subtract` | Subtracts B from A | `{.Subtract(10,4)}` → `6`
    | `.Multiply` | Multiplies numbers | `{.Multiply(2,3,4)}` → `24`
    | `.RandomInt` | Random integer | `{.RandomInt(1,9)}` → `7`
    | `.InRange` | Checks intervals | `{.InRange(5,1,10)}` → `True`
    | `.Time` | Current time | `{.Time}` → `10:30:00Z`
    | `.ChatKey`| [Locator 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) Key | `{.ChatKey}` → `ANY-KEY`
    


    ---
    <br/>
