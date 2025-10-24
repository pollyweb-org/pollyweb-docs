<!-- TODO: -->

# 😃🧠 {$holder} function

> Part of [{Function} 🐍](<{Function} 🐍.md>)

<br/>

1. **What's syntax for input placeholders?**


    <br/>
    
    Consider the following [Talker 😃](<../../😃 Talker role.md>).
    
    ```yaml
    # 😃 Talker 
    EVAL >> $p
        $: my default
        A: another property

    INFO|{$p}   # Prints "my default"
    INFO|{$p.$} # Prints "my default"
    INFO|{$p.A} # Prints "another property"
    ```

    | [Command ⌘](<../... ⌘ commands/⌘ Command.md>) | Purpose
    |-|-
    | ⬇️ [`EVAL`](<../... placeholders 🧠/EVAL ⬇️ flow.md>) | To push an object into a [placeholder 🧠](<../... placeholders 🧠/$Placeholder 🧠.md>).
    | ℹ️ [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️ prompt.md>) | To show the placeholder values.
    
    ---
    <br/>



1. **What's an example for input placeholders?**
   
    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Give me a quantity  | ↕️ 1234
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ I'm saving `1,234`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Although you typed `1234`
    |

    <br/>
    
    Here's the [Script 📃](<../... ⌘ commands/📃 Script.md>).
        
    ```yaml
    # 😃 Talker 
    💬 Example:
    - QUANTITY|Give me a quantity >> $n
    - INFO|I'm saving `{$n}`
    - INFO|Although you typed `{$n.Text}`
    ```

    | [Command ⌘](<../... ⌘ commands/⌘ Command.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️ prompt.md>) | To show the [placeholder 🧠](<../... placeholders 🧠/$Placeholder 🧠.md>) values.
    | ↕️ [`QUANTITY`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/42 ↕️ QUANTITY prompt.md>) | To collect the number input.
    

    ---
    <br/>
   
