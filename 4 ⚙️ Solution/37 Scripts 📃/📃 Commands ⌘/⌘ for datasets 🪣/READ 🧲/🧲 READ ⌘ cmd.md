<!-- TODO: detail the relation with database -->

# 😃🧲 Talker `READ` command

> Implementation
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* Implemented by the [`READ` 📃 script](<🧲 READ 📃 script.md>)

## FAQ

1. **What's a READ item command?**

    A `READ` 🧲
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that retrieves an item by key 🔑
    * from a key-value resource pool 🪣
    * into a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).

    ---
    <br/>



1. **What's the read syntax?**

    ```yaml
    # Comprehensive
    - READ >> $item:
        Set: <set>
        Key: <key>
        Get: <property1>, <property2>, ...

        # Required by default
        Default: {object}
        OnMissing: <command>
    ```

    ```yaml
    # Simplest
    - READ|<set>|<key> >> $item
    ```

    | Input| Purpose | Example
    |-|-|-
    | `Set` | Name of resource pool | `MyPool`
    | `Key`  | Key to look up in the pool | `1` `$h` `{A:1,B:2}`
    | `Get`  | [List 🧠](<../../../📃 Holders 🧠/🧠🔩 List holders/List holders.md>) of fields to retrieve | `A,B` `{Alias:A}`
    |        | Makes the `$item` readonly
    | `Default` | [Maps 🧠](<../../../📃 Holders 🧠/🧠 Input holders/Map holders.md>) to return if missing | `{C:3}` 
    || Always returns the key | `{A:1,B:2,C:3}`
    | `OnMissing` | [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) or [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | `MyScript`
    | `$item` | Item to retrieve | -

    ---
    <br/>

1. **Why does the item become readonly when using `Get`?**

    When using the `Get` input, 
    * only a subset of the item fields are retrieved,
    * causing the resulting item to be incomplete;
    * thus, it's made readonly to prevent accidental updates.
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
    
    The following [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) renders `ℹ️ 2.A` in the [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

    ```yaml
    📃 Script:
    - READ|MyPool|Key2 >> $myItem
    - INFO|{$myItem.PropA} 
    ```

    Uses: [`READ`](<🧲 READ ⌘ cmd.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br>

1. **What does it look in a Chat?**

    Consider the resource pool `Items` 🪣 as the following.
    || Number | Name          |
    |-|--------|---------------|
    || 123    | water bottle  |
    || 456    | beer          |
    |

    Here's a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>).

    || [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    |-| - | - | - |
    || 🍫 Vending | 😃 What's the item number?   | 🔢 123
    || 🍫 Vending | 😃 A water bottle? [Yes, No]  
    ||

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

    ```yaml
    📃 Script:

    # Get the item code.
    - DIGITS|What's the item number? >> $n

    # Get the item.
    - READ >> $item:
        Set: Items
        Key: $n

    # Confirm the item name.
    - CONFIRM|A {$item.Name}?
    ```

    Uses: [`CONFIRM`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`DIGITS`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/DIGITS 🔢/DIGITS 🔢 prompt.md>) [`READ`](<🧲 READ ⌘ cmd.md>)
    
   
    

    ---
    <br/>
   

1. **How to return a default value?**

    > Used by the [`Saved@Broker` 📃 handler](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Saved 🧑‍🦰🐌🤵/🤵 Saved 📃 handler.md>)

    ```yaml
    # Get the item.
    - READ >> $item:
        Set: Items
        Key: 000

        # Return a dummy item if not found
        Default: 
            Number: 000    
            Name: Missing
    ```

    ---
    <br/>

1. **How to find a child by key?**

    > Used by the [`Pop Vault` 📃 handler](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/Pop Bind 🔗/📃 Remove Bind/🤵 Remove Bind 📃 script.md>)


    ```yaml
    # Get the child 
    - READ >> $child:
        Set: $parent.Children
        Key: <child-key>
    ```


    `Advantage` This method ensures that the underlying relationship between the parent and the child is preserved. 
    * For example, it's not possible to get an `OrderLine` by `LineUUID` from the `Orders` table if given `OrderLine` is not linked to the `Order`.

    ---
    <br/>