# 🐍 Talker `{Function}` 

> Part of [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>)

<br/>

1. **What's a Talker {Function}?**

    A [{Function}](<12 🐍 {Function}.md>) 
    * is a string encapsulated in brackets 
    * that calculates one if the following values.

    |Format|Details
    |-|-
    | `{$placeholder}`| The value of a [$placeholder 💾](<10 💾 $Placeholder.md>).
    | `{/path/to/file}` | A file in the [Hoster ☁️](<../../4 ⚙️ Solution/45 🛠️ Helper domains/55 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>) file system.
    | `{handler(args)}`| Logic in a code handler - e.g., python.
    | `{.helper(args)}`| Pre-built functions - e.g., `Sum()`
    

    ---
    <br/>
    


1. **What's syntax for input placeholders?**


    <br/>
    
    Consider the following [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>).
    
    ```yaml
    # 😃 Talker 
    EVAL >> $p
        $: my default
        A: another property

    INFO|{$p}   # Prints "my default"
    INFO|{$p.$} # Prints "my default"
    INFO|{$p.A} # Prints "another property"
    ```

    | [Command ⌘](<../40 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
    |-|-
    | ⬇️ [`EVAL`](<20 ⬇️ EVAL flow.md>) | To push an object into a [$placeholder 💾](<10 💾 $Placeholder.md>).
    | ℹ️ [`INFO`](<../20 🤔 Prompts/4 ⚠️ Status prompts/21 ℹ️ INFO prompt.md>) | To show the placeholder values.
    
    ---
    <br/>


    

1. **What's an example for input placeholders?**
   
    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | 😃 Give me a quantity  | ↕️ 1234
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | ℹ️ I'm saving `1,234`
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | ℹ️ Although you typed `1234`
    |

    <br/>
    
    Here's the [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>).
        
    ```yaml
    # 😃 Talker 
    💬 Example:
    - QUANTITY|Give me a quantity >> $n
    - INFO|I'm saving `{$n}`
    - INFO|Although you typed `{$n.Text}`
    ```

    | [Command ⌘](<../40 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<../20 🤔 Prompts/4 ⚠️ Status prompts/21 ℹ️ INFO prompt.md>) | To show the [$placeholder 💾](<10 💾 $Placeholder.md>) values.
    | ↕️ [`QUANTITY`](<../20 🤔 Prompts/7 ✏️ Input prompts/42 ↕️ QUANTITY prompt.md>) | To collect the number input.
    

    ---
    <br/>
   

1. **What's syntax for files?**

    ```yaml
    # Static paths
    {/path/to/file} 

    # Dynamic paths
    {{function}}
    ```

    | Argument| Purpose
    |-|-
    | `/path/to/file` | Path to a file in the [Hoster ☁️](<../../4 ⚙️ Solution/45 🛠️ Helper domains/55 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>) folders.
    | `{function}` | Function that evaluates to a path.

    ---
    <br/>
   

1. **What's an example for files?**


    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | 💬 [Who is in the picture?](<../20 🤔 Prompts/7 ✏️ Input prompts/32 🔠 TEXT prompt.md>) 🖼️ | `Elvis`


    ```yaml
    # 😃 Talker configuration
    💬 Example:
    TEXT|Who is in the picture?:
        Appendix: {/photos/elvis.png}
    ```
    
    ---
    <br/>

1. **What's the syntax for code handlers?**

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



1. **What's an example of code handlers?**



    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | ℹ️ No numbers equals 0
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | ℹ️ 1+2+3 equals 6
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | 😃 Give me a number |  ↕️ 4
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | ℹ️ 4+4 equals 8



    ```yaml
    # 😃 Talker configuration
    💬 Example:
    - INFO|No numbers equals {Sum}
    - INFO|1+2+3 equals {Sum(1,2,3)}
    - QUANTITY|Give me a number >> $n
    - INFO|{$n}+{$n} equals {Sum($n,$n)}
    ```

    | [Command ⌘](<../40 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
    |-|-
    | ↕️ [`QUANTITY`](<../20 🤔 Prompts/7 ✏️ Input prompts/42 ↕️ QUANTITY prompt.md>) | To collect the number input.


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
    | `{f($p)}` | ✅ Passes the `$p` placeholder.
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

1. **How to dump code handler invocations for debugging?**
   
    

    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | ℹ️ You sent:<br/>- Function: MyFunction <br>- Inputs: [1, 2, 3] <br/>- Input: 1
    

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



1. **What's the syntax for built-in helper functions?**

    ```yaml
    {.helper(params)}
    ```

    | Argument| Purpose
    |-|-
    | `.helper`  | Name of the built-in helper function.
    | `params`  | Optional comma-separated parameters.

    ---
    <br/>


1. **What are examples of built-in helper functions?**

    | Function | Details | Example
    |-|-|-
    | `.Sum` | Sums numbers | `{.Sum(1,2,3)}` → `6`
    | `.Subtract` | Subtracts B from A | `{.Subtract(10,4)}` → `6`
    | `.Multiply` | Multiplies numbers | `{.Multiply(2,3,4)}` → `24`
    | `.RandomInt` | Random integer | `{.RandomInt(1,9)}` → `7`
    | `.InRange` | Checks intervals | `{.InRange(5,1,10)}` → `True`
    | `.Time` | Current time | `{.Time}` → `10:30:00Z`
    
    ---
    <br/>
