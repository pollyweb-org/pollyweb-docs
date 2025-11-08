<!-- TODO -->

# 🧠 List holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ


1. **What are the built-in functions for list holders?**

    Group | [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | Purpose 
    |-|-|-
    |Size   | [`.IsEmpty`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsEmpty}.md>)  | Is empty?
    |       | [`.IsOne`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsOne}.md>)    | Has only one item?
    |       | [`.AreMany`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.AreMany}.md>)  | Has more than one item?
    |       | [`.Length`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Length}.md>)   | What's the length?
    |       | [`.Size`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Size}.md>)     | What's the length?
    |Query| [`.Contains`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Contains}.md>) | Contains a given item?
    |       | [`.First`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.First}.md>)    | What's the first item?
    |       | [`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>)     | What's the last item
    |       | [`.Equals`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Equals}.md>)   | Has these items in this order?
    |       | [`.Differs`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Differs}.md>)  | Does not equal this other list?
    |       | [`.Is`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Is}.md>)       | Has these items in any order?
    |       | [`.IsNot`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsNot}.md>)    | Are any of these items missing?
    |Change | [`.Distinct`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Distinct}.md>) | What are the unique items?
    |       | [`.Filter`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Filter}.md>)   | What items meet given filters?
    |       | [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Append}.md>)     | What if we add items?
    |       | [`.Add`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>) | Same as [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Append}.md>)
    |       | [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>)   | What if we remove items?
    |       | [`.Minus`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Minus}.md>) | Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>)
    |       | [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>) | Same as [`.Remove`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>)
    | Format | [`.Format`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Format}.md>) | Formats the items in ths list
    |       | [`.List`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.List}.md>) | Extracts a single item property 
    
    ---
    <br/>



1. **What are the commands for list holders?**

    |[Command ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 🚦 [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) | Asserts the items in a list
    | 🧮 [`EVAL`](<../../📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) | Formats a list into another
    | 🌪️ [`DISTINCT`](<../../📃 Commands ⌘/⌘ for holders 🧠/DISTINCT 🌪️/🌪️ DISTINCT ⌘ cmd.md>) | Returns the unique items 
    | 🔽 [`FILTER`](<../../📃 Commands ⌘/⌘ for holders 🧠/FILTER 🔽/🔽 FILTER ⌘ cmd.md>) | Filters items with [{Functions} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
    | 4️⃣ [`FOR`](<../../📃 Commands ⌘/⌘ for control ▶️/FOR 4️⃣/4️⃣ FOR ⌘ cmd.md>) | Loops items in sequence
    | *️⃣ [`PARALLEL`](<../../📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) | Loops items in parallel
    | 🅾️ [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) | Filters items with SQL queries

    ---
    <br/>
    
1. **How to assert a list of objects?**

    Let's assert this list.
    ```yaml
    ┌────┬────┬───┐        
    │ A  │ B  │ C │        
    ├────┼────┼───┤        
    │ 10 │ 11 │ X │        
    │ 20 │ 21 │ Y │        
    └────┴────┴───┘        
    ```

    Here's the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    - ASSERT|$list:
        - AllOf: A, B
        - A.IsBetween(10,19)
        - B.IsBetween(20,29)
        - C.IsIn(X,Y)
    ```
    Uses: [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`.IsBetween`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsBetween}.md>) [`.IsIn`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsIn}.md>)

    ---
    <br/>




1. **How to append into lists?**

    Using the [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Append}.md>) or [`.Add` functions](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>).
    
    ```yaml   
    ┌────────────────────────┬──────────────┐
    │ Explicit               │ Implicit     │ 
    ├────────────────────────┼──────────────┤
    │ EVAL|$lst.Add >> $lst: │ EVAL +> $lst │ 
    │   A: 1                 │   A: 1       │
    │   B: 2                 │   B: 2       │
    └────────────────────────┴──────────────┘    
    ```

    To append a value in a [List 🧠](<List holders.md>) with [`EVAL`](<../../📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>), use  `+>` instead of `>>`.
    ```yaml
    📃 Example:
    - EVAL|A +> $list
    - EVAL|B +> $list
    # Results in [A,B]    
    ```

    Here's a alternative syntax using the [`.Add` function](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>) in a [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).

    ```yaml
    📃 Example:
    - EVAL|A >> $list
    - EVAL|$list.Add(A) >> $list
    # Results in [A,B]    
    ```
    
    ---
    <br/>

