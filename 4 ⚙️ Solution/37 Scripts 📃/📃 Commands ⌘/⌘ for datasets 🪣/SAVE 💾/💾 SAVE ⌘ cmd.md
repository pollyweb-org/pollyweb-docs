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
        .Delete: <duration>   # Optional
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
    | `{object}` | [`CALL`](<../../⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) item to save in the pool | `MyKey` `$key`
    | `.Delete` | Automatic cleanup with [`{.Add}`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>) | `30 days`
    | `$inserted` | [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) with the insertion | `$item`

    ---
    <br/>

1. **How to insert an item?**

    ```yaml
    # With an object
    - SAVE mySet:
        A: 1
        B: 2
        .Delete: 1 day

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
        .Delete: 1 day
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
        .Delete: <period>
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

1. **How do handled blocked tables?**

    Raises a 409 HTTP error in a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) when trying to update an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) with the `NoUpdate` flag active - e.g. [`Grab@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️📨 Printer msgs/Grab 👥🚀🖨️/🖨️ Grab 🚀 call.md>).

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
    
    - SAVE $item
    ```
    Uses: [`SELECT`](<../../⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) [`.Is`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>)

    ---
    <br/>

1. **How to use functions on .Delete?**

    Consider the following [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) excerpt from [`Issue@Broker` 🐌 msg](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>).
    
    ```yaml
    SAVE $item:
        .Delete: 
            .Lower:
                $expiration,
                Now.Add(30 days)
    ```

    Uses: [`.Lower`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Lower ⓕ.md>) [`.Now`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>) [`.Add`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>) 

    ---
    <br/>