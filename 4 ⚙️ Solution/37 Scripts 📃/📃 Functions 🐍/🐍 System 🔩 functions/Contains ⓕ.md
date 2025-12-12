# 😃🔩 Talker `{.Contains}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ


1. **What's the behavior of .Contains?**

    |Type|Returns|Behavior
    |-|-|-
    |[Text 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>)   |bool| Is the given [Text 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>) a subs string?
    |[Period 🧠](<../../📃 Holders 🧠/Output holders 📤/Period holders.md>) |bool| Is the given [Time 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>) in the date interval?
    |[List 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>)   |bool| Is the given value in the [List 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>)?
    |[Map 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)    |bool| Is the given key in the [`.Keys`](<Keys ⓕ.md>) list?
    |[Set 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>)    |bool| Is the given [Map 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>) in the [Set 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Set holders.md>)?

    ---
    <br/>

1. **What's the .Contains syntax?**

    ```yaml
    .Contains($source, value)
    ```

    | Inputs | Purpose | Examples
    |-|-|-
    | `$source` | Collection to look into | `[1,ABC]` `ABCD` `.Last(year)`
    | `value`  | Value to look for | `1` `ABC` 

    ---
    <br/>

1. **What are examples of .Contains for lists?**
    
    | [List 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 List holders.md>) |Value  |Result
    |-|-|-
    | ... | `{empty}`  | ❌ False
    | `{empty}`  | ... | ❌ False
    | `B,C,D,A` |`A`  | ✅ True
    | `Y,Z` |`X`  | ❌ False
    
    ---
    <br/>


1. **What are examples of .Contains for strings?**

    [Text 🧠](<../../📃 Holders 🧠/Input holders 📥/🧠 Text holders.md>) | Value |Result
    |-|-|-
    | `{empty}` | ... | ❌ False
    | `AB` | `ABC`| ✅ True
    | `BA` | `ABC`| ❌ False

    ---
    <br/>


1. **What are examples of .Contains for [Map 🧠 holders](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)?**

    Value 1 | Value 2 |Result|Reason
    |-|-|-|-
    | `{empty}` | ... | ❌ False | An empty map contains nothing
    |`B` | `{A:1,B:2}` | ✅ True | Key `B` exists with a value
    |`B` | `{A:1,B:}` | ❌ False | Key `B` exists but has no value
    |`B:2` | `{A:1,B:2,C:3}` | ✅ True | Key `B` exists with value `2`
    |`B:4` | `{A:1,B:2,C:3}` | ❌ False | Key `B` exists but has a different value

    ---
    <br/>


1. **How to use .Contains in a Script?**

    Here's a [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

    ```yaml
    📃 Example:

    # Let's set a list
    - PUT: 1,2,3 >> $p

    # Use with IFs
    - IF $p.Contains(1): 
        INFO Found!   

    # Use with ASSERTs
    - ASSERT:           
        $p.Contains(1)
    ```
    Uses: [`ASSERT`](<../../📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CALL`](<../../📃 Commands ⌘/⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`IF`](<../../📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`INFO`](<../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>
