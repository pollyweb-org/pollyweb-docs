# 😃🧮 Talker `CALL` command 

> About 
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* Implements [`{code}` 🐍  functions](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>) 
* Implemented by the [`CALL` 📃 script](<🧮 CALL 📃 script.md>)

## FAQ

1. **What is the CALL command?**

    `CALL` 🧮
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that evaluates a `.` prefixed [Built-in 🐍 function](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * or a customized [Code 🐍 function](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>)
    * into a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).

    ---
    <br/>

1. **What's the [`CALL`](<🧮 CALL ⌘ cmd.md>) syntax?**

    |Variation| Behavior
    |-|-|
    | `CALL\|f(*)` | Executes a [{code} 🐍 function](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>) with `*` args
    ||Equals `CALL\|f: *`
    | `CALL\|f(*) >> $out` | Puts [{code} 🐍](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>) results in a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    || Equals `CALL\|f >> $out: *` 
    | `CALL\|.f(*) >> $out` | Executes a built-in [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
    || Equals `CALL\|.f >> $out: *`  
    | `CALL\|$in: *` | Equals [`SET`](<../../⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>)`\|$in: *` 
    | `CALL\|$in >> $out: *` | Equals [`PUT`](<../../⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>)`\|$in >> $out: *`
    | `CALL\|* >> $out` | Equals [`PUT`](<../../⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>)`\|* >> $out`
    | `CALL >> $out: *` | Equals [`PUT`](<../../⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>)` >> $out: *`
    
    ---
    <br/>


1. **How to pass arguments to a [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) on [`CALL`](<🧮 CALL ⌘ cmd.md>)?**

    ```yaml
    # Multi-position functions
    CALL|f(1,A,$p)
    ```
    
    ```yaml
    # Single-position functions
    CALL|f:
        x: 1
        y: A
        z: $p
    ```

    ---
    <br/>
    

1. **What's an [`CALL`](<🧮 CALL ⌘ cmd.md>) example with a [`{code}` function](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>)?**
  
    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Add a database row? [Yes, No] | Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ The database now has 9 rows.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Add a database row? [Yes, No] | Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ The database now has 10 rows.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Add a database row? 

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    - CONFIRM Add a database row?
    - CALL addRow >> $count
    - DONE: The database now has {$count} rows.
    - REPEAT
    ```

    Uses: [`CONFIRM`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/👍 CONFIRM ⌘ cmd.md>) [`CALL`](<🧮 CALL ⌘ cmd.md>) [`REPEAT`](<../../⌘ for control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) [`DONE`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)


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

