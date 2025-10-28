# 😃🧠 Talker `$placeholder` 

> Part of [Talker 😃](<../../😃 Talker role.md>)

<br/>


1. **What is a Talker $placeholder?**

    A `$placeholder`
    * is a named memory slot 
    * associated with a [Chat 💬](<../../../💬 Chats/💬 Chat.md>)
    * and managed by a [Talker 😃](<../../😃 Talker role.md>).

    ---
    <br/>


1. **How to read a $placeholder?**

    In a [Talker 😃](<../../😃 Talker role.md>) script,
    * placeholders are prefixed with a dollar sign;
    * e.g., `$p` to reference placeholder named `p`.

    In Python 🐍 code, 
    * use the placeholder handler;
    * e.g., `.Placeholders.Get('$p')`.

    ---
    <br/>


1. **How to read properties from $placeholder objects?**

    In a [Talker 😃](<../../😃 Talker role.md>) script, use `dot` notation to access properties:
    * `$p.MyProp` reads property `MyProp`
    * `$p.L1.L2` reads property `L2` of property `L1`

    In Python 🐍 code, use the placeholder handler:
    * `.Placeholders.Get('$p.MyProp')` reads `MyProp`
    * `.Placeholders.Get('$p.L1.L2')` reads `L2` of `L1`

    ---
    <br/>

1. **Is there a default $placeholder property?**

    Yes. 
    * If a placeholder object `$p` has a `.$` property, 
    * then reading `$p` is the same as reading `$p.$`.

    Here's a [Script 📃](<../...commands ⌘/Script 📃/📃 Script.md>).
    ```yaml
    📃 Example: 

    - EVAL >> $p:
        A: 10
        B: 20
        $: 30

    - INFO|$p.A.  # show 10
    - INFO|$p     # show 30
    ```
    Commands: [`EVAL`](<EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>


1. **How to read lists of values?**

    To loop a list placeholder called $list use [`PARALLEL`](<../...control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>).
    
    Here's a [Script 📃](<../...commands ⌘/Script 📃/📃 Script.md>).
    ```yaml
    📃 Example: 
    
    # Evaluate [A,B,C] into $list
    - EVAL|A,B,C >> $list 

    # This shows C, A, and B, in any order
    - PARALLEL|$list|$number:
        - INFO|$number
    ```
    Commands: [`EVAL`](<EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`PARALLEL`](<../...control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>)

    ---
    <br/>

1. **How to get get the length of a list?**    

    Use the [`{.Size} function`](<../...functions 🐍/🔩 {.Size}.md>) with `$p.Length()` or `$p.Size()`.

    Here's a [Script 📃](<../...commands ⌘/Script 📃/📃 Script.md>).
    ```yaml
    📃 Example: 

    # Create a list
    - EVAL|A,B,C >> $list # [A,B,C]

    # Show the length
    - INFO|$list.Length() # Shows 3
    - INFO|$list.Size() # Shows 3
    ```
    Commands: [`EVAL`](<EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>

1. **How to group object properties from lists?**
    
    Lists of properties allow for grouping properties into lists of values.
    
    Here's a [Script 📃](<../...commands ⌘/Script 📃/📃 Script.md>).
    ```yaml
    📃 Example: 

    # Create a list of objects
    - EVAL|{A:1},{A:2} >> $list

    # Show the list of values in property A
    - INFO|$list.A   # Shows [1,2]
    ```
    Commands: [`EVAL`](<EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>

1. **How to write to a placeholder?**

    In Python 🐍 code, use the placeholder handler:
    * `.Placeholders.Set('$p', new_value)` 

    In a [Talker 😃](<../../😃 Talker role.md>) script, use `>>` to send a value to a $placeholder:
    * `TEXT|bla >> $p` writes the answer to a [`TEXT` 🔠 input](<../../../🤔 Prompts/🤔✏️ Prompt inputs/TEXT 🔠/TEXT 🔠 prompt.md>).
    * `EVAL|f >> $p` writes the return of a [{Function}](<../...functions 🐍/{Function} 🐍.md>) named `f`.

    You can also push data structures with [`EVAL` ⬇️](<EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>).
    
    ```yaml
    EVAL >> $p:   # Write values
      123
    ```
        
    ```yaml
    EVAL >> $p:   # Write lists
      - A
      - B
    ```

    ```yaml
    EVAL >> $p:   # Write objects
      A: 1
      B: 2
    ```

    ```yaml 
    EVAL >> $p:   # Merge objects with ':object:'
      A: 1
      :$another-placeholder:
      B: 2
    ```

    ---
    <br>

1. **How to change the properties of an object placeholder?**

    Use [`EVAL`](<EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>).

    Here's a [Script 📃](<../...commands ⌘/Script 📃/📃 Script.md>).
    ```yaml
    📃 Example:

    # Set {A:1,B:2}
    - EVAL >> $p:  
        A: 1
        B: 2

    # Changed to {A:1, B:200, C3}
    - EVAL|$p: 
        B: 200
        C: 3
    ```

    ---
    <br/>
  
1. **How to integrate functions?**

    Placeholders allow [{Function} 🐍](<../...functions 🐍/{Function} 🐍.md>) suffixes.

    * The function is called with the first argument as the placeholder.
  
    | Function | Holder `$p` | Example | Result
    |-|-|-|-
    | [`.Add`](<../...functions 🐍/🔩 {.Add}.md>) | `[A,B]` | `$p.Add(C)` | `[A,B,C]`
    | [`.Diff`](<../...functions 🐍/🔩 {.Diff}.md>) | `[A,B,C]` | `$p.Diff(B)` | `[A,C]`
    | [`.In`](<../...functions 🐍/🔩 {.In}.md>) | `A` | `$.In([A,B])` | `True`
    | [`.Length`](<../...functions 🐍/🔩 {.Size}.md>) | `[A,B]` | `$p.Length()` | `2`
    | [`.Size`](<../...functions 🐍/🔩 {.Size}.md>) | `[A,B]` | `$p.Size()` | `2`
    
    ---
    <br/>

1. **How to reference a placeholder by name?**

    > Used in the [`FILTER`](<../...methods 🤵/FILTER 🔽/🔽 FILTER ⌘ cmd.md>) command

    Leverage `{$*}` interpolation with [Commands ⌘](<../...commands ⌘/Command ⌘/⌘ Command.md>).

    ```yaml
    📃 Example:

    - EVAL|p >> $name
    - EVAL|123 >> {$name}
    - INFO|The value of $p is {$p}

    # This shows: 
    #    The value of p is 123
    ```
    Commands: [`EVAL`](<EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>