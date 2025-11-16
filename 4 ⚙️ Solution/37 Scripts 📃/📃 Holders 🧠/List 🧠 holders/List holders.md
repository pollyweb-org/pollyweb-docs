# 🧠 List holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ


1. **What are List holders?**

    List holders store items in a sequence - e.g. `[1, A, {X:9}]`

    ---
    <br/>

1. **How are the called across the main programming languages?**
   
    |Synonym |Languages
    |-|-
    | `Array` | C, C++, JSON, Java, JavaScript, PHP, Python, Ruby, Swift, YAML
    | `Collection` | VB.NET
    | `List` | C#, Dart, Haskell, Kotlin, Lisp, ML, NoSQL, R, Scala
    | `Sequence` | F#, OCaml
    | `Slice` | Go
    | `Tuple` | Python
    | `Vector` | MATLAB, Perl
    
    ---
    <br/>

1. **What are the built-in functions for list holders?**

    Group | [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) |Type| Purpose 
    |-|-|-|-
    |Query  | [`.Contains`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Contains}.md>) |bool| Contains a given item?
    |       | [`.Equals`](<../Any 🧠 holders/Equals ⓕ any.md>)   |bool| Has these items in this order?
    |       | [`.Differs`](<../Any 🧠 holders/Differs ⓕ any.md>)  |bool| Does not equal this other list?
    |       | [`.Is`](<../Any 🧠 holders/Is ⓕ any.md>)       |bool| Has these items in any order?
    |       | [`.IsNot`](<../Any 🧠 holders/IsNot ⓕ any.md>)    |bool| Are any of these items missing?
    |Size   | [`.IsEmpty`](<../Any 🧠 holders/IsEmpty ⓕ any.md>)  | bool| Is empty?
    |       | [`.IsOne`](<IsOne ⓕ list.md>)    | bool| Has only one item?
    |       | [`.AreMany`](<AreMany ⓕ list.md>)  | bool| Has more than one item?
    |       | [`.Size`][.Size]     | [num][num]| Returns the number of items
    |       | [`.Length`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Length}.md>)   |  [num][num]| Equals [`.Size`][.Size]
    |Read   | [`.First`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.First}.md>)   |[list][list], any| Get the first `n` items
    |       | [`.Last`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Last}.md>)   |[list][list], any| Get the last `n` items
    |       | [`.Distinct`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Distinct}.md>) |[list][list]| Return only unique items
    |Change | [`.Append`][.Append]     |[list][list]| Add items to the list
    |       | [`.Add`](<../Any 🧠 holders/Add ⓕ any.md>) |[list][list]| Same as [`.Append`][.Append]
    |       | [`.Remove`][.Remove]   |[list][list]| Remove items from the list
    |       | [`.Minus`](<../Any 🧠 holders/Minus ⓕ any.md>) |[list][list]| Same as [`.Remove`][.Remove]
    |       | [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>) |[list][list]| Same as [`.Remove`][.Remove]
    
    
    ---
    <br/>



