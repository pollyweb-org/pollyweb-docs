# 😃↘️ Talker `SET` command 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ

1. **What's an SET command?**

    `SET` ↘️
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that changes the value of a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    * using the [`.Set`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Set}.md>) function.

    ---
    <br/>

1. **What's the [`SET`](<↘️ SET ⌘ cmd.md>) syntax?**

    |Syntax| Behavior
    |-|-|
    | `SET\|$in: *` | Changes a [Pair 🧠 holder](<../../../📃 Holders 🧠/🧠 Holder types/Pair holders.md>) with [`.Set`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Set}.md>)
    || Equals [`EVAL`](<../EVAL 🧮/🧮 EVAL ⌘ cmd.md>)`\|`[`.Set`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Set}.md>)`>> $in: $in,*`
    |`SET\|$in.f(*)`| Sets a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) to the [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) result
    || Equals [`PUT`](<../PUT ⬇️/⬇️ PUT ⌘ cmd.md>)`\|$in.f(*) >> $in`
    | `SET\|$in >> $out` | Equals [`PUT`](<../PUT ⬇️/⬇️ PUT ⌘ cmd.md>)`\|$in >> $out`
    | `SET\|* >> $out` | Equals [`PUT`](<../PUT ⬇️/⬇️ PUT ⌘ cmd.md>)`\|* >> $out`
    
    

    ---
    <br/>



1. **How to change a single property in a $holder?**
  
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    
    # Create {a:1, b:2}
    - PUT >> $p: 
        a: 1
        b: 2

    # Change to {a:1, b:x, c:z}
    - SET|$p:
        b: x
        c: z
    ```
    Uses: [`PUT`](<../PUT ⬇️/⬇️ PUT ⌘ cmd.md>)

    ---
    <br/>
