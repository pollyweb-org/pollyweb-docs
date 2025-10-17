# 🗑️ Talker `DELETE` command

> Part of [Talker 😃](<../😃 Talker.md>)

> Relates to [Tables 🪣 folder](<../../../55 👷 Build domains/📦 Hosteds/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>


1. **What's the syntax of a delete?**

    ```yaml
    # Single item
    - DELETE|<pool>|<key>
    ```

    ```yaml
    # Multiple items
    - Delete:
        - <pool-1>: <key-1>
        - <pool-n>: <key-n>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<pool>` | Name of resource pool | `MyPool`
    | `{object}` | Item to update or insert in the pool | `MyKey` `$key`

    ---
    <br/>


1. **How up delete a mapped item?**

    ```yaml
    # Get the item from the database.
    - MAP|myPool|myKey >> $item
    
    # Delete the item.
    - DELETE|$item 
    ```

    ---
    <br/>


1. **What's the syntax for soft deletes?**

    ```yaml
    DELETE|<pool>|<key>:

        Soft: <n> <days|hours|minutes|months>

        OnSoft: 
            - <command-1>
            - <command-n>

        OnHard:
            - <command-1>
            - <command-n>
    ````

    ---
    <br/>

1. **What's a use case for soft deletes?**

    See [Pop Token 🔆](<Pop Token 🔆.md>).

    ---
    <br/>