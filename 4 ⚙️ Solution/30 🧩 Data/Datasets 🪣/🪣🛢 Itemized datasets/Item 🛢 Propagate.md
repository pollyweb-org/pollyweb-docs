# Item 🛢 Propagate

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ


1. **How to automatically propagate parents?**

    Add a `Propagate` list 
    * for parents to be automatically created 
    * on the [`SAVE` 💾 command](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
    * and on the [`Save@Itemizer` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Save 👥🚀🛢/🛢 Save 🚀 request.md>).

    ```yaml
    Table: <name>
    
    # Define the parent
    Parents:
        <parent>: {...}

    # Automatically create missing parents.
    Propagate:
       - <parent1>
       - <parent2>
    ```

    ---
    <br/>

