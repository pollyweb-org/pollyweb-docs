# 🔀 Talker `CASE` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a CASE flow?**

    A `CASE` 🔀
    * is a flow [Command ⌘](<10 ⌘ Command.md>)  
    * that runs a matching [Procedure ⚙️](<11 ⚙️ Procedure.md>) or [Command ⌘](<10 ⌘ Command.md>) 
    * based on the evaluation of a [{Function}](<12 🐍 {Function}.md>).

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    # One line values
    - CASE|{function}:
        $: <action-$>
        <value-1>: <action-1>
        <value-n>: <action-n>
        
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
    | `{function}` | Optional [{Function}](<12 🐍 {Function}.md>) to evaluate; <br/>- defaults to the last input.
    | `<value-n>`| Static value to be matched with.
    | `$` |  if unmatched with any other value.
    | `<action-n>`| Run a [Procedure ⚙️](<11 ⚙️ Procedure.md>) or one-line [Command ⌘](<10 ⌘ Command.md>).
    | `<cmd-n>`| Run a multi-line [Command ⌘](<10 ⌘ Command.md>) list.
    

    ---
    <br/>

1. **What's an example with function logic?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Hi, premium customer!

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


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 [Select an option.](<../31 🤔 Prompts/25 1️⃣ ONE prompt.md>) <br/> - [ A ] <br/> - [ B ] <br/> - [ C ] | > B
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ You selected option B.
    
   
    ```yaml
    # 😃 Talker

    💬 Example:
    - ONE|Select an option.|A,B,C >> $x
    - CASE:
        B: INFO|You selected option B.
        $: WhenUnmatched

    WhenUnmatched:
    - INFO|You selected option {$x}.
    ```

    ---
    <br/>