# 😃↘️ Talker `SET` command 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ

1. **What's an SET command?**

    `SET` ↘️
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that changes the value of a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    * using the [`.Set`](<../../../📃 Holders 🧠/Any 📚 holders/Set ⓕ.md>) function.

    ---
    <br/>

1. **What's the [`SET`](<↘️ SET ⌘ cmd.md>) syntax?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    |Syntax| Behavior
    |-|-|
    | `SET\|$in: *` | Changes a [Map 🧠 holder](<../../../📃 Holders 🧠/Map 📚 holders/🧠 Map holders.md>) with [`.Set`](<../../../📃 Holders 🧠/Any 📚 holders/Set ⓕ.md>)
    || Equals [`CALL`](<../CALL 🧮/🧮 CALL ⌘ cmd.md>)`\|`[`.Set`](<../../../📃 Holders 🧠/Any 📚 holders/Set ⓕ.md>)`>> $in: $in,*`
    |`SET\|$in.f(*)`| Sets a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) to the [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) result
    || Equals [`CALL`](<../CALL 🧮/🧮 CALL ⌘ cmd.md>)`\|`[`.Set`](<../../../📃 Holders 🧠/Any 📚 holders/Set ⓕ.md>)`($in,$in.f(*)) >> $in`
    | `SET\|$in >> $out` | Adds `$in` to `$out`
    || Equals [`CALL`](<../CALL 🧮/🧮 CALL ⌘ cmd.md>)`\|`[`.Set`](<../../../📃 Holders 🧠/Any 📚 holders/Set ⓕ.md>)`($out,$in) >> $out`
    | `SET\|$in >> $out: *` | Adds parts of `$in` into `$out`
    || Equals [`CALL`](<../CALL 🧮/🧮 CALL ⌘ cmd.md>)`\|`[`.Set`](<../../../📃 Holders 🧠/Any 📚 holders/Set ⓕ.md>)`>> $out: $in,*`
    | `SET\|* >> $out` | Replaces the content of `$out` with `*`
    || Equals [`PUT`](<../PUT ⬇️/⬇️ PUT ⌘ cmd.md>)`\|* >> $out`
    
    

    ---
    <br/>



1. **How to change a single property in a $holder?**
  
    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

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
