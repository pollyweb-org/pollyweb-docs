<!-- TODO -->

# 🧠 List holders

> Part of [Holders 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)

## FAQ

1. **What are the commands for list holders?**

    |[Command ⌘](<../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | Purpose
    |-|-
    | 🚦 [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) | Asserts the items in a list
    | ⬇️ [`EVAL`](<../../📃 Commands ⌘/⌘ for holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) | Formats a list into another
    | 🌪️ [`DISTINCT`](<../../📃 Commands ⌘/⌘ for holders 🧠/DISTINCT 🌪️/🌪️ DISTINCT ⌘ cmd.md>) | Returns the unique items 
    | 🔽 [`FILTER`](<../../📃 Commands ⌘/⌘ for holders 🧠/FILTER 🔽/🔽 FILTER ⌘ cmd.md>) | Filters items with [{Functions} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
    | 4️⃣ [`FOR`](<../../📃 Commands ⌘/⌘ for control ▶️/FOR 4️⃣/4️⃣ FOR ⌘ cmd.md>) | Loops items in sequence
    | *️⃣ [`PARALLEL`](<../../📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) | Loops items in parallel
    | 🅾️ [`SELECT`](<../../📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>) | Filters items with SQL queries

    ---
    <br/>

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
    |       | [`.Add`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>)      | What if we add items?
    |       | [`.Minus`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Minus}.md>)    | What if we remove items?
    |       | [`.Diff`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>) | Same as [`.Minus`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Minus}.md>)
    
    ---
    <br/>


1. **How to assert a list of objects?**

    Here's a [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # Create a list
    EVAL >> $list:
        - {A:10, B:20, C:X}
        - {A:11, B:21, C:Y}

    # Verify the list items.
    ASSERT|$list:
        - AllOf: A, B
        - A.IsBetween(10,19)
        - B.IsBetween(20,29)
        - C.IsIn(X,Y)
    ```
    Uses: [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../📃 Commands ⌘/⌘ for holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`.IsBetween`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsBetween}.md>) [`.IsIn`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsIn}.md>)

    ---
    <br/>



1. **How to format a list of objects?**

    Here's the syntax.

    ```yaml
    # Syntax - fails if $list was never set
    EVAL|$list >> $output:
        {object}
    ```

    ||Inputs| Purpose
    |-|-|-
    || `$list` | [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) list of objects
    ||| Fails if `$list` was never set
    |

    Here's a list.

    ```yaml
    ┌────┬────┬────┐
    │ A  │ B  │ C  │
    ├────┼────┼────┤
    │ 10 │ 11 │ 12 │
    │ 20 │ 21 │ 22 │
    └────┴────┴────┘
    ```

    Here's the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # Extract only A and B properties.
    - EVAL|$list >> $output:
        Alpha: A
        Beta: B
    ```

    Here's the `$output`.

    ```yaml
    ┌───────┬──────┐
    │ Alpha │ Beta │
    ├───────┼──────┤
    │   10  │  11  │
    │   20  │  21  │
    └───────┴──────┘
    ```

    ---
    <br/>



1. **How to create a value array from a list of objects?**
  
    Here's the syntax.

    ```yaml
    # Syntax
    EVAL|$list >> $output:
        <property>
    ```
    
    Here's a list.

    ```yaml
    | A  | B  | C  |
    | -- | -- | -- |
    | 10 | 11 | 12 |
    | 20 | 21 | 22 |
    ```
    
    Here's the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml   
    📃 Example:
    
    # Extract only A properties.
    - EVAL|$list >> $output:
        A
    ```

    Here's the `$output`.

    ```yaml
    [10, 20]
    ```



    ---
    <br/>



1. **How to create an object array from a list of objects?**
  
    Here's the syntax.

    ```yaml
    # Syntax
    EVAL|$list >> $output:
        - <property-1>
        - <property-2>
    ```
    
    Here's a list.

    ```yaml
    | A  | B  | C  |
    | -- | -- | -- |
    | 10 | 11 | 12 |
    | 20 | 21 | 22 |
    ```
    
    Here's the [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml  
    📃 Example:

    # Extract only properties A and B.
    - EVAL|$list >> $output:
        - A
        - B
    ```

    Here's the `$output`.

    ```yaml
    - A: 10
      B: 11
      
    - A: 20
      B: 21
    ```

    ---
    <br/>


1. **How to append into lists?**

    > Used by the [`CreateBinds@Broker` 📃 script](<../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/scripts/🤵 Create Binds 📃 script.md>)
    
    <br/>

    To insert a value in a lists, use  `+>` instead of `>>`.
    ```yaml
    📃 Example:
    - EVAL|A +> $list
    - EVAL|B +> $list
    # Results in [A,B]    
    ```

    Here's a alternative syntax using the [`.Add`](<../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>) function in a [Holder 🧠](<../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).

    ```yaml
    📃 Example:
    - EVAL|A >> $list
    - EVAL|$list.Add(A) >> $list
    # Results in [A,B]    
    ```
    
    ---
    <br/>

1. **How to merge two lists?**

    ```yaml
    📃 Merge two lists:
    - EVAL >> $merged:
        :list1:
        :list2:
    ```

    | List1 | List2 | Result
    |-|-|-
    | `A,B` | `B,C` | `A,B,B,C`
    | `{A:1}` | `{B:2},{C:3}`| `{A:1},{B:2},{C:3}`

    ---
    <br/>


1. **How to imitate SQL queries?**

    ```yaml
    📃 Similar to SQL query:
    - EVAL >> $output-list: |

        SELECT          
            A:Col1       # Object composition
            B:Col2       # Aliases
        FROM $input-list    
        
        # Function comparison  
        WHERE Col3.Is($any-value)  

        ORDER BY Col2   # Ordering

        UNION           # Merged lists

        SELECT 1, 2     # Static values
    ```

    ---
    <br/>

