<!-- TODO: beautify -->

# 🔩 {.Keys}

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

> Works with [`.Key`](<Key ⓕ.md>) and [`.Value`](<Value ⓕ.md>)

## FAQ

1. **What's the behavior of .Keys?**
   
    |Type|Input|Output
    |-|-|-
    |[Map 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Map holders.md>)|`{A:1,B:2}` | `[A,B]`

    ---
    <br/>

1. **How to use in a loop?**

    Consider the following [Script 📃](<../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    ```yaml
    - FOR|$map.Keys|$key:
        INFO|Iterating key {$key}
    ```
    Uses: [`FOR`](<../../📃 Commands ⌘/⌘ for control ▶️/FOR 4️⃣/4️⃣ FOR ⌘ cmd.md>) [`INFO`](<../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>