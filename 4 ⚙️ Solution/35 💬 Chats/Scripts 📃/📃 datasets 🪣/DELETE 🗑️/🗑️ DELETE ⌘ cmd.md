<!-- TODO: detail the relation with database -->
<!-- TODO: add details to soft delete -->


# 😃🗑️ Talker `DELETE` command

> Part of [Talker 😃](<../../../Talkers 😃/😃 Talker role.md>)

> Relates to [Tables 🪣 folder](<../../../../55 👷 Build domains/Hosteds 📦/📦📄 Hosted files/🪣📂 Tables folder.md>)

<br/>

1. **What is a DELETE command?**

    A `DELETE` 🗑️
    * is a [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * that deletes an item from an [Itemized 🛢 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

    ---
    <br/>


1. **What's the syntax of a delete?**

    ```yaml
    # After a GET
    - DELETE|$item
    ```

    | Input| Purpose 
    |-|-
    | `$item` | Previous return from [`GET`](<../GET 🧲/🧲 GET ⌘ cmd.md>) 

    <br/>

    ```yaml
    # Inline
    - DELETE|<set>|<key>

    # Comprehensive
    - DELETE:
        Set: <set>
        Key: {key}
        Undo: <undo> <days|hours|minutes|months>
    ```


    | Input| Purpose | Example
    |-|-|-
    | `Set` | Name of the dataset | `MySet`
    | `Key` | Key(s) to delete from the set |-
    ||  `<key>` as a string or array | `A` `A,B` `$a` 
    || `{key}` as an object map | `{A:1,B:2}`
    | `Undo` | Hide to allow an [`UNDO`](<../UNDO ↩️/↩️ UNDO ⌘ cmd.md>) later | `30 days`
    | | `days` `hours` `minutes` `months`
    
    ---
    <br/>

1. **How up delete a mapped item?**

    ```yaml
    # Get the item from the database.
    - GET|myPool|myKey >> $item
    
    # Delete the item.
    - DELETE|$item 
    ```

    Commands: [`GET`](<../GET 🧲/🧲 GET ⌘ cmd.md>) [`DELETE`](<🗑️ DELETE ⌘ cmd.md>)

    ---
    <br/>

