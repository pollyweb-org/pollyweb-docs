# 🔀 Talker `CASE` flow 

> Part of [Talker 😃](<../../😃 Talker.md>)

<br/>


1. **What's a CASE flow?**

    A `CASE` 🔀
    * is a flow [Command ⌘](<⌘ Command.md>)  
    * that runs a matching [Procedure ⚙️](<⚙️ Procedure.md>) or [Command ⌘](<⌘ Command.md>) 
    * based on the evaluation of a [{Function}](<../for data/{Function} 🐍.md>).

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    # Simplest
    - CASE|{function}:
        <value>: <action>
    ```


    | Argument| Purpose | Example
    |-|-|-
    | `{function}` | Optional [{Function}](<../for data/{Function} 🐍.md>) to evaluate | `{f}` `{$p}`
    || Allows for missing `{}` in functions | `f()` `$p`
    || Defaults to the last [input prompt ✏️](<../../../🤔 Prompts/🤔⚙️ Prompt features/9 ✏️ as Input.md>) | `TEXT\|Id?`
    | `<value>`| Static value to be matched with. | `ABC`
    | `<action>`| Run a [Procedure ⚙️](<⚙️ Procedure.md>) | `MyProc`
    || or a one-line [Command ⌘](<⌘ Command.md>). | `INFO\|OK`
    

    ```yaml
    # One line values
    - CASE|{function}:
        $: <action-$>
        <value-1>: <action-1>
        <value-n>: <action-n>
    ```

    | Argument| Purpose
    |-|-
    | `$` | Catch-all clause if unmatched with any other value.
    
    

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

    | Argument| Purpose
    |-|-
    | `<cmd-n>`| Run a multi-line [Command ⌘](<⌘ Command.md>) list.
    

    ---
    <br/>

1. **What's an example with function logic?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Hi, premium customer!
    |

    Here's the [Talker 😃](<../../😃 Talker.md>).

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


    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 [Select an option.](<../../../🤔 Prompts/🤔✏️ Prompt inputs/53 1️⃣ ONE prompt.md>) <br/> - [ A ] <br/> - [ B ] <br/> - [ C ] | > B
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ You selected option B.
    |

    Here's the [Talker 😃](<../../😃 Talker.md>).
   
    ```yaml
    # 😃 Talker

    💬 Example:

    - ONE >> $x:
        Statement: Select an option.
        Options: A,B,C 

    - CASE: # Default to last input.
        B: INFO|You selected option B.
        $: WhenUnmatched

    WhenUnmatched:
    - INFO|You selected option {$x}.
    ```

    ---
    <br/>