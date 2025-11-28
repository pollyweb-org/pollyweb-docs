# Item 🛢 Propagate

> About
* Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)
* Used by the [`Broker.Binds` 🪣 table](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>) 
    * to insert into the [`Broker.Domains` 🪣 table](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🪣 Broker tables/Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>)

<br/>

## FAQ

1. **How does Propagate relate to Event Sourcing Projections?**

    `Propagate`
    * is a simplified way to automatically create parent items
    * on the [`SAVE` 💾 command](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 
    * and on the [`Save@Itemizer` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Save 👥🚀🛢/🛢 Save 🚀 call.md>).
    * without having to write full Event Sourcing Projections.
  
    ---
    <br/>

1. **How to automatically propagate parents?**

    Add a `Propagate` list referencing the [Item 🛢 Parents](<Item 🛢 Parents.md>).
    
    ```yaml
    Table: <name>
    
    # Define the parent
    Parents:
        <parent1>: {...}
        <parent2>: {...}

    # Automatically create missing parents.
    Propagate: <parent1>, <parent2>
    ```

    ---
    <br/>

