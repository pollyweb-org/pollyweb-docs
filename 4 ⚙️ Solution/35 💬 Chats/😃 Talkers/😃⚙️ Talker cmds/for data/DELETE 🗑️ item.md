<!-- TODO: detail the relation with database -->
<!-- TODO: add details to soft delete -->


# 😃🗑️ Talker `DELETE` command

> Part of [Talker 😃](<../../😃 Talker.md>)

> Relates to [Tables 🪣 folder](<../../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>

1. **What is a DELETE command?**

    A `DELETE` 🗑️
    * is a [Command ⌘](<../for control/⌘ Command.md>) 
    * that deletes an item from an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

    ---
    <br/>


1. **What's the syntax of a delete?**

    ```yaml
    # Inline
    - DELETE|<set>|<key>

    # Multiline
    - DELETE:
        Set: <set>
        Key: {key}
    ```


    | Argument| Purpose | Example
    |-|-|-
    | `<set>` | Name of the dataset | `MySet`
    | `<key>` | Key(s) to delete from the set | `A` `A,B` `$a` 
    | `{key}` | Key to delete from the set | `{A:1,B:2}`

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

    See a comprehensive example at [`UNDO`](<UNDO ↩️.md>).

    ```yaml
    DELETE|<set>|<key>:
        Undo: <n> <days|hours|minutes|months>
    ````



    ---
    <br/>

1. **What's a use case for soft deletes?**

    See [Pop Token 🔆](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📃 Broker scripts/...procedures/🤵📃 Pop Token 🎫.md>).

    ---
    <br/>