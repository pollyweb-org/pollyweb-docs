<!--
Example:
* [text](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)
-->


# 🪣 Talker `MAP` command

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's a MAP item command?**

    ---
    <br/>

2. **What's the syntax?**

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

3. **What does it look in a chat?**


    ```yaml
    💬|[Buy] an item:

    # Ask for the item number
    - INT|What's the item number? >> number

    # Map item number to name.
    - MAP|Items|{$number} >> item
    - CONFIRM|A {$item.Name}?     

    # Ask proof of over 21 if needed.
    - IF|{$item.21+}:
        Then: SHARE|nlweb.org/IDENTITY/OVER-21

    # Charge the item price.
    - CHARGE|{$item.Price}     

    # Deliver the item.
    - TEMP|Delivering...    
    - RELAY|Machines|{$$locator.key}
        Command: Open({$item.Number})
        OnFailure: failure
        OnSignal: success

    # Show success.
    success:
    - SUCCESS|Thanks! Pick up your item.
    - GOODBYE

    # Show error.
    fail:
    - FAILURE|It didn't work, sorry!
    - REFUND|{$item.Price}
    ```

    ---
    <br/>
   
4. **What are example use cases?**

    * [Vending machines 🏪](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/20 🏪 Vending/01 🏪 Index.md>)

    ---
    <br/>