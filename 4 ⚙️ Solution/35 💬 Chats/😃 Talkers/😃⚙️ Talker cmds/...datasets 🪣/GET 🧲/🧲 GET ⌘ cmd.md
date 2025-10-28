<!-- TODO: detail the relation with database -->

# 😃🧲 Talker `GET` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

> Relates to [Tables 🪣 folder](<../../../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>

1. **What's a GET item command?**

    A `GET` 🧲
    * is a [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) 
    * that retrieves an item by key 🔑
    * from a key-value resource pool 🪣
    * into a [Talker 😃](<../../../😃 Talker role.md>) holder.

    ---
    <br/>



1. **What's the read syntax?**

    ```yaml
    # Comprehensive
    - GET >> $item:
        Set: <set>
        Key: <key>

        # Required by default
        Default: {object}
        OnMissing: <command>
    ```

    ```yaml
    # Simplest
    - GET|<set>|<key> >> $item
    ```

    | Input| Purpose | Example
    |-|-|-
    | `Set` | Name of resource pool | `MyPool`
    | `Key`  | Key to look up in the pool | `MyKey` `$key`
    | `Default` | Objet to return if missing | `{A:1, B:2}`
    | `OnMissing` | [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) or [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) | `MyScript`
    | `$item` | Item to retrieve | -

    ---
    <br/>

1. **How to read a specific item property?**

    The syntax for properties is th following.

    ```yaml
    {$holder.property}
    ```

    Consider the resource pool `MyPool` 🪣 as the following.
   
    |Key|PropA|PropB
    |-|-|-
    |Key1|1.A|1.B 
    |Key2|2.A|2.B 
    
    The following [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) renders `ℹ️ 2.A` in the [Chat 💬](<../../../../💬 Chats/💬 Chat.md>).

    ```yaml
    📃 Script:
    - GET|MyPool|Key2 >> $myItem
    - INFO|{$myItem.PropA} 
    ```

    Commands: [`GET`](<🧲 GET ⌘ cmd.md>) [`INFO`](<../../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br>

1. **What does it look in a Chat?**

    Consider the resource pool `Items` 🪣 as the following.
    || Number | Name          |
    |-|--------|---------------|
    || 123    | water bottle  |
    || 456    | beer          |
    |

    Here's a [Chat 💬](<../../../../💬 Chats/💬 Chat.md>).

    || [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    |-| - | - | - |
    || 🍫 Vending | 😃 What's the item number?   | 🔢 123
    || 🍫 Vending | 😃 A water bottle? [Yes, No]  
    ||

    Here's the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>)

    ```yaml
    📃 Script:

    # Get the item code.
    - DIGITS|What's the item number? >> $n

    # Get the item.
    - GET >> $item:
        Set: Items
        Key: $n

    # Confirm the item name.
    - CONFIRM|A {$item.Name}?
    ```

    Commands: [`CONFIRM`](<../../../../🤔 Prompts/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`DIGITS`](<../../../../🤔 Prompts/🤔✏️ Prompt inputs/DIGITS 🔢/DIGITS 🔢 prompt.md>) [`GET`](<🧲 GET ⌘ cmd.md>)
    
   
    

    ---
    <br/>
   

1. **How to return a default value?**

    ```yaml
    # Get the item.
    - GET >> $item:
        Set: Items
        Key: 000

        # Return a dummy item if not found
        Default: 
            Number: 000    
            Name: Missing
    ```

    ---
    <br/>