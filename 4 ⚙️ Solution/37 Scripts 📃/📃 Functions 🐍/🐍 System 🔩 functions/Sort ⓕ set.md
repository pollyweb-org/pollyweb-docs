<!-- MERGE -->
# 🧠🔩 Set.Sort extension

> Part of [Set 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>)

> Used by [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)

## FAQ

1. **What's the Set.Sort syntax?**

    ```yaml
    $set.Sort: [order...]
    ```

    Inputs|Details | Example
    |-|-|-|
    |`$set`| [Set 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>) | `{A:1},{A:2}`
    |`order`| Order of [map](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) keys | `A,B+,C-` 
    

    ---
    <br/>


1. **What do symbols mean?**

   |Symbol|Meaning
   |-|-
   |`+`| Ascending order (default)
   |`-`| Descending order

   ---
   <br/>

   
1. **What are Set.Sort examples?**
  
    ```yaml
    # Original      # Sort A,B      # Sort B-,C+
    ┌───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
    │ A │ B │ C │   │ A │ B │ C │   │ A │ B │ C │
    ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
    │ 3 │ C │ 5 │   │ 1 │ A │ 6 │   │ 2 │ D │ 6 │
    │ 1 │ A │ 6 │   │ 2 │ A │ 7 │   │ 3 │ C │ 5 │
    │ 2 │ D │ 6 │   │ 2 │ D │ 6 │   │ 1 │ A │ 6 │
    │ 2 │ A │ 7 │   │ 3 │ C │ 5 │   │ 2 │ A │ 7 │
    └───┴───┴───┘   └───┴───┴───┘   └───┴───┴───┘
    ```
    
    ---
    <br/>