1. **What are the commands for list holders?**

    |[Command ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 🚦 [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) | Asserts the items in a list
    | 🌪️ [`DISTINCT`](<../../📃 Commands ⌘/⌘ for holders 🧠/DISTINCT 🌪️/🌪️ DISTINCT ⌘ cmd.md>) | Returns the unique items 
    | 🔽 [`FILTER`](<../../📃 Commands ⌘/⌘ for holders 🧠/FILTER 🔽/🔽 FILTER ⌘ cmd.md>) | Filters items with [{Functions} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
    | 4️⃣ [`FOR`](<../../📃 Commands ⌘/⌘ for control ▶️/FOR 4️⃣/4️⃣ FOR ⌘ cmd.md>) | Loops items in sequence
    | *️⃣ [`PARALLEL`](<../../📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) | Loops items in parallel
    | ⬇️ [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) | Formats a list into another
    | 🅾️ [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) | Filters items with SQL queries
    | ↘️ [`SET`](<../../📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>) | Changes a list

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
    Uses: [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CALL`](<../../📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`.IsBetween`](<../Any 🧠 holders/IsBetween ⓕ any.md>) [`.IsIn`](<../Any 🧠 holders/IsIn ⓕ any.md>)

    ---
    <br/>




1. **How to append into lists?**

    Using the [`.Append`][.Append] or [`.Add` functions](<../Any 🧠 holders/Add ⓕ any.md>) with [`CALL`](<../../📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>).
    
    ```yaml   
    ┌────────────────────────┬─────────────┐
    │ Explicit               │ Implicit    │ 
    ├────────────────────────┼─────────────┤
    │ CALL|$lst.Add >> $lst: │ PUT +> $lst │ 
    │   A: 1                 │   A: 1      │
    │   B: 2                 │   B: 2      │
    └────────────────────────┴─────────────┘    
    ```

    Or use  `+>` instead of `>>` to append to a [List 🧠][list] with [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>).
    
    ```yaml
    📃 Example:
    - PUT|A +> $list
    - PUT|B +> $list
    # Results in [A,B]    
    ```

    Here's a alternative syntax using the [`.Add` function](<../Any 🧠 holders/Add ⓕ any.md>) in a [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).

    ```yaml
    📃 Example:
    - PUT|A >> $list
    - PUT|$list.Add(A) >> $list
    # Results in [A,B]    
    ```
    
    ---
    <br/>

1. **How to merge two lists?**

    Using the [`.Append`][.Append] or [`.Add` functions](<../Any 🧠 holders/Add ⓕ any.md>) with the [`.Evaluate`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Evaluate}.md>) syntax.

    ```yaml   
    ┌────────────────────┬──────────────┐
    │ Explicit           │ Implicit     │ 
    ├────────────────────┼──────────────┤
    │ CALL|.Add >> $out: │ PUT >> $out: │ 
    │   - $lst1          │   $lst1      │
    │   - $lst2          │   $lst2      │
    └────────────────────┴──────────────┘    
    ```

    | List1 | List2 | Result
    |-|-|-
    | `A,B` | `B,C` | `A,B,B,C`
    | `{A:1}` | `{B:2},{C:3}`| `{A:1},{B:2},{C:3}`

    ---
    <br/>


1. **How to filter a list?**

    Using the [`.Filter` function](<../Set 🧠 holders/Filter ⓕ set.md>) or the [`FILTER` command](<../../📃 Commands ⌘/⌘ for holders 🧠/FILTER 🔽/🔽 FILTER ⌘ cmd.md>).

    ```yaml   
    ┌───────────────────────────┬──────────────────────┐
    │ Explicit                  │ Implicit             │ 
    ├───────────────────────────┼──────────────────────┤
    │ CALL|$lst.Filter >> $out: │ FILTER|$lst >> $out: │ 
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

    Using the [`.Format` function](<../Set 🧠 holders/Format ⓕ set.md>) or the [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) command.

    ```yaml
    ┌───────────────────────────┬───────────────────┐
    │ Explicit                  │ Implicit          │ 
    ├───────────────────────────┼───────────────────┤
    │ CALL|$lst.Format >> $out: │ PUT|$lst >> $out: │ 
    │   Alpha: A                │   Alpha: A        │      
    │   Beta: B                 │   Beta: B         │  
    └───────────────────────────┴───────────────────┘    
    ```

    ---
    <br/>


1. **How to take some properties from a [List 🧠][list] of [Map 🧠](<../Map 🧠 holders/Map holders.md>)?**
  
    Using the [`.Format` function](<../Set 🧠 holders/Format ⓕ set.md>) in one of 3 forms:
    * with the [`CALL` commands](<../../📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>),
    * or as `$holder.property` for a single property on [`PUT`](<../../📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>),
    * or as `$holder(prop-1, prop-N)` for a multiple properties.
    
    Here's a [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to take 1 property.

    ```yaml   
    ┌───────────────────────────┬──────────────┐
    │ Explicit                  │ Implicit     │ 
    ├───────────────────────────┼──────────────┤
    │ CALL|$lst.Format >> $out: │ PUT >> $out: │ 
    │    A                      │   $lst.A     │
    └───────────────────────────┴──────────────┘    
    ```

    Here's a [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to take 2 properties.

    ```yaml   
    ┌───────────────────────────┬──────────────┐
    │ Explicit                  │ Implicit     │ 
    ├───────────────────────────┼──────────────┤
    │ CALL|$lst.Format >> $out: │ PUT >> $out: │ 
    │    - A                    │   $lst(A,B)  │      
    │    - B                    │              │      
    └───────────────────────────┴──────────────┘    
    ```

    ---
    <br/>



1. **How to select distinct a unique set of items?**

    Using the [`.Distinct` function](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Distinct}.md>)  or the [`DISTINCT` command](<../../📃 Commands ⌘/⌘ for holders 🧠/DISTINCT 🌪️/🌪️ DISTINCT ⌘ cmd.md>).

    ```yaml
    ┌─────────────────────────┬───────────────────┐
    │ Explicit                │ Implicit          │ 
    ├─────────────────────────┼───────────────────┤
    │ CALL|.Distinct >> $out: │ DISTINCT >> $out: │ 
    │   $lst1.Add($lst2)      │   $lst1           │
    |                         │   $lst2           │     
    └─────────────────────────┴───────────────────┘    
    ```

    ---
    <br/>


[list]: <List holders.md>
[.Size]: <../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Size}.md>
[num]: <Num holders.md>
[.Append]: <../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Append}.md>
[.Remove]: <../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Remove}.md>