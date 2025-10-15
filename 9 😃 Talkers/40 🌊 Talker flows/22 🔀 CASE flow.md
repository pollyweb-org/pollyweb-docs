# 🔀 Talker `CASE` flow 

> Part of [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>)

<br/>


1. **What's a CASE flow?**

    A `CASE` 🔀
    * is a flow [Command ⌘](<10 ⌘ Command.md>)  
    * that runs a matching [Procedure ⚙️](<11 ⚙️ Procedure.md>) or [Command ⌘](<10 ⌘ Command.md>) 
    * based on the evaluation of a [{Function}](<../30 🗃️ Talker data/12 🐍 {Function}.md>).

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
    | `{function}` | Optional [{Function}](<../30 🗃️ Talker data/12 🐍 {Function}.md>) to evaluate | `{f}` `{$p}`
    || Allows for missing `{}` in functions | `f()` `$p`
    || Defaults to the last [input prompt ✏️](<../20 🤔 Prompts/1 📘 Prompt specs/09 ✏️ as Input.md>) | `TEXT\|Id?`
    | `<value>`| Static value to be matched with. | `ABC`
    | `<action>`| Run a [Procedure ⚙️](<11 ⚙️ Procedure.md>) | `MyProc`
    || or a one-line [Command ⌘](<10 ⌘ Command.md>). | `INFO\|OK`
    

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
    | `<cmd-n>`| Run a multi-line [Command ⌘](<10 ⌘ Command.md>) list.
    

    ---
    <br/>

1. **What's an example with function logic?**

    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | ℹ️ Hi, premium customer!
    |

    Here's the [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>).

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


    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/$ 👥 Domain.md>) | [Prompt](<../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | 😃 [Select an option.](<../20 🤔 Prompts/7 ✏️ Input prompts/53 1️⃣ ONE prompt.md>) <br/> - [ A ] <br/> - [ B ] <br/> - [ C ] | > B
    | [🤗 Host](<../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/$ 🤗🎭 Host role.md>) | ℹ️ You selected option B.
    |

    Here's the [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>).
   
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