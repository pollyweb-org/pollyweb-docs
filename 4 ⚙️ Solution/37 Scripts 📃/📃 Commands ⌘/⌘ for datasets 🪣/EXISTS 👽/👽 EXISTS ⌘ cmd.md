# 😃👽 Talker `EXISTS` command

> Implementation
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ

1. **What's a EXISTS item command?**

    A `EXISTS` 🧲
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that says if a item exists by key 🔑
    * from an [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

    ---
    <br/>



1. **What's the EXISTS syntax?**

    ```yaml
    # Comprehensive
    - EXISTS >> $item:
        Set: <set>
        Key: <key>

        # Apply conditions when reading
        Assert: [assertions...]
    ```

    ```yaml
    # Simplest
    - EXISTS|<set>|<key> >> $item
    ```

    | Input| Purpose | Example
    |-|-|-
    | `Set` | Name of resource pool | `MyPool`
    | `Key`  | Key to look up in the pool | `1` `$h` `{A:1,B:2}`
    | `Assert` | [`.Assert`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Assert ⓕ.md>) filters | `Type:Admin`
    | `$item` | Item to retrieve | -

    ---
    <br/>

