# Item 🛢 Cascade

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)


## FAQ


1. **How to automatically cascade deletes?**

    Add a `Cascade` list 
    * for children to be automatically deleted 
    * on the [`DELETE` 🗑️ command](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) 
    * and on the [`Delete@Itemizer` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>).

    ```yaml
    Table: <name>
    
    # Define the chidren
    Children:
        <child>: {...}

    # Automatically delete children.
    Cascade:
        - <child1>
        - <child2>
    ```

    ---
    <br/>

