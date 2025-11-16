# 😃🅾️ Talker `SELECT` command

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ 

1. **What is a SELECT command?**

    A `SELECT`
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that handles [List 🧠 holders](<../../../📃 Holders 🧠/🧠 Input holders/List holders.md>) 
    * using a SQL (Structured Query Language) syntax.

    ---
    <br/>

1. **What's the SELECT syntax?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Evaluate}.md>) syntax.

    ```yaml
    SELECT:
        All|First|Last|Distinct: [fields]
        From: $list-1, $list-n
        Where: {filters}
        OrderBy: +a, -b
        Limit: 10
    ```

    |Input|Purpose||
    |-|-|-
    | `All` | Uses [`.Format`](<../../../📃 Holders 🧠/🧠🔩 Set holders/Set.Format 🔩 ext.md>) to format item properties
    | `First` | Uses [`.First`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.First}.md>) and [`.Format`](<../../../📃 Holders 🧠/🧠🔩 Set holders/Set.Format 🔩 ext.md>) on the 1st item
    | `Last` | Uses [`.Last`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>) and [`.Format`](<../../../📃 Holders 🧠/🧠🔩 Set holders/Set.Format 🔩 ext.md>) on the last item
    | `Distinct` | Uses [`.Distinct`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Distinct}.md>) to group results 
    | `From` | Uses [`.Cross`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Cross}.md>) to join [List 🧠 holders](<../../../📃 Holders 🧠/🧠 Input holders/List holders.md>)
    | `Where` | Uses [`.Filter`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Filter}.md>) to filter [List 🧠](<../../../📃 Holders 🧠/🧠 Input holders/List holders.md>) items 
    | `OrderBy`| Uses [`.Sort`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Sort}.md>) to order the [List 🧠](<../../../📃 Holders 🧠/🧠 Input holders/List holders.md>) items
    | `Limit` | Uses [`.First`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.First}.md>) to limit the items returned

    ---
    <br/>

1. **What's the difference between creating and changing?**
    
    | Behavior | Syntax | 
    |-|-
    | Create a new [List 🧠](<../../../📃 Holders 🧠/🧠 Input holders/List holders.md>) | `SELECT >> $lst`
    | Change a [List 🧠](<../../../📃 Holders 🧠/🧠 Input holders/List holders.md>) | `SELECT\|$lst:`
    | - equivalent to           | `SELECT\|$lst >> $lst:`
    

    ---
    <br/>

1. **How to filter lists with SELECT?**


    Consider the following lists of `$items` and `$suppliers`.

    ```yaml
    # $items                     # $suppliers
    ┌────┬───────┬───────┐       ┌────┬──────┬──────┐
    │ ID │ Price │ SupID │       │ ID │ Name │ City │
    ├────┼───────┼───────┤       ├────┼──────┼──────┤
    │  1 │    10 │ A     │       │ A  │ ABC  │ C1   │
    │  2 │    20 │ X     │       │ X  │ XPTO │ C2   │
    │  3 │    30 │ X     │       │ Y  │ ANY  │ C3   │
    └────┴───────┴───────┘       └────┴──────┴──────┘
    ```

    ```yaml
    # Filter items:            # ┌────┬───────┐
    - SELECT >> $out:          # │ ID │ SupID │
        All: ID, SupID         # ├────┼───────┤
        From: $items           # │  3 │ X     │
        Where: ID.IsIn(1,3)    # │  1 │ A     │
        OrderBy: ID-           # └────┴───────┘
    ```    

    ```yaml
    # Items with suppliers:    # ┌────┬───────┬──────┐
    SELECT >> $out:            # │ ID │ Price │ Sup  │
      All:                     # ├────┼───────┼──────┤
        ID: "P{i.ID}"          # | P1 |    15 | ABC  |
        Price: Price.Add(50%)  # | P2 |    30 | XPTO |
        Sup: Name              # | P3 |    45 | XPTO |
      From:                    # └────┴───────┴──────┘ 
        i: $items
        s: $suppliers        
      Where: s.ID.Is(SupID)    
    ```    

    ---
    <br/>
