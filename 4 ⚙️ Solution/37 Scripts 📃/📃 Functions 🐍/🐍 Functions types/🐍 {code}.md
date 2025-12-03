<!-- TODO: -->

# 🐍 {code} function

> About
* Part of [{Functions} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
* Implemented with the [`CALL` 🧮 command](<../../📃 Commands ⌘/⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>)
* Calls either an internal function 
  * or a function implemented in a [Hosted 📦 domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>)

## FAQ

1. **What's the syntax for code handlers?**

    ```yaml
    {handler[(param-1[,param-n])]}
    ```

    | Input| Purpose
    |-|-
    | `handler`  | Name of the code handler.
    | `param-1`  | Optional parameter.
    | `param-n`  | Additional comma-separated parameters.

    ---
    <br/>


1. **What's an example of code handlers?**



    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ No numbers equals 0
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ 1+2+3 equals 6
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Give me a number |  ↕️ 4
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ 4+4 equals 8



    ```yaml
    # 😃 Talker configuration
    💬 Example:
    - INFO|No numbers equals {Sum}
    - INFO|1+2+3 equals {Sum(1,2,3)}
    - QUANTITY|Give me a number >> $n
    - INFO|{$n}+{$n} equals {Sum($n,$n)}
    ```

    Uses: [`INFO`](<../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`QUANTITY`](<../../📃 Prompts 🤔/🤔 Input ✏️ prompts/QUANTITY ↕️/QUANTITY ↕️ prompt.md>)

    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['Function']:
        case 'Sum':
          return sum(args['Inputs'])
    ```

    ---
    <br/>

1. **What are examples of code invocations?**
   
    | Example | Details
    |-|-
    | `{f}` | ✅ Evaluates a function named `f`.
    | `{f(C)}` | ✅ Evaluates `f` with constant `C`.
    | `{f($p)}` | ✅ Passes the `$p` holder.
    | `{f(C,$p)}` | ✅ Passes `C` and `$p` in positions.
    | `{f([C,$p])}` |  ✅ Passes `C` and `$p` as a list. 
    | `{f({a:1,b:$p}}` |  ✅ Passes `{a,b}` dictionary. 
    
    ---
    <br/> 

1. **What is passed down to code handlers?**

    | Component | Details | Example
    |-|-|-
    |`function`  | Function name  | `f` in `{f(1,2,3)}`
    |`inputs`| Parameter list | • `[]` in `{f}` (no parameters) <br/> • `[1,2,3]` in `{f(1,2,3)}`
    |`input`| The first parameter | `{a:1,b:2}` <br/> in `{f({a:1,b:2})}`

    ---
    <br/>

1. **What's the syntax of a Function name?**

    No emojis nor special characters except dashes `-`, underscores `_`, and spaces ` `.
    * Emojis and special characters are reserved for current and future use.
    * Spaces are OK because only commas and pipes are used as separators.

    |Type|Example|
    |-|-
    |✅ Valid | `MyF` `My F` `myF` `my-f` `f2` `my_f`  `my--f` 
    |❌ Invalid | `{f}` `my$f` `$` `my-f!` `my/f` `my\|f` `my>f` `my,p` `👋`

    ---
    <br/>





1. **How to dump code handler invocations for debugging?**
   
    

    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ You sent:<br/>- Function: MyFunction <br>- Inputs: [1, 2, 3] <br/>- Input: 1
    |
    

    ```yaml
    # 😃 Talker configuration
    💬 Example:
    - INFO|{MyFunction(1,2,3)}
    ```

    Uses: [`INFO`](<../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)
    
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

