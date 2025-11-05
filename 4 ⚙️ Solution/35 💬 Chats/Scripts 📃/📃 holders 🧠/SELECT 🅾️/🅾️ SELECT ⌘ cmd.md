# 😃🅾️ Talker `SQL` command

> Part of [Script 📃](<../../📃 basics/Script 📃.md>)

## FAQ 

1. **What is a SQL command?**

    A `SQL`
    * is a [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * that works with lists like SQL.

    ---
    <br/>

1. **What's the SQL syntax?**

    ```yaml
    SELECT >> $output:
        First|All|Distinct|Top(n): 
            A:a
            B:b
        From: $list
        Union: $list-1, $list-n
        Where: {filters}
        OrderBy: +a, -b
    ```

    |Input|Purpose|Example
    |-|-|-
    | `Distinct` | Groups results with [`.Distinct`](<../../📃 functions 🐍/🔩 {.Distinct}.md>)
    | `Union` | Merges lists with {{.Union}}
    | `Where` | Filters items with [`.Filter`](<../../📃 functions 🐍/🔩 {.Filter}.md>) 

    ---
    <br/>