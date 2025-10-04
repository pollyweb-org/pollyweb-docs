# 😃 Talker `EVAL` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's an EVAL command?**

    An `EVAL` is a [Command](<10 Command.md>) that evaluates one of the following expressions into a placeholder.
    
    |Expression|Examples
    |-|-
    |`<string>`| `3` `Alice`
    [`{Function}`](<11 {Function}.md>) | `{$placeholder}` `{handler(1)}` `{.helper(1)}` 

    ---
    <br/>

2. **What's the syntax?**

    ```yaml
    - EVAL|<expression> >> <placeholder>
    ```

    | Argument| Purpose
    |-|-
    | `<expression>`| The string or [{Function}](<11 {Function}.md>) to be evaluated.
    | `<placeholder>`| The placeholder to store the evaluation result.
    
    ---
    <br/>

2. **What's a string example?**




  
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ The placeholder number is 3.


    ```yaml
    # 😃 Talker.
    💬 Example:
    - EVAL|3 >> n
    - INFO|The placeholder number is {$n}.
    ```

    ---
    <br/>

3. **What's a code example?**
  
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Add a database row? [Yes, No] | Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ The database now has 9 rows.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Add a database row? [Yes, No] | Yes
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ✅ The database now has 10 rows.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 Add a database row? 


    ```yaml
    # 😃 Talker.
    💬 Example:
    - CONFIRM|Add a database row?
    - EVAL|{addRow} >> count
    - SUCCESS|The database now has {$count} rows.
    - REPEAT
    ```


    | [Command](<10 Command.md>) | Purpose
    |-|-
    | 👍 [`CONFIRM`](<../13 🤔 Prompts/24 👍 CONFIRM prompt.md>) | To pause for user confirmation.
    | 🔁 [`REPEAT`](<23 🔁 REPEAT flow.md>) | To add more rows.


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
