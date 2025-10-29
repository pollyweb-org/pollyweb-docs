<!-- TODO: detail -->

# 😃*️⃣ Talker `PARALLEL` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

> Example: [Pop Vault 🔆](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Chats 💬 Pop 🧑‍🦰🐌🤵/Pop Vault/🤵 Pop Vault 📃 handler.md>)


<br/>




1. **What is a PARALLEL command?**

    A `PARALLEL` *️⃣
    * is a flow [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>)  
    * that runs a list of [Commands ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) 
    * for each item in a given list.
  
    ---
    <br/>

1. **What is the difference to a standard FOR cycle?**

    * `FOR` cycles iterate in sequence, allowing for ordered logic.
    * [`PARALLEL`](<*️⃣ PARALLEL ⌘ cmd.md>) commands iterate concurrently in a random order.
    ---
    <br/>

1. **What is the syntax of the PARALLEL command?**

    ```yaml
    PARALLEL|$list|$item:
        # List of commands
        - <command-1>|$item
        - <command-n>|$item
    ```

    | Input | Purpose | Example
    |-|-|-
    | `$input-list` | List to iterate | `[1,2,3]`
    | `$input-item` | Item of an iteration | `1`
    | `<command-n>`   | [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) to execute | [`SAVE`](<../../...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)

    ---
    <br/>


1. **How to use the PARALLEL command?**

    Here's a [Chat 💬](<../../../../Chats 💬/💬 Chat.md>)

    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Item `2` in random order
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Item `1` in random order
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Item `3` in random order
    

    <br/>

    Here's the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>)

    ```yaml
    - PARALLEL|[1,2,3]|$n:
        - INFO|Item `{$n}` in random order
    ```

    ---
    <br/>

