# 😃💾 Talker `SAVE` command

> Part of [Script 📃](<../../📃 basics/Script 📃.md>)

> Implemented by the [`.SAVE` 📃 script](<💾 SAVE 📃 script.md>)

> Relates to [Tables 🪣 folder](<../../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>

1. **What is a SAVE command?**

    A `SAVE` 💾
    * is a [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * that stores an item in an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

    ---
    <br/>

1. **What's the syntax of an insert SAVE?**

    ```yaml
    # Single item
    - SAVE|<set> >> $inserted:
        {object}
        .Delete: <duration>        # Optional
        .OnBlocked: <holder>  # Optional
    ```

    ```yaml
    # Multiple items in all-or-nothing transaction.
    - SAVE:
        - <pool-1>: {object-1}
        - <pool-n>: {object-n}
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<set>` | Name of the [Dataset 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | `MySet`
    | `{object}` | Item to update or insert in the pool | `MyKey` `$key`
    | `.Delete` | Automatic cleanup with [`{.Add}`](<../../📃 functions 🐍/🔩 {.Add}.md>) | `30 days`
    | `.OnBlocked`| [`$Holder`](<../../📃 basics/Holder 🧠.md>) name to set `True` | `onBlocked`
    | `$inserted` | [Holder 🧠](<../../📃 basics/Holder 🧠.md>) with the insertion | `$item`

    ---
    <br/>

1. **How to insert an item?**

    ```yaml
    # With an object
    - SAVE|mySet:
        A: 1
        B: 2
        .Delete: 1 day
        .OnBlocked: onBlocked

    # With a holder
    - SAVE|mySet:
        $myItem


    # With a mix of both, 
    #   by adding surrounding ":" to placeholders
    - SAVE|mySet:
        A: 1
        B: 2
        :{$partA}:
        :{$partB}:
        .Delete: 1 day
        .OnBlocked: onBlocked
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
        .Delete: <period>
        .OnBlocked: <holder>
    ```

    | Input| Purpose | Examples
    |-|-|-
    | `$item` | [Holder 🧠](<../../📃 basics/Holder 🧠.md>) loaded with [`READ`](<../READ 🧲/🧲 READ ⌘ cmd.md>)
    | `{changes}` | Object with changes to apply | `{A:1, B:2}`

    ---
    <br/>

1. **How up update an item?**

    ```yaml
    # Get the item from the database
    - READ >> $item:
        Set: mySet
        Key: anExistingKey

    # Change a single property
    # Save or fail on concurrent saves
    - SAVE|$item:
        a: 1
    ```

    Commands:  [`SAVE`](<💾 SAVE ⌘ cmd.md>)

    ---
    <br/>

1. **What if the item doesn't exist?**

    Set the `Default` property of [`READ`](<../READ 🧲/🧲 READ ⌘ cmd.md>).

    ```yaml
    # Get the item from the database
    - READ >> $item:
        Set: mySet
        Key: aMissingKey # any missing key

        # Return {a:0, b:2} if missing
        Default: 
            a: 0
            b: 2

    # Save {a:1, b:2}
    - SAVE|$item:
        a: 1
    ```

    Commands: [`SAVE`](<💾 SAVE ⌘ cmd.md>)
    
    ---
    <br/>

1. **How do handled blocked tables?**

    Raises a 409 HTTP error in a [Script 📃](<../../📃 basics/Script 📃.md>) when trying to update an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) with the `NoUpdate` flag active - e.g. [`Grab@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Grab 👥🚀🖨️/🖨️ Grab 🚀 request.md>).

    ---
    <br/>

1. **How to save with reference data?**

    Here's a example [Script 📃](<../../📃 basics/Script 📃.md>):
    * This matches the first item in `$list`
    *  where the value of `$list.B` 
    *  matches the value of `$item.B`
    *  setting `$item.A` with the value of `$list.A`

    ```yaml
    📃 Example:

    - SQL >> $item.A:
        First: A
        From: $list
        Where: B.Is($item.B)
    
    - SAVE|$item
    ```
    Commands: 

    ---
    <br/>