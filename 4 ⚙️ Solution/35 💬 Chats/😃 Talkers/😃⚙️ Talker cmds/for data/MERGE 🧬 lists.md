# 🧬 Talker `MERGE` Command

> Part of [Talker 😃](<../../😃 Talker.md>)

> Used by [`Chats@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>)

<br/>

1. **What's the syntax of MERGE?**

    ```yaml
    # Comprehensive
    MERGE >> $out:

        # lists to merge
        List: $listA
        With: $listB

        # matched properties 
        When: 
            {object}

        # setter of properties
        Then: 
            {object}

        # optional final layout
        View: 
            {object}
    ```

    | Param | Purpose | Example
    |-|-|-
    | `List` | The list to enrich with more data | `$1st`
    | `With` | Another list with additional data  | `$2nd`
    | `When` | Match fields of `1st` and `2nd` lists | `{A:A, B:B}`
    | `Then` | Set fields of `1st` with values of `2nd`  | `{X:X, Y:Y}`
    | `View` | Optional output format after merged | `{Out: X}`
    | `$out` | [Placeholder 🧠](<../../😃 Talkers/😃⚙️ Talker cmds/for data/$Placeholder 🧠.md>) with the merge or view | -

    ```yaml
    # Simple
    MERGE|<$listA>|<$listB> >> $out:
        When: KeyA = KeyB
        Then: PropA = PropB
    ```

    | Param | Purpose | Example
    |-|-|-
    | `When` | Match fields of `1st` and `2nd` lists | `A=B, C=D`
    | `Then` | Set fields of `1st` with values of `2nd`  | `X=X, Y=Y`

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
        List: $items
        With: $suppliers
        When: SupplierID = ID
        Then: SupplierName = Name
        View: 
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