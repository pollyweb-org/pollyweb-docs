# 😃⏯️️ Talker `CASE` flow 

> Part of [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>)

<br/>


1. **What's a CASE flow?**

    A `CASE` ⏯️️
    * is a flow [Command ⌘](<../../📃 basics/⌘ Command.md>)  
    * that runs a matching [Script 📃](<../../📃 basics/📃 Script.md>) or [Command ⌘](<../../📃 basics/⌘ Command.md>)
    * based on the evaluation of a [{Function}](<../../📃 functions 🐍/{Function} 🐍.md>).

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    # Simplest
    - CASE|{function}:
        <value>: <action>
    ```


    | Input| Purpose | Example
    |-|-|-
    | `{function}` | Optional [{Function}](<../../📃 functions 🐍/{Function} 🐍.md>) to evaluate | `{f}` `{$p}`
    || Allows for missing `{}` in functions | `f()` `$p`
    || Defaults to the last [input prompt ✏️](<../../../Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>) | `TEXT\|Id?`
    | `<value>`| Static value to be matched with. | `ABC`
    | `<action>`| Run a [Script 📃](<../../📃 basics/📃 Script.md>) | `MyProc`
    || or a one-line [Command ⌘](<../../📃 basics/⌘ Command.md>). | `INFO\|OK`
    
    <br/>

    ```yaml
    # One line values
    - CASE|{function}:
        $: <action-$>
        <value-1>: <action-1>
        <value-n>: <action-n>
    ```

    | Input| Purpose
    |-|-
    | `$` | Catch-all clause if unmatched with any other value.
    
    <br/>

    ```yaml 
    # Multi-line values
    - CASE|{function}:
        $: 
            - <cmd-$>
        <value-1>: 
            - <cmd-1>
            - <cmd-2>
        <value-n>: 
            - <cmd-n>
    ```

    | Input| Purpose
    |-|-
    | `<cmd-n>`| Run a multi-line [Command ⌘](<../../📃 basics/⌘ Command.md>) list.
    
    <br/>

    ```yaml 
    # Attributions
    - CASE|$input >> $output:
        <when-1>: <then-1>
        <when-n>: <then-n>
    ```

    | Input| Purpose
    |-|-
    | `$input`  | Value to evaluate            | `1,2,3`
    | `<when>`  | Constant to match against     | `1`
    | `<then>`  | Resulting output if matched   | `one`
    | `$output` | Output [Holder 🧠](<../../📃 holders 🧠/$Holder 🧠.md>)  | -

    ---
    <br/>

1. **What's an example with function logic?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Hi, premium customer!
    |

    Here's the [Script 📃](<../../📃 basics/📃 Script.md>).

    ```yaml
    # 😃 Talker

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
      match args['Function']:
        case 'customer-type':
          return context.CustomerType
    ```

    ---
    <br/>

1. **What's an example with inputs?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 [Select an option.](<../../../Prompts 🤔/🤔✏️ Prompt inputs/ONE 1️⃣/ONE 1️⃣ prompt.md>) <br/> - [ A ] <br/> - [ B ] <br/> - [ C ] | > B
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ You selected option B.
    |

    Here's the [Script 📃](<../../📃 basics/📃 Script.md>).
   
    ```yaml
    # 😃 Talker

    💬 Example:

    - ONE >> $x:
        Text: Select an option.
        Options: A,B,C 

    - CASE: # Default to last input.
        B: INFO|You selected option B.
        $: WhenUnmatched

    WhenUnmatched:
    - INFO|You selected option {$x}.
    ```
    Commands: [`INFO`](<../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>

1. **What's an example of an attribution?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Number from 1 to 3? | `3`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ You said `three`
    |

    <br/>

    Here's the [Script 📃](<../../📃 basics/📃 Script.md>)

    ```yaml 
    # Collect a number
    - DIGITS|Number from 1 to 3? >> $input

    # Translate the number
    - CASE|$input >> $output:
        1: one
        2: two
        3: three

    # Show the translation 
    - INFO|You said `{$output}`
    ```    
    Commands: [`DIGITS`](<../../../Prompts 🤔/🤔✏️ Prompt inputs/DIGITS 🔢/DIGITS 🔢 prompt.md>) [`INFO`](<../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>