1. **How to merge two lists?**

    Using the [`.Append`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Append}.md>) or [`.Add` functions](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>).

    ```yaml   
    ┌────────────────────┬───────────────┐
    │ Explicit           │ Implicit      │ 
    ├────────────────────┼───────────────┤
    │ EVAL|.Add >> $out: │ EVAL >> $out: │ 
    │   - $lst1          │   $lst1       │
    │   - $lst2          │   $lst2       │
    └────────────────────┴───────────────┘    
    ```

    | List1 | List2 | Result
    |-|-|-
    | `A,B` | `B,C` | `A,B,B,C`
    | `{A:1}` | `{B:2},{C:3}`| `{A:1},{B:2},{C:3}`

    ---
    <br/>


1. **How to filter a list?**

    Using the [`.Filter` function](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Filter}.md>) or the [`FILTER` command](<../../📃 Commands ⌘/⌘ for holders 🧠/FILTER 🔽/🔽 FILTER ⌘ cmd.md>).

    ```yaml   
    ┌───────────────────────────┬──────────────────────┐
    │ Explicit                  │ Implicit             │ 
    ├───────────────────────────┼──────────────────────┤
    │ EVAL|$lst.Filter >> $out: │ FILTER|$lst >> $out: │ 
    │   - A.IsBelow(3)          │   - A.IsBelow(3)     │
    │   - B.IsNotEmpty          │   - B.IsNotEmpty     │
    │   - C: 123                │   - C: 123           │
    └───────────────────────────┴──────────────────────┘    
    ```

    | List1 | List2 | Result
    |-|-|-
    | `A,B` | `B,C` | `A,B,B,C`
    | `{A:1}` | `{B:2},{C:3}`| `{A:1},{B:2},{C:3}`

    ---
    <br/>


1. **How to format a list of objects?**

    Using the [`.Format` function](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Format}.md>) to extract specific properties.

    ```yaml
    ┌───────────────────────────┬────────────────────┐
    │ Explicit                  │ Implicit           │ 
    ├───────────────────────────┼────────────────────┤
    │ EVAL|$lst.Format >> $out: │ EVAL|$lst >> $out: │ 
    │   Alpha: A                │   Alpha: A         │      
    │   Beta: B                 │   Beta: B          │  
    └───────────────────────────┴────────────────────┘    
    ```

    ---
    <br/>


1. **How to take some properties from a [List 🧠](<List holders.md>) of [Pair 🧠](<Pair holders.md>)?**
  
    Using the [`.List` function](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.List}.md>) in one of 3 forms:
    * with the [`EVAL` command](<../../📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>),
    * or as `$holder.property` for a single property,
    * or as `$holder(prop-1, prop-N)` for a multiple properties.
    
    Here's a [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to take 1 property.

    ```yaml   
    ┌─────────────────────────┬───────────────┐
    │ Explicit                │ Implicit      │ 
    ├─────────────────────────┼───────────────┤
    │ EVAL|$lst.List >> $out: │ EVAL >> $out: │ 
    │    A                    │   $lst.A      │
    └─────────────────────────┴───────────────┘    
    ```

    Here's a [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to take 2 properties.

    ```yaml   
    ┌─────────────────────────┬───────────────┐
    │ Explicit                │ Implicit      │ 
    ├─────────────────────────┼───────────────┤
    │ EVAL|$lst.List >> $out: │ EVAL >> $out: │ 
    │    - A                  │   $lst(A,B)   │      
    │    - B                  │               │      
    └─────────────────────────┴───────────────┘    
    ```

    ---
    <br/>



1. **How to select distinct a unique set of items?**

    Using the [`.Distinct` function](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Distinct}.md>)  or the [`DISTINCT` command](<../../📃 Commands ⌘/⌘ for holders 🧠/DISTINCT 🌪️/🌪️ DISTINCT ⌘ cmd.md>).

    ```yaml
    ┌─────────────────────────┬───────────────────┐
    │ Explicit                │ Implicit          │ 
    ├─────────────────────────┼───────────────────┤
    │ EVAL|.Distinct >> $out: │ DISTINCT >> $out: │ 
    │   $lst1.Add($lst2)      │   $lst1           │
    |                         │   $lst2           │     
    └─────────────────────────┴───────────────────┘    
    ```

    ---
    <br/>
