
<!-- TODO: detail -->

# 😃4️⃣ Talker `FOR` command

> Part of [Script 📃](<../../📃 basics/Script 📃.md>)

> Example: [Pop Vault 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Pop 🧑‍🦰🐌🤵/Pop Vault/🤵 Pop Vault 📃 handler.md>)


<br/>




1. **What is a FOR command?**

    A `FOR` *️⃣
    * is a flow [Command ⌘](<../../📃 basics/Command ⌘.md>)  
    * that runs a list of [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * in an orderly sequence
    * for each item in a given list.
  
    ---
    <br/>


1. **What is the syntax of the FOR command?**

    ```yaml
    FOR|$list|$item:
        # List of commands
        - <command-1>|$item
        - <command-n>|$item
        - BREAK
    ```

    | Input | Purpose | Example
    |-|-|-
    | `$list` | List to iterate | `[1,2,3]`
    | `$item` | Item of an iteration | `1`
    | `<command>`   | [Command ⌘](<../../📃 basics/Command ⌘.md>) to execute | [`SAVE`](<../../📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
    | `BREAK`| Special command to stop

    ---
    <br/>


1. **How to use the FOR command?**

    Here's a [Chat 💬](<../../../Chats 💬/💬 Chat.md>)

    | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt 🤔](<../../../Prompts 🤔/🤔 Prompt.md>) | [Wallet 🧑‍🦰 apps](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [Host 🤗 domains](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Item `1` in sequence
    | [Host 🤗 domains](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Item `2` in sequence
    | [Host 🤗 domains](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Item `3` in sequence
    

    <br/>

    Here's the [Script 📃](<../../📃 basics/Script 📃.md>)

    ```yaml
    📃 Example:
    - FOR|[1,2,3]|$n:
        - INFO|Item `{$n}` in random order
    ```

    ---
    <br/>
