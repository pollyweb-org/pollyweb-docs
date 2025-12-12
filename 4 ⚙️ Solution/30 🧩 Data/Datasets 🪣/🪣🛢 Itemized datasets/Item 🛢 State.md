# Item 🛢 .State

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

<br/>

## FAQ

1. **What's the .State field for?**

    The `.State` field
    * allows to track the state of an item in a workflow
    * and trigger actions on state changes
    * such as sending notifications, or triggering other processes.

    ---
    <br/>

1. **What architecture patterns does it allow?**

    |Pattern|Description|
    |-|-|
    | `Saga`   | Distributed asynchronous transactions coordination |


    ---
    <br/>

1. **How to work with .State changes?**

    `.State` changes
    * are set on the [`Build@Itemized` 🐌 msg](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢📨 Itemizer msgs/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
    * and processed by [Item 🛢 Handlers](<Item 🛢 Handlers.md>)
    * with the new state in the `New.State` property
    * and the old state in the `Old.State` property.


    ---
    <br/>

1. **How does it behave in idempotent scenarios?**

    `.State` is supposed to be changed.
    * Meaning that setting a `.State` in an item with the same state fails.
    * Meaning that duplicate events fail to be processed.
    * To mitigate error logs, stale `.State` changes raise a special `REPEATED` event.

    ---
    <br/>

1. **What if the code fails after the state change?**

    To ensure consistency,
    * state changes should be the last operation of an event handler,
    * leaving further operations to be processed on the following state handler.

    ---
    <br/>

1. **What's an alternative more compact syntax?**

    Here's an alternative syntax using `>>`.

    ```yaml
    Handlers:
        INSERTED >> OnInserted:
        UPDATED  >> OnUpdated:
            Assert: 
                New.AnyField: AnyNewValue
    ```

    ---
    <br/>

1. **How to define that state B only happens after A?**

    You can chain events using `>`.

    ```yaml
    Handlers:
        A > B >> OnB:
    ```

    This way, 
    * `OnB` will be called 
    * when an item state is first  `A` and then later `B`. 
    
    If `B` is set first, 
    * the handler will not be called
    * and the item is marked as having an invalid state.

    ---
    <br/>

1. **Where does the RETURN of a handler goes?**

    The [`RETURN`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) of [Item 🛢 Handlers](<Item 🛢 Handlers.md>)
    * automatically update the state of the item;
    * thus, the follow two blocks are equivalent.
  
    ```yaml
    📃 Exit transition with RETURN:

    - IF $Item.HasErrors:
        RETURN ERROR_STATE
    - ELSE:
        RETURN VALID_STATE
    ```

    Uses: [`IF`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RETURN`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)

    ```yaml
    📃 Exit transition with SAVE:

    # Exit with errors
    - IF $Item.HasErrors:
        - SAVE Table:
            .State: ERROR_STATE
        - RETURN

    # Exit successfully
    - SAVE $Item:
        .State: VALID_STATE
    ```

    Uses: [`IF`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`RETURN`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>)

    ---
    <br/>