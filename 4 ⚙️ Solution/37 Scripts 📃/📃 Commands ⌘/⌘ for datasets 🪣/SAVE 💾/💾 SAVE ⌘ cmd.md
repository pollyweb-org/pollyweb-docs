# 😃💾 Talker `SAVE` command

> About
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* Implemented by the [`.SAVE` 📃 script](<💾 SAVE 📃 script.md>)
* Relates to [Tables 🪣 folder](<../../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>)

## FAQ

1. **What is a SAVE command?**

    A `SAVE` 💾
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that stores an item in an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

    ---
    <br/>

1. **What's the syntax of an insert SAVE?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.
    
    ```yaml
    # Single item
    - SAVE <set> >> $inserted:
        :{object}:
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<set>` | Name of the [Dataset 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | `MySet`
    | `{object}` | [`CALL`](<../../⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) item to save in the pool | `MyKey` `$key`
    | `$inserted` | [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the insertion | `$item`

    ---
    <br/>

1. **How to insert an item?**

    ```yaml
    # With an object
    - SAVE mySet:
        A: 1
        B: 2

    # With a holder
    - SAVE mySet:
        $myItem


    # With a mix of both, 
    #   by adding surrounding ":" to placeholders
    - SAVE mySet:
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
    - SAVE $item

    # Comprehensive
    - SAVE $item: 
        :{changes}:
        STATE: <state>
    ```

    | Input| Purpose | Examples
    |-|-|-
    | `$item` | [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) loaded with [`READ`](<../READ 🧲/🧲 READ ⌘ cmd.md>)
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
    - SAVE $item:
        a: 1
    ```

    Uses:  [`SAVE`](<💾 SAVE ⌘ cmd.md>)

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
    - SAVE $item:
        a: 1
    ```

    Uses: [`SAVE`](<💾 SAVE ⌘ cmd.md>)
    
    ---
    <br/>


1. **How to save with reference data?**

    Here's a example [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>):
    * This matches the first item in `$list`
    *  where the value of `$list.B` 
    *  matches the value of `$item.B`
    *  setting `$item.A` with the value of `$list.A`

    ```yaml
    📃 Example:

    - SELECT >> $item.A:
        First: A
        From: $list
        Where: B.Is($item.B)
    
    - SAVE: $item
    ```
    Uses: [`SELECT`](<../../⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) [`.Is`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>)

    ---
    <br/>



1. **What are the possible errors?**

    | Status | Details
    |-|-
    | `BLOCKED` | On insert with [`SAVE`](<💾 SAVE ⌘ cmd.md>), the key is already used by an item with a different content. If the content is the same, then no error is raised.
    | `OUTDATED`  | On update, i.e. a [`SAVE`](<💾 SAVE ⌘ cmd.md>) after [`READ`](<../READ 🧲/🧲 READ ⌘ cmd.md>), the item was changed by a concurrent [`SAVE`](<💾 SAVE ⌘ cmd.md>).
    
    ---
    <br/>