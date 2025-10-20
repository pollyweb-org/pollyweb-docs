<!-- TODO: detail the relation with database -->

# 😃⏬ Talker `GET` command

> Part of [Talker 😃](<../../😃 Talker.md>)

> Relates to [Tables 🪣 folder](<../../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>

1. **What's a GET item command?**

    A `GET` ⏬
    * is a [Command ⌘](<../for control/⌘ Command.md>) 
    * that retrieves an item by key 🔑
    * from a key-value resource pool 🪣
    * into a [Talker 😃](<../../😃 Talker.md>) placeholder.

    ---
    <br/>



1. **What's the read syntax?**

    ```yaml
    # Comprehensive
    - GET >> $item:
        Pool: <pool>
        Key: <key>
        # Required by default
        OnMissing: <command>
    ```

    ```yaml
    # Simplest
    - GET|<pool>|<key> >> $item
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `Pool` | Name of resource pool | `MyPool`
    | `Key`  | Key to look up in the pool | `MyKey` `$key`
    | `OnMissing` | [Command ⌘](<../for control/⌘ Command.md>) or [Script 📃](<../for control/📃 Script.md>) | `Handler`
    | `$item` | Item to retrieve

    ---
    <br/>

1. **How to read a specific item property?**

    The syntax for properties is th following.

    ```yaml
    {$placeholder.property}
    ```

    Consider the resource pool `MyPool` 🪣 as the following.
   
    |Key|PropA|PropB
    |-|-|-
    |Key1|1.A|1.B 
    |Key2|2.A|2.B 
    
    The following [Talker 😃](<../../😃 Talker.md>) renders `ℹ️ 2.A` in the Chat.

    ```yaml
    # 😃 Talker 
    - GET|MyPool|Key2 >> $myItem
    - INFO|{$myItem.PropA} 
    ```

    Commands: [`GET`](<GET ⏬ item.md>) [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️ prompt.md>)

    ---
    <br>

1. **What does it look in a [Chat 💬](<../../../💬 Chats/💬 Chat.md>)?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🍫 Vending | 😃 What's the item number?   | 🔢 123
    | 🍫 Vending | 😃 A water bottle? [Yes, No]  
    ||

    ```yaml
    # 😃 Talker
    - DIGITS|What's the item number? >> $n
    - GET|Items|$n >> $item
    - CONFIRM|A {$item.Name}?     
    ```

    Commands: [`CONFIRM`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) [`DIGITS`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/44 🔢 DIGITS prompt.md>) [`GET`](<GET ⏬ item.md>)
    
    | Number | Name          |
    |--------|---------------|
    | 123    | water bottle  |
    | 456    | beer          |
    
    

    ---
    <br/>
   
