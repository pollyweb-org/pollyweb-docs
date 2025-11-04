# ⬇️ FILTER ⌘ cmd

> Part of [Script 📃](<../../📃 basics/Script 📃.md>)

## FAQ 

1. **What is a FILTER command?**

    A `FILTER`
    * is a [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * that filters a list with the [`.Filter`](<../../📃 functions 🐍/🔩 {.Filter}.md>) function.

    ---
    <br/>

1. **What's the FILTER syntax?**

    ```yaml
    # As a YAML object
    FILTER|$list1 >> $list2:
        <property-n>: <value-n>
        :<boolean-n>:
    ```

    ```yaml
    # As a YAML list
    FILTER|$list1 >> $list2:
        - <property-n>: <value-n>
        - <boolean-n>
    ```

    ---
    <br/>