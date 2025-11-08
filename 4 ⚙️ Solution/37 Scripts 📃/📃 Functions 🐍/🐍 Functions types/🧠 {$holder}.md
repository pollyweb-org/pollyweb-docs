<!-- TODO: -->

# 🐍 {$holder} function

> Part of [{Functions} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

<br/>

1. **What's syntax for input placeholders?**

    
    Consider the following [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    
    ```yaml
    # 😃 Talker 
    PUT >> $p
        $: my default
        A: another property

    INFO|{$p}   # Prints "my default"
    INFO|{$p.$} # Prints "my default"
    INFO|{$p.A} # Prints "another property"
    ```

    | [Command ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 🧮 [`EVAL`](<../../📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) | To push an object into a [holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).
    | ℹ️ [`INFO`](<../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) | To show the holder values.
    
    ---
    <br/>



1. **What's an example for input placeholders?**
   
    | [Domain](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Give me a quantity  | ↕️ 1234
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ I'm saving `1,234`
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Although you typed `1234`
    |

    <br/>
    
    Here's the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
        
    ```yaml
    # 😃 Talker 
    💬 Example:
    - QUANTITY|Give me a quantity >> $n
    - INFO|I'm saving `{$n}`
    - INFO|Although you typed `{$n.Text}`
    ```

    | [Command ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) | To show the [holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) values.
    | ↕️ [`QUANTITY`](<../../📃 Prompts 🤔/🤔 Input ✏️ prompts/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) | To collect the number input.
    

    ---
    <br/>
   
