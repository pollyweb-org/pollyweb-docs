# 🪣 Talker `MAP` command

> Part of [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>)

<br/>


1. **What's a MAP item command?**

    A `MAP` 🪣
    * is a [Command ⌘](<../40 🌊 Talker flows/10 ⌘ Command.md>) 
    * that retrieves an item by key 🔑
    * from a key-value resource pool 🪣
    * into a [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>) placeholder.

    ---
    <br/>

1. **How to define a Resource Pool?**

    Resource Pools are defined in four ways in the [🪣 Pools file](<../91 🧑‍💻 Hosteds/17 🪣📄 Pools file.md>) of [Hoster ☁️ domains](<../../4 ⚙️ Solution/45 🛠️ Helper domains/55 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>).

    |Format| Details
    |-|-
    | `Markdown` | This is an upload `.md` file.
    | `YAML` | This is also an uploaded `.yaml` file.
    | `HTTP`| This is an endpoint defined in the settings.
    | `Folder` | This is a folder with `.pdf` and `.png` files
    |

    <br/>

    Example of a Markdown resource pool called `Items.md`

    ```yaml
    # 🪣 Items
    | Code | Name          | Price  | 21+
    |------|---------------|--------|----
    | 123  | water bottle  |  1.50  |
    | ABC  | beer          |  4.50  | Yes
    ```

    <br/>

    Example of a YAML resource pool called `Items.yaml`

    ```yaml
    # 🪣 Items
    - 123: 
        Code: 123
        Name: water bottle
        Price: 1.50
    - ABC:
        Code: ABC
        Name: beer
        Price: 4.50
        21+: Yes
    ```

    <br/>

    Example of an HTTP endpoint.

    ```yaml
    Items:
        Endpoint: https://rest.any-domain.com/Items/{key}
    ```

    ---
    <br/>


1. **What are use cases?**

    * [Vending machines 🏪](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    - MAP|<pool>|<key> >> $item
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<pool>` | Name of resource pool | `MyPool`
    | `<key>`  | Key to look up in the pool | `MyKey` `$key`
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
    
    The following [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>) renders `ℹ️ 2.A` in the Chat.

    ```yaml
    # 😃 Talker 
    - MAP|MyPool|Key2 >> $myItem
    - INFO|{$myItem.PropA} 
    ```

    ---
    <br>

1. **What does it look in a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)?**


    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | [Prompt](<../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)
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
   