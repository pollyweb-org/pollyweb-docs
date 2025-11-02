# 😃⬇️ Talker `EVAL` command 

> Part of [Script 📃](<../../📃 basics/Script 📃.md>)

<br/>


1. **What's an EVAL command?**

    An `EVAL` ⬇️
    * is a [Command ⌘](<../../📃 basics/Command ⌘.md>) 
    * that evaluates strings, objects, and [`{Functions}`](<../../📃 basics/Function 🐍.md>)
    * into a holder.

    ---
    <br/>

1. **What's the EVAL syntax?**

    ```yaml
    # Objects
    EVAL >> $output:
        {object}
    ```

    | Input| Purpose | Example
    |-|-|-
    | `<object>` | Object to evaluate | `{A:1, B:$n}`
    |            | Or a simple string | `How nice!`
    |            | Or an interpolated string | `Hi, {$name}`
    | `$output`  | Holder for storage | `$my-var`

    <br/>

    ```yaml
    # Functions
    EVAL|{function} >> $output:
        {input}
    ```

    | Input| Purpose | Example
    |-|-|-
    | `{function}`| [{Function}](<../../📃 basics/Function 🐍.md>) to be evaluated | `{f}` `{$p}` | 
    || Supports missing `{}` | `f` `$p`
    | `{input}`| Input for the `{function}` | `3` `[A,B]` `{A:1}` 
    || Passed as single argument | `f({input})`
    
    ---
    <br/>


1. **How to pass arguments to a function on EVAL?**

    ```yaml
    # Multi-position functions
    EVAL|f(1,A,$p)
    ```
    
    ```yaml
    # Single-position functions
    EVAL|f:
        x: 1
        y: A
        z: $p
    ````

    ---
    <br/>
    
1. **What's an EVAL example with static values?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ The A holder has 3.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Holder B also has 3.

    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

    ```yaml
    📃 Example:
    
    # First message.
    - EVAL >> $A:
        3

    - INFO|The A holder has {$A}.

    # Second message.
    - EVAL >> $B:
        Holder B also has {$A} 
    - INFO|$B
    ```

    ---
    <br/>

1. **What's an EVAL example with code?**
  
    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Add a database row? [Yes, No] | Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ The database now has 9 rows.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Add a database row? [Yes, No] | Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ The database now has 10 rows.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Add a database row? 

    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

    ```yaml
    📃 Example:
    - CONFIRM|Add a database row?
    - EVAL|addRow >> $count
    - SUCCESS|The database now has {$count} rows.
    - REPEAT
    ```

    Commands: [`CONFIRM`](<../../../Prompts 🤔/🤔✏️ Prompt inputs/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`EVAL`](<⬇️ EVAL ⌘ cmd.md>) [`REPEAT`](<../../📃 control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) [`SUCCESS`](<../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)


    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['Function']:
        case 'addRow':
          rowCount = insertDatabaseRow()
          return rowCount
    ```
       
    ---
    <br/>


