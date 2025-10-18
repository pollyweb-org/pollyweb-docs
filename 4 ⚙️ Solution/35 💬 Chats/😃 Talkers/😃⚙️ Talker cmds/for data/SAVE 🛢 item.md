<!-- TODO: detail the relation with database -->

# 🛢 Talker `SAVE` command

> Part of [Talker 😃](<../../😃 Talker.md>)

> Relates to [Tables 🪣 folder](<../../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>


1. **What's the syntax of a SAVE?**

    ```yaml
    # Single item
    - SAVE|<pool>:
        {object}
    ```

    ```yaml
    # Multiple items in all-or-nothing transaction.
    - SAVE:
        - <pool-1>: {object-1}
        - <pool-n>: {object-n}
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<pool>` | Name of resource pool | `MyPool`
    | `{object}` | Item to update or insert in the pool | `MyKey` `$key`

    ---
    <br/>


1. **How up update an item?**

    ```yaml
    # Get the item from the database.
    - GET|myPool|myKey >> $item

    # Change a single property.
    - EVAL|$item:
        a: 1
    
    # Save or fail on concurrent saves.
    - SAVE|$item 
    ```

    ---
    <br/>