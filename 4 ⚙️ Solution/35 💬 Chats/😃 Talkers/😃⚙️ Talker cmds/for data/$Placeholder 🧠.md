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

    ---
    <br/>




1. **How to write to a placeholder?**

    In Python 🐍 code, use the placeholder handler:
    * `.Placeholders.Set('$p', new_value)` 

    In a [Talker 😃](<../../😃 Talker role.md>) script, use `>>` to send a value to a $placeholder:
    * `TEXT|bla >> $p` writes the answer to a [`TEXT` 🔠 input](<../../../🤔 Prompts/🤔✏️ Prompt inputs/32 🔠 TEXT prompt.md>).
    * `EVAL|f >> $p` writes the return of a [{Function}](<{Function} 🐍.md>) named `f`.

    You can also push data structures with [`EVAL` ⬇️](<EVAL ⬇️ flow.md>).
    
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

    ---
    <br>

