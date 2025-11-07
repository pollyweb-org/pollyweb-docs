<!-- TODO -->

# 😃🅾️ Talker `SQL` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ 

1. **What is a SQL command?**

    A `SQL`
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that works with lists like SQL.

    ---
    <br/>

1. **What's the SQL syntax?**

    ```yaml
    SELECT >> $output:
        All|First|Last|Distinct: [fields]
        From: $list-1, $list-n
        Where: {filters}
        OrderBy: +a, -b
        Limit: 123
    ```

    |Input|Purpose||
    |-|-|-
    | `All` | Default
    | `First` | Uses [`.First`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.First}.md>) to return only the 1st item
    | `Last` | Uses [`.Last`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>) to return only the last item
    | `Distinct` | Uses [`.Distinct`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Distinct}.md>) to group results 
    | `From` | Uses [`.Append`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Append}.md>) to merge multiple lists
    | `Where` | Uses [`.Filter`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Filter}.md>) to filter list items 
    | `OrderBy`| Uses...
    | `Limit` | Uses...

    ---
    <br/>


1. **How to filter lists with SQL?**


    Consider the following lists of `$items` and `$suppliers`.

    ```yaml
    # Items                      # Suppliers
    ┌────┬───────┬───────┐       ┌────┬──────┬──────┐
    │ ID │ Price │ SupID │       │ ID │ Name │ City │
    ├────┼───────┼───────┤       ├────┼──────┼──────┤
    │  1 │   10  │   A   │       │  A │ ABC  │ C1   │
    │  2 │   20  │   X   │       │  X │ XPTO │ C2   │
    │  3 │   30  │   X   │       │  Y │ ANY  │ C3   │
    └────┴───────┴───────┘       └────┴──────┴──────┘
    ```


    ```yaml
    📃 Example:
    - SELECT >> $filtered:
        All: ID, Name
        From: $suppliers
        Where: ID.IsIn(X, Y)
    ```    
    Here's the final `$filtered` list.

    ```yaml
    # Suppliers
    ┌────┬──────┐
    │ ID │ Name │
    ├────┼──────┤
    │ X  │ XPTO │
    │ Y  │ ANY  │
    └────┴──────┘
    ```


    ---
    <br/>



1. **How to update lists with SELECT?**

    Here's an example using the same lists as before.
   
    ```yaml
    📃 Example:
    
    # Create a simple list with all item IDs
    - EVAL|$items >> $out:
        Item: ID

    # For each item, add Supplier and City
    - SELECT|$out: 
        First:
            Supplier: Name
            City: City
        From: $suppliers
        Where: ID.Is(SupID)
    ```
    Commands: [`EVAL`](<../EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>)
    
    Here's the final `$out` list.

    ```yaml
    ┌──────┬──────────┬──────┐
    │ Item │ Supplier │ City │
    ├──────┼──────────┼──────┤
    │  1   │   ABC    │ C1   │
    │  2   │   XPTO   │ C2   │
    │  3   │   XPTO   │ C2   │
    └──────┴──────────┴──────┘
    ```

    ---
    <br/>
    
