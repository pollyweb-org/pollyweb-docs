# 🪣 Talker `MAP` command

> Part of [Talker 😃](<../😃 Talker.md>)

> Relates to [Tables 🪣 folder](<../../../55 👷 Build domains/📦 Hosteds/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>


1. **What's a MAP item command?**

    A `MAP` 🪣
    * is a [Command ⌘](<../😃⚙️ Talker cmds/⌘ Command.md>) 
    * that retrieves an item by key 🔑
    * from a key-value resource pool 🪣
    * into a [Talker 😃](<../😃 Talker.md>) placeholder.

    ---
    <br/>



1. **What's the read syntax?**

    ```yaml
    # Comprehensive
    - MAP >> $item:
        Pool: <pool>
        Key: <key>
    ```

    ```yaml
    # Simplest
    - MAP|<pool>|<key> >> $item
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `Pool` | Name of resource pool | `MyPool`
    | `Key`  | Key to look up in the pool | `MyKey` `$key`
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
    
    The following [Talker 😃](<../😃 Talker.md>) renders `ℹ️ 2.A` in the Chat.

    ```yaml
    # 😃 Talker 
    - MAP|MyPool|Key2 >> $myItem
    - INFO|{$myItem.PropA} 
    ```

    ---
    <br>

1. **What does it look in a [Chat 💬](<../../💬 Chats/💬 Chat.md>)?**


    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 🍫 Vending | 😃 What's the item number?   | 🔢 123
    | 🍫 Vending | 😃 A water bottle? [Yes, No]  
    ||

    ```yaml
    # 😃 Talker
    - DIGITS|What's the item number? >> $n
    - MAP|Items|$n >> $item
    - CONFIRM|A {$item.Name}?     
    ```
    
    | Number | Name          |
    |--------|---------------|
    | 123    | water bottle  |
    | 456    | beer          |
    
    

    ---
    <br/>
   
