# Item 🛢 Assert

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

<br/>

## FAQ

1. **What is the Assert for?**

    `Assert` verifies the state of an item, 
    * marking it as invalid
    * and blocking [Item 🛢 State](<Item 🛢 State.md>) transitions.
  
    ---
    <br/>

1. **Why not raise an Error instead?**

    Because `Assert` allows to 
    * keep the item data for inspection
    * and to later recover it by fixing or adjusting the `Assert`.

    ---
    <br/>

1. **Why not blocking it from being read?**

    Because reading is required for inspection.

    ---
    <br/>

1. **How to define assertions?**

    Use the syntax from the [`ASSERT` 🚦](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) command.

    ```yaml
    # Example
    Assert:
        AllOf: <field1>, <field2>
        UUIDs: <field1>
        Texts: <field2>, <field3>
        <field1>.<assertion1>: {...}
        <field2>.<assertion2>: {...}
    ```

    ---
    <br/>