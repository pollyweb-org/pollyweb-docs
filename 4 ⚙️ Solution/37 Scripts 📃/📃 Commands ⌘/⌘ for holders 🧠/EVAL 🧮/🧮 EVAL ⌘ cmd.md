# 😃🧮 Talker `EVAL` command 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ

1. **What's an EVAL command?**

    An `EVAL` 🧮
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that evaluates a `.` prefixed [Built-in 🐍 function](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) 
    * or a customized [Code 🐍 function](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>)
    * into a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>).

    ---
    <br/>

1. **What's the [`EVAL`](<🧮 EVAL ⌘ cmd.md>) syntax?**

    |Variation| Behavior
    |-|-|
    | `EVAL\|f(*)` | Executes a [{code} 🐍 function](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>) with `*` args
    ||Same as `EVAL\|f: *`
    | `EVAL\|f(*) >> $out` | Puts [{code} 🐍](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>) results in a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    || Same as `EVAL\|f >> $out: *` 
    | `EVAL\|.f >> $out: *` | Executes a built-in [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
    || Same as `EVAL\|.f >> $out: *`    

    ---
    <br/>


1. **How to pass arguments to a [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) on [`EVAL`](<🧮 EVAL ⌘ cmd.md>)?**

    ```yaml
    # Multi-position functions
    EVAL|f(1,A,$p)
    ```
    
    ```yaml
    # Single-position functions
    EVAL|f:
        x: 1
        y: A
        z: $p
    ```

    ---
    <br/>
    

1. **What's an [`EVAL`](<🧮 EVAL ⌘ cmd.md>) example with a [`{code}` function](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>)?**
  
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
    - CONFIRM|Add a database row?
    - EVAL|addRow >> $count
    - SUCCESS|The database now has {$count} rows.
    - REPEAT
    ```

    Uses: [`CONFIRM`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`EVAL`](<🧮 EVAL ⌘ cmd.md>) [`REPEAT`](<../../⌘ for control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) [`SUCCESS`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)


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

