<!-- TODO: -->

# 😃🧠 {$holder} function

> Part of [{Function} 🐍](<../📃 basics/Function 🐍.md>)

<br/>

1. **What's syntax for input placeholders?**


    <br/>
    
    Consider the following [Script 📃](<../📃 basics/Script 📃.md>).
    
    ```yaml
    # 😃 Talker 
    EVAL >> $p
        $: my default
        A: another property

    INFO|{$p}   # Prints "my default"
    INFO|{$p.$} # Prints "my default"
    INFO|{$p.A} # Prints "another property"
    ```

    | [Command ⌘](<../📃 basics/Command ⌘.md>) | Purpose
    |-|-
    | ⬇️ [`EVAL`](<../📃 holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) | To push an object into a [holder 🧠](<../📃 basics/Holder 🧠.md>).
    | ℹ️ [`INFO`](<../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) | To show the holder values.
    
    ---
    <br/>



1. **What's an example for input placeholders?**
   
    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Give me a quantity  | ↕️ 1234
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ I'm saving `1,234`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Although you typed `1234`
    |

    <br/>
    
    Here's the [Script 📃](<../📃 basics/Script 📃.md>).
        
    ```yaml
    # 😃 Talker 
    💬 Example:
    - QUANTITY|Give me a quantity >> $n
    - INFO|I'm saving `{$n}`
    - INFO|Although you typed `{$n.Text}`
    ```

    | [Command ⌘](<../📃 basics/Command ⌘.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) | To show the [holder 🧠](<../📃 basics/Holder 🧠.md>) values.
    | ↕️ [`QUANTITY`](<../../Prompts 🤔/🤔✏️ Prompt inputs/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) | To collect the number input.
    

    ---
    <br/>
   
