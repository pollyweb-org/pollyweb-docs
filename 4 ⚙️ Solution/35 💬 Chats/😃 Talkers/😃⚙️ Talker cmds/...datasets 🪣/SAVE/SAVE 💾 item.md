<!-- TODO: detail the relation with database -->

# 😃💾 Talker `SAVE` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

> Implemented by the [`.SAVE` 📃 script](<.📎 Assets/SAVE 📃 script.md>)

> Relates to [Tables 🪣 folder](<../../../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>

1. **What is a SAVE command?**

    A `SAVE` 💾
    * is a [Command ⌘](<../../...commands ⌘/⌘ Command.md>) 
    * that stores an item in an [Itemized 🛢 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

    ---
    <br/>

1. **What's the syntax of an insert SAVE?**

    ```yaml
    # Single item
    - SAVE|<set> >> $inserted:
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
    | `<set>` | Name of resource pool | `MyPool`
    | `{object}` | Item to update or insert in the pool | `MyKey` `$key`
    | `$inserted` | [Placeholder 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) with the insertion | `$item`

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
    # Simplest
    SAVE|$item

    # Comprehensive
    SAVE|$item: 
        {changes}
        .Timeout: {period}
    ```

    | Argument| Purpose | Examples
    |-|-|-
    | `$item` | [Placeholder 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) loaded with [`GET`](<../GET/GET ⏬ item.md>)
    | `{changes}` | Object with changes to apply | `{A:1, B:2}`
    | `.Timeout` | Automatic delete for cleanup, in | `30 days`
    | | `minutes` `hours` `days` `months`

    ---
    <br/>

1. **How up update an item?**

    ```yaml
    # Get the item from the database
    - GET >> $item:
        Set: myPool
        Key: anExistingKey

    # Change a single property
    # Save or fail on concurrent saves
    - SAVE|$item:
        a: 1
    ```

    Commands: [`EVAL`](<../GET/GET ⏬ item.md>) [`SAVE`](<SAVE 💾 item.md>)

    ---
    <br/>

1. **What if the item doesn't exist?**

    Set the `Default` property of [`GET`](<../GET/GET ⏬ item.md>).

    ```yaml
    # Get the item from the database
    - GET >> $item:
        Set: myPool
        Key: aMissingKey # any missing key

        # Return {a:0, b:2} if missing
        Default: 
            a: 0
            b: 2

    # Save {a:1, b:2}
    - SAVE|$item:
        a: 1
    ```

    Commands: [`EVAL`](<../GET/GET ⏬ item.md>) [`SAVE`](<SAVE 💾 item.md>)
    
    ---
    <br/>

1. **How do handled blocked tables?**

    Raises a 409 HTTP error in a [Talker 😃](<../../../😃 Talker role.md>) when trying to update an [Itemized 🛢 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) with the `NoUpdate` flag active - e.g. [`Grab@Printer`](<../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/👥🚀🖨️ Grab.md>).

    ---
    <br/>