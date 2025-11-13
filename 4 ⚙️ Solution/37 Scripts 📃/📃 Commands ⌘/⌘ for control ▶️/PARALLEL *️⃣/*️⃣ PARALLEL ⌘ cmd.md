<!-- TODO: detail -->

# 😃*️⃣ Talker `PARALLEL` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

> Example: [Pop Vault 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/Pop Bind 🔗/📃 Remove Bind/🤵 Remove Bind 📃 script.md>)


<br/>




1. **What is a PARALLEL command?**

    A `PARALLEL` *️⃣
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  
    * that runs a list of [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * for each item in a given list.
  
    ---
    <br/>

1. **What is the difference to a standard FOR cycle?**

    * [`FOR`](<../FOR 4️⃣/4️⃣ FOR ⌘ cmd.md>) cycles iterate in sequence, allowing for ordered logic.
    * [`PARALLEL`](<*️⃣ PARALLEL ⌘ cmd.md>) commands iterate concurrently in a random order.
    ---
    <br/>

1. **What is the PARALLEL syntax for list items?**

    ```yaml
    PARALLEL:
        # List of commands
        - <command-1>
        - <command-n>
    ```

    | Input | Purpose | Example
    |-|-|-
    | `<command>`   | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) to execute in parallel | [`SAVE`](<../../⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)

    ---
    <br/>


1. **What is the syntax of the PARALLEL for blocks?**

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
    | `<command-n>`   | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) to execute | [`SAVE`](<../../⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)

    ---
    <br/>


1. **How to use the PARALLEL command?**

    Here's a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Item `2` in random order
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Item `1` in random order
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Item `3` in random order
    

    <br/>

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

    ```yaml
    - PARALLEL|[1,2,3]|$n:
        - INFO|Item `{$n}` in random order
    ```

    ---
    <br/>

