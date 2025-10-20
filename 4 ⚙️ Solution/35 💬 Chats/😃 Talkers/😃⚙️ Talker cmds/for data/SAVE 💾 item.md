<!-- TODO: detail the relation with database -->

# 😃💾 Talker `SAVE` command

> Part of [Talker 😃](<../../😃 Talker.md>)

> Relates to [Tables 🪣 folder](<../../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>

1. **What is a SAVE command?**

    A `SAVE` 💾
    * is a [Command ⌘](<../for control/⌘ Command.md>) 
    * that stores an item in an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>).

    ---
    <br/>

1. **What's the syntax of an insert SAVE?**

    ```yaml
    # Single item
    - SAVE|<pool> >> $inserted:
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
    | `$inserted` | [Placeholder 🧠](<$Placeholder 🧠.md>) with the insertion | `$item`

    ---
    <br/>

1. **How to insert an item?**

    ```yaml
    # With an object
    - SAVE|myPool:
        A: 1
        B: 2

    # With a placeholder
    - SAVE|myPool:
        {$myItem}

    # With a mix of both, 
    #   by adding surrounding ":" to placeholders
    - SAVE|myPool:
        A: 1
        B: 2
        :{$partA}:
        :{$partB}:
    ```

    ---
    <br/>

1. **What's the syntax of an update SAVE?**

    ```yaml
    SAVE|$item
    ```

    | Argument| Purpose 
    |-|-
    | `$item` | [Placeholder 🧠](<$Placeholder 🧠.md>) item loaded with [`GET` ⏬](<GET ⏬ item.md>)

    ---
    <br/>

1. **How up update an item?**

    ```yaml
    # Get the item from the database.
    - GET >> $item:
        Pool: myPool
        Key: myKey

    # Change a single property.
    - EVAL|$item:
        a: 1
    
    # Save or fail on concurrent saves.
    - SAVE|$item 
    ```

    ---
    <br/>

1. **How do handled blocked tables?**

    Raises a 409 HTTP error in a [Talker 😃](<../../😃 Talker.md>) when trying to update an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢.md>) with the `NoUpdate` flag active - e.g. [`Grab@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/👥🚀🖨️ Grab.md>).

    ---
    <br/>