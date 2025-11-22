# Item 🛢 .State

> Part of [Itemized 🪣 dataset](<../🪣🔣 Dataset types/Itemized 🛢 dataset.md>)

## FAQ


1. **How to work with .State changes?**

    `.State` changes
    * are set on the [`Build@Itemized` 🅰️ method](<../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Table Build 👥🐌🛢/🛢 Build 🐌 msg.md>)
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