# 😃🧬 Talker `MERGE` Command

> Part of [Talker 😃](<../../😃 Talker.md>)

> Used by [`Chats@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>)

<br/>


1. **What is a MERGE command?**

    A `MERGE` 🧬
    * is a [Command ⌘](<../for control/⌘ Command.md>) 
    * that merges too lists or an object with a list
    * by matching a list of properties.

    ---
    <br/>

1. **What's the syntax of MERGE?**

    ```yaml
    MERGE >> $out:

        Lists: # lists to merge 
            <1st-alias>: $1st
            <2nd-alias>: $2nd
    
        Match: # matched properties 
            {object}
    
        Output: # final layout
            {object} 
    ```

    | Param | Purpose | Example
    |-|-|-
    | `Lists` | The list to enrich with more data | `$1st`
    |  | Another list with additional data  | `$2nd`
    | `Match` | Match fields of `1st` and `2nd` lists | `{1st.A:2nd.A}`
    | `Output` | Output item template after merged | `{Out: 2nd.Y}`
    | `$out` | [Placeholder 🧠](<$Placeholder 🧠.md>) with the merge or view | -

    ---
    <br/>

1. **What's an example of MERGE?**

    Consider the 1st list `$items`.

    ```yaml
    # Items
    | ID | PRICE | SUP_ID |
    | -- | ----- | ------ |
    |  1 |    10 |      A |
    |  2 |    20 |      X |
    |  3 |    30 |      X |
    ```


    And the 2nd list `$suppliers`.

    ```yaml
    # Suppliers
    | ID | NAME |
    | -- | ---- |
    |  A |  ABC |
    |  X | XPTO |
    ```
    
    Let's merge them with [`MERGE`](<MERGE 🧬 lists.md>) and [`EVAL`](<EVAL ⬇️ flow.md>).

    ```yaml
    # Merge
    - MERGE >> $merged:
        Lists: 
            ITEMS: $items
            SUPPLIERS: $suppliers
        Match: 
            ITEMS.SUP_ID: SUPPLIERS.ID
        Output: 
            ITEM: ITEMS.ID
            SUPPLIER: SUPPLIERS.NAME
    ```
    
    Here's the final `$merged` list.

    ```yaml
    | ITEM | SUPPLIER |
    | ---- | -------- |
    |    1 |      ABC |
    |    2 |     XPTO |
    |    3 |     XPTO |
    ```

    ---
    <br/>

1. **How to only add properties?**

    Add one of the lists with surrounding `:` characters.

    ```yaml
    - MERGE >> $merged:
        Lists: 
            ITEMS: $items
            SUPPLIERS: $suppliers
        Match: 
            ITEMS.SUP_ID: SUPPLIERS.ID
        Output: 
            SUPPLIER: SUPPLIERS.NAME
            # also include all ITEM properties.
            :ITEM:
    ```

    ---
    <br/>