1. **What's an EVAL example with objects?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Welcome to Any Business! <br/> - We are a 3.6 M£ business  <br/> &nbsp;&nbsp; based out of London, UK.
    |

    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

    ```yaml
    📃 Example:

    # Prepare the data into an object.
    - EVAL >> $data:
        Input:
            Name: Any Business
            Revenue: {get-revenue}
            Address: 
                City: London
                Country: UK

    # Render the intro into a string.
    - EVAL >> $intro:
        Input:
            Welcome to {$data.Name}! \n
            We are a {$data.Revenue} M£ 
            business based out of 
            {$data.Address.City}, 
            {$data.Address.Country}

    # Show the intro.
    - INFO|$intro
    ```

    Commands: [`EVAL`](<⬇️ EVAL ⌘ cmd.md>) [`INFO`](<../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>


1. **How to change a single property in a $holder?**
  
    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

    ```yaml
    📃 Example:
    
    # Create {a:1, b:2}
    - EVAL >> $p: 
        a: 1
        b: 2

    # Change to {a:1, b:x, c:z}
    - EVAL|$p:
        b: x
        c: z
    ```

    ---
    <br/>



1. **How to merge objects in an EVAL?**

    With a mix of dictionary values and [Holder 🧠](<../../📃 basics/Holder 🧠.md>) surrounded with `:`.
    
    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

    ```yaml
    📃 Example:

    # $partB: {B:2}
    - EVAL >> $partB:
        B: 2

    # $partC: {C:3}
    - EVAL >> $partC:
        C: 3

    # $output: {A:1, B:2, C:3, D:4}
    - EVAL >> $output:
        A: 1
        :{$partB}:
        :{$partC}:
        D: 4
    ```
    
    In the example above, `$output` has `{A:1,B:2,C:3,D:4}`.


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
    || `$list` | [Holder 🧠](<../../📃 basics/Holder 🧠.md>) list of objects
    ||| Fails if `$list` was never set
    |

    Here's a list.

    ```yaml
    | A  | B  | C  |
    | -- | -- | -- |
    | 10 | 11 | 12 |
    | 20 | 21 | 22 |
    ```

    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

    ```yaml
    📃 Example:

    # Extract only A and B properties.
    - EVAL|$list >> $output:
        Alpha: A
        Beta: B
    ```

    Here's the `$output`.

    ```yaml
    | Alpha | Beta |
    | ----- | ---- |
    |    10 |   11 |
    |    20 |   21 |
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
    
    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

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
    
    Here's the [Script 📃](<../../📃 basics/Script 📃.md>).

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

1. **How to merge lists with FROM-MATCH?**


    Consider the 1st list `$items`.

    ```yaml
    # Items
    | ID | Price | SupID  |
    | -- | ----- | ------ |
    |  1 |    10 |      A |
    |  2 |    20 |      X |
    |  3 |    30 |      X |
    ```


    And the 2nd list `$suppliers`.

    ```yaml
    # Suppliers
    | ID | Name |
    | -- | ---- |
    |  A |  ABC |
    |  X | XPTO |
    |  Y |  ANY |
    ```
    
    Let's merge them with [`EVAL`](<⬇️ EVAL ⌘ cmd.md>).

    
    ```yaml
    📃 Merge:
    
    - EVAL|$items >> $merged:
        Item: ID
        Supplier: Name #, other, another
            FROM $suppliers
            MATCH SupID, $suppliers.ID
    ```
    
    Here's the final `$merged` list.

    ```yaml
    | ITEM | SUPPLIER |
    | ---- | -------- |
    |    1 |      ABC |
    |    2 |     XPTO |
    |    3 |     XPTO |
    ```


    Here's the syntax.

    ```yaml
    # Syntax
    EVAL|$list-A >> $merged:
        <original-property>: <list-A-property>
        <merged-property>: 
            <list-B-1-property>, <list-B-n-property>
            FROM $list-B
            MATCH <list-match-A>, $list-B.<list-match-B>
    ```

    <br/>
    
1. **How to filter lists with FROM-MATCH?**

    

    Here's an example using the same lists as before.

    ```yaml
    📃 Filter with a list of values:
    # List: X, Y
    - EVAL|X,Y >> $filtered:
        FROM $suppliers
        MATCH $suppliers.ID
    ```

    ```yaml
    📃 Filter with a list of objects:
    #   List: {Key:X},{Key:Y}
    - EVAL|{Key:X},{Key:Y} >> $filtered:
        FROM $suppliers
        MATCH Key, $suppliers.ID
    ```
    
    Here's the final `$filtered` list.

    ```yaml
    # Suppliers
    | ID | Name |
    | -- | ---- |
    |  X | XPTO |
    |  Y |  ANY |
    ```

    Here's the syntax.

    ```yaml
    # Syntax to filter with a list of values
    EVAL|$list-of-values >> $filtered:
        FROM $list
        MATCH $list.<matching-property>

    # Syntax to filter with a list of objects
    EVAL|$list-of-objects >> $filtered:
        FROM $list
        MATCH <object-property>, $list.<matching-property>
    ```

    ---
    <br/>


1. **How to append into lists?**

    > Used by the [`CreateBinds@Broker` 📃 script](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 📃 part 2.md>)
    
    <br/>

    To insert a value in a lists, use  `+>` instead of `>>`.
    ```yaml
    📃 Example:
    - EVAL|A +> $list
    - EVAL|B +> $list
    # Results in [A,B]    
    ```

    Here's a alternative syntax using the [`.Add`](<../../📃 functions 🐍/🔩 {.Add}.md>) function in a [Holder 🧠](<../../📃 basics/Holder 🧠.md>).

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

1. **How to make a distinct in lists?**

    Using the [`{.Distinct}`](<../../📃 functions 🐍/🔩 {.Distinct}.md>) function

    ```yaml
    📃 Inline in a holder:
    - EVAL|$list.Distinct() >> $list
    ```

    ```yaml
    📃 Break down in a single list:
    - EVAL|.Distinct >> $distinct:
        $list
    ```

    ```yaml
    📃 Distinct after merging multiple lists:
    - EVAL|.Distinct >> $distinct:
        :$list-1:
        :$list-n:
    ```
    
    ---
    <br/>

1. **How to imitate SQL queries?**

    ```yaml
    📃 Similar to SQL query:
    - EVAL >> $output-list:
        Col1, Col2              # Similar to SELECT 
        FROM $input-list        # Similar to FROM
        MATCH Col3, $any-value  # Similar to WHERE
    ```

    ---
    <br/>

