# 😃🔩 Talker `{.Set}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Used by [`.Add`](<../../📃 Holders 🧠/Any 📚 holders/Add ⓕ any.md>) and [`SET`](<../../📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>)

## FAQ

1. **What's the syntax for .Set?**

    ```yaml
    .Set(original, change)
    ```

    Input | Purpose | Example
    |-|-|-
    | `original` | Original [Map 🧠 holder](<../../📃 Holders 🧠/Map 📚 holders/🧠 Map holders.md>) | `{A:1,B:2}`
    |           | or [List 🧠 holder](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>) of maps | `{A:1},{A:2}`
    | `change`   | Object with keys/values to set | `{B:3,C:4}`

    ---
    <br/>

1. **What are examples of .Set for [Map 🧠 holders](<../../📃 Holders 🧠/Map 📚 holders/🧠 Map holders.md>)?**

    | Original | Change | Result
    |-|-|-
    | `{A:1,B:2}` | `{A:2}` | `{A:2,B:2}`
    | `{A:1,B:2}` | `{C:3}` | `{A:1,B:2,C:3}`
    | `{A:1,B:2}` | `{A:0,C:3}` | `{A:0,B:2,C:3}`

    ---
    <br/>

1. **What are examples of .Set for [List 🧠 holders](<../../📃 Holders 🧠/List 📚 holders/🧠 List holders.md>)?**

    > This uses the [`.Evaluate`](<../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    ```yaml
    # Lets change      # Into this
    ┌────┬────┬───┐    ┌────┬────┬───┐        
    │ A  │ B  │ C │    │ A  │ B  │ C │   # Add 70 to A     
    ├────┼────┼───┤    ├────┼────┼───┤   # Remove 1 from B
    │ 10 │ 11 │ X │    │ 80 │ 10 │ D │   # Set C to "D"
    │ 20 │ 21 │ Y │    │ 90 │ 20 │ D │        
    └────┴────┴───┘    └────┴────┴───┘        
    ```

    ```yaml
    ┌───────────────────────┬──────────────────────────┐
    │ Explicit with CALL    │ Implicit with SET        │
    ├───────────────────────┼──────────────────────────┤
    │ CALL|.Set >> $output: │ - SET|$input >> $output: │
    │   - $input            │     A.Add(70):           │
    │   - A.Add(70)         │     B.Remove(1):         │
    │   - B.Remove(1)       │     C: D                 │
    │   - C: D              │                          │
    └───────────────────────┴──────────────────────────┘
    ```

    Uses: [`CALL`](<../../📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`SET`](<../../📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>)

    ---
    <br/>