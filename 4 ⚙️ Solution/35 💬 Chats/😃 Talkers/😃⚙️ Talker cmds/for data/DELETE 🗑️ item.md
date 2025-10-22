<!-- TODO: detail the relation with database -->
<!-- TODO: add details to soft delete -->


# 😃🗑️ Talker `DELETE` command

> Part of [Talker 😃](<../../😃 Talker.md>)

> Relates to [Tables 🪣 folder](<../../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>

1. **What is a DELETE command?**

    A `DELETE` 🗑️
    * is a [Command ⌘](<../for control/⌘ Command.md>) 
    * that deletes an item from an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

    ---
    <br/>


1. **What's the syntax of a delete?**

    ```yaml
    # Single item
    - DELETE|<pool>|<key>:
        Pool: <pool>
        Key: <key>
    ```

    ```yaml
    # Multiple items in all-or-nothing transaction.
    - Delete:
        - Pool: <pool-1>
          Key: <key-1>
        - Pool: <pool-n>
          Key: <key-n>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<pool>` | Name of resource pool | `MyPool`
    | `<key>` | Key to delete from the pool | `MyKey` `$key`

    ---
    <br/>

1. **How to delete a complex key?**

    ```yaml
    # Single item with complex key
    - DELETE|<pool>:
        {key}
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `{key}` | Complex key to delete | `{a:1, b:2}`

    ---
    <br/>


1. **How up delete a mapped item?**

    ```yaml
    # Get the item from the database.
    - GET|myPool|myKey >> $item
    
    # Delete the item.
    - DELETE|$item 
    ```

    Commands: [`GET`](<GET ⏬ item.md>) [`DELETE`](<DELETE 🗑️ item.md>)

    ---
    <br/>


1. **What's the syntax for soft deletes?**

    <!-- TODO: add the property explanations -->

    ```yaml
    DELETE|<pool>|<key>:

        Soft: <n> <days|hours|minutes|months>

        OnSoft: <one-line-command>
            - <command-1>
            - <command-n>

        OnHard: <one-line-command>
            - <command-1>
            - <command-n>
    ````

    ---
    <br/>

1. **What's a use case for soft deletes?**

    See [Pop Token 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📃 Broker scripts/...supporters/🤵📃 Pop Token 🎫.md>).

    ---
    <br/>