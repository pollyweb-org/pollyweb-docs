<!--
Example:
* [text](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)
-->


# 🪣 Talker `MAP` command

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a MAP item command?**

    A `MAP` 
    * is a [Command](<10 Command.md>) 
    * that retrieves an item by key from a resource pool
    * into a placeholder.

    ---
    <br/>


2. **What are use cases?**

    * [Vending machines 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)

    ---
    <br/>

3. **What's the syntax?**

    ```yaml
    - MAP|<pool>|<key> >> <item>
    ```

    | Argument| Purpose
    |-|-
    | `<pool>` | Name of resource pool.
    | `<key>`  | Key to look up in the pool.
    | `<item>` | Item to retrieve.

    ---
    <br/>

4. **What does it look in a chat?**


    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 🍫 Vending | 😃 What's the item number?   | 🔢 123
    | 🍫 Vending | 😃 A water bottle? [Yes, No]  
    ||

    ```yaml
    # 😃 Talker
    - INT|What's the item number? >> number
    - MAP|Items|{$number} >> item
    - CONFIRM|A {$item.Name}?     
    ```


    ```yaml
    # 🪣 Items
    | Number | Name          | Price  | 21+
    |--------|---------------|--------|----
    | 123    | water bottle  |  1.50  |
    | 124    | beer          |  4.50  | Yes
    ```
    

    ---
    <br/>
   