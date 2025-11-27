# 😃🔩 Talker `{.IsAfter}` function

> Part of [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)

## FAQ

1. **What is the .IsAfter function?**

    `{.IsAfter}`
    * is a [{Function} 🐍](<../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * that returns `True` if a [Time 🧠 holder](<../../📃 Holders 🧠/Input holders 📥/🧠 Time holders.md>) input is after the other
    * or `False` otherwise.

    ---
    <br/>

1. **How does .IsAfter comparisons work?**

    | Situation | Behavior | Input 1 | Input 2 | Result 
    |-|-|-|-|-
    | `Time` | Compared  |`2023-01-03Z` | `2023-01-02Z`   | ✅ True
    | `Empties` | Ignored | `$empty` | `2023-01-01Z` | ❌ False
    | `Others` | Blocked | `2023-01-01T10:00Z` | `ABC` | 🚫 Blocked
    | | | `2023-01-01T10:00Z` | `1.0` | 🚫 Blocked

    ---
    <br/>