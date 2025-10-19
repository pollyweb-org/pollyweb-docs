# 🧬 Talker `MERGE` Command

> Part of [Talker 😃](<../../😃 Talker.md>)

> Used by [`Chats@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>)

<br/>

1. **What's the syntax of MERGE?**

    ```yaml
    # Comprehensive
    MERGE >> $out:
        Lists: # lists to merge 
            $1st
            $2nd
        Match: # matched properties 
            {object}
        Eval: # setter of properties
            {object}
        Output: # optional final layout
            {object} 
    ```

    | Param | Purpose | Example
    |-|-|-
    | `Lists` | The list to enrich with more data | `$1st`
    |  | Another list with additional data  | `$2nd`
    | `Match` | Match fields of `1st` and `2nd` lists | `{A:A, B:B}`
    | `Eval` | Set fields of `1st` with values of `2nd`  | `{X:X, Y:Y}`
    | `Output` | Optional output format after merged | `{Out: X}`
    | `$out` | [Placeholder 🧠](<$Placeholder 🧠.md>) with the merge or view | -

    ---
    <br/>

1. **What's an example of MERGE?**

    Consider the 1st list `$items`.

    ```yaml
    # Items
    | ID | Price | SupplierID |
    | -- | ----- | ---------- |
    |  1 |    10 |          A |
    |  2 |    20 |          X |
    |  3 |    30 |          X |
    ```


    And the 2nd list `$suppliers`.

    ```yaml
    # Suppliers
    | ID | Name |
    | -- | ---- |
    |  A |  ABC |
    |  X | XPTO |
    ```
    
    Let's merge them with [`MERGE`](<MERGE 🧬 lists.md>) and [`EVAL`](<EVAL ⬇️ flow.md>).

    ```yaml
    # Merge
    - MERGE >> $merged:
        Lists: 
            $items
            $suppliers
        Match: 
            SupplierID: ID
        Eval: 
            SupplierName: Name
        Output: 
            Item: ID
            Supplier: SupplierName
    ```
    
    Here's the final `$merged` list.

    ```yaml
    | Item | Supplier |
    | ---- | -------- |
    |    1 |      ABC |
    |    2 |     XPTO |
    |    3 |     XPTO |
    ```

    ---
    <br/>