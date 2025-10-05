# 🪣 Talker `MAP` command

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a MAP item command?**

    A `MAP` 🪣
    * is a [Command ⌘](<10 ⌘ Command.md>) 
    * that retrieves an item by key 🔑
    * from a key-value resource pool 🪣
    * into a [Talker 😃](<01 😃 Talker.md>) placeholder.

    ---
    <br/>

1. **How to define a Resource Pool?**

    Resource Pools are defined in three ways in [Hoster ☁️ domains](<../35 ☁️ Hosters/05 ☁️🛠️ Hoster helper.md>).

    |Format| Details
    |-|-
    | `Markdown` | This is an upload `.md` file.
    | `YAML` | This is also an uploaded `.yaml` file.
    | `HTTP`| This is an endpoint defined in the settings.
    |

    Example of a Markdown resource pool called `Items.md`

    ```yaml
    # 🪣 Items
    | Code | Name          | Price  | 21+
    |------|---------------|--------|----
    | 123  | water bottle  |  1.50  |
    | ABC  | beer          |  4.50  | Yes
    ````

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

    Example of an HTTP endpoint.

    ```yaml
    Items:
        Endpoint: https://rest.any-domain.com/Items/{key}
    ```

    ---
    <br/>


2. **What are use cases?**

    * [Vending machines 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)

    ---
    <br/>

3. **What's the syntax?**

    ```yaml
    - MAP|<pool>|<key> >> $item
    ```

    | Argument| Purpose
    |-|-
    | `<pool>` | Name of resource pool.
    | `<key>`  | Key to look up in the pool.
    | `$item` | Item to retrieve.

    ---
    <br/>

4. **How to read a specific item property?**

    The syntax for properties is th following.

    ```yaml
    {$placeholder.property}
    ```

    Consider the resource pool `MyPool` 🪣 as the following.
   
    |Key|PropA|PropB
    |-|-|-
    |Key1|1.A|1.B 
    |Key2|2.A|2.B 
    
    The following [Talker 😃](<01 😃 Talker.md>) renders `ℹ️ 2.A` in the Chat.

    ```yaml
    # 😃 Talker 
    - MAP|MyPool|Key2 >> $myItem
    - INFO|{$myItem.PropA} 
    ```

    ---
    <br>

5. **What does it look in a Chat?**


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🍫 Vending | 😃 What's the item number?   | 🔢 123
    | 🍫 Vending | 😃 A water bottle? [Yes, No]  
    ||

    ```yaml
    # 😃 Talker
    - INT|What's the item number? >> $n
    - MAP|Items|{$n} >> $item
    - CONFIRM|A {$item.Name}?     
    ```
    
    | Number | Name          |
    |--------|---------------|
    | 123    | water bottle  |
    | 456    | beer          |
    
    

    ---
    <br/>
   