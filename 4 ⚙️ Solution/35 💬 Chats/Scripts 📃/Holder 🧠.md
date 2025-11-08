# 😃🧠 Talker `$holder` 

> Part of [Script 📃](<Script 📃.md>)

<br/>


1. **What is a Talker $holder?**

    A `$holder`
    * is a named memory slot 
    * associated with a [Chat 💬](<../Chats 💬/💬 Chat.md>)
    * and managed by a [Script 📃](<Script 📃.md>).

    ---
    <br/>

1. **What are the system holders?**

    | Holder 🧠 | Details
    |-|-
    | [`$.Chat`](<../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>) | Contains the details of the current  [Chat 💬](<../Chats 💬/💬 Chat.md>) 
    | [`$.Inputs`](<../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Inputs ▶️/▶️ $.Inputs 🧠 holder.md>) | Contains the inputs of the current [`RUN` command](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>) 
    | [`$.Msg`](<../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) | Contains the properties of the current [Message 📨](<../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)
    | [`$.Hosted`](<../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) | Contains the settings of the [Hosted 📦 domain](<../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>)

    ---
    <br/>

1. **How to read a $holder?**

    In a [Script 📃](<Script 📃.md>),
    * holders are prefixed with a dollar sign;
    * e.g., `$p` to reference holder named `p`.

    In Python 🐍 code, 
    * use the holder handler;
    * e.g., `.Holders.Get('$p')`.

    ---
    <br/>


1. **How to read properties from $holder objects?**

    In a [Script 📃](<Script 📃.md>), use the `dot` notation to access properties:
    * `$p.MyProp` reads property `MyProp`
    * `$p.L1.L2` reads property `L2` of property `L1`

    In Python 🐍 code, use the holder handler:
    * `.Holders.Get('$p.MyProp')` reads `MyProp`
    * `.Holders.Get('$p.L1.L2')` reads `L2` of `L1`

    ---
    <br/>

1. **Is there a default $holder property?**

    Yes. 
    * If a holder object `$p` has a `.$` property, 
    * then reading `$p` is the same as reading `$p.$`.

    Here's a [Script 📃](<Script 📃.md>).
    ```yaml
    📃 Example: 

    - PUT >> $p:
        A: 10
        B: 20
        $: 30

    - INFO|$p.A.  # show 10
    - INFO|$p     # show 30
    ```
    Uses: [`EVAL`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`INFO`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>


1. **How to read lists of values?**

    To loop a list holder called $list use [`PARALLEL`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>).
    
    Here's a [Script 📃](<Script 📃.md>).
    ```yaml
    📃 Example: 
    
    # Evaluate [A,B,C] into $list
    - PUT|A,B,C >> $list 

    # This shows C, A, and B, in any order
    - PARALLEL|$list|$number:
        - INFO|$number
    ```
    Uses: [`EVAL`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`INFO`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`PARALLEL`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`PUT`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>)

    ---
    <br/>

1. **How to get get the length of a list?**    

    Use the [`{.Size} function`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Size}.md>) with `$p.Length()` or `$p.Size()`.

    Here's a [Script 📃](<Script 📃.md>).
    ```yaml
    📃 Example: 

    # Create a list
    - PUT|A,B,C >> $list # [A,B,C]

    # Show the length
    - INFO|$list.Length() # Shows 3
    - INFO|$list.Size() # Shows 3
    ```
    Uses: [`EVAL`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`INFO`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`PUT`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>)

    ---
    <br/>

1. **How to group object properties from lists?**
    
    Lists of properties allow for grouping properties into lists of values.
    
    Here's a [Script 📃](<Script 📃.md>).
    ```yaml
    📃 Example: 

    # Create a list of objects
    - PUT|{A:1},{A:2} >> $list

    # Show the list of values in property A
    - INFO|$list.A   # Shows [1,2]
    ```
    Uses: [`EVAL`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`INFO`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`PUT`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>)

    ---
    <br/>

1. **How to write to a holder?**

    In Python 🐍 code, use the holder handler:
    * `.Holders.Set('$p', new_value)` 

    In a [Script 📃](<Script 📃.md>), use `>>` to send a value to a $holder:
    * [`TEXT`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>)`|bla >> $p` puts the answer to a [`TEXT` 🔠 input](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/TEXT 🔠/TEXT 🔠 prompt.md>).
    * [`EVAL`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>)`|f >> $p` puts the return of a [{Function}](<Function 🐍.md>) named `f`.
    * [`PUT`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>)`|X >> $p` puts the string `X`.

    ```yaml
    PUT >> $p:   # Write values
      123
    ```
        
    ```yaml
    PUT >> $p:   # Write lists
      - A
      - B
    ```

    ```yaml
    PUT >> $p:   # Write objects
      A: 1
      B: 2
    ```

    ```yaml 
    PUT >> $p:   # Merge objects with ':object:'
      A: 1
      $another-holder:
      B: 2
    ```

    ---
    <br>

1. **How to change the properties of an object holder?**

    Use [`PUT`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) and [`SET`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>).

    Here's a [Script 📃](<Script 📃.md>).
    ```yaml
    📃 Example:

    # Set {A:1,B:2}
    - PUT >> $p:  
        A: 1
        B: 2

    # Changed to {A:1, B:200, C3}
    - SET|$p: 
        B: 200
        C: 3
    ```

    ---
    <br/>
  
1. **How to integrate functions?**

    Holders allow [{Function} 🐍](<Function 🐍.md>) suffixes.

    * The function is called with the first argument as the holder.
  
    | Function | Holder `$p` | Example | Result
    |-|-|-|-
    | [`.Add`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Add}.md>) | `[A,B]` | `$p.Add(C)` | `[A,B,C]`
    | [`.Diff`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Diff}.md>) | `[A,B,C]` | `$p.Diff(B)` | `[A,C]`
    | [`.IsIn`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsIn}.md>) | `A` | `$.IsIn([A,B])` | `True`
    | [`.Length`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Size}.md>) | `[A,B]` | `$p.Length()` | `2`
    | [`.Size`](<../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Size}.md>) | `[A,B]` | `$p.Size()` | `2`
    
    ---
    <br/>

1. **How to reference a holder by name?**

    > Used in the [`ASK`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/ASK 🙋/🙋 ASK ⌘ cmd.md>) command

    Leverage `{$*}` interpolation with [Commands ⌘](<Command ⌘.md>).

    ```yaml
    📃 Example:

    - PUT|p >> $name
    - PUT|123 >> {$name}
    - INFO|The value of $p is {$p}

    # This shows: 
    #    The value of p is 123
    ```
    Uses: [`EVAL`](<../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`INFO`](<../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>