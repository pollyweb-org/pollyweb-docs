# Item 🛢 Propagate

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ


1. **How to automatically propagate parents?**

    For parents to be automatically created, add a `Propagate`.

    ```yaml
    Table: <name>
    
    # Define the parent
    Parents:
        <parent>: {...}

    # Automatically create missing parents.
    Propagate:
        <parent1>, <parent2>
    ```

    ---
    <br/>

