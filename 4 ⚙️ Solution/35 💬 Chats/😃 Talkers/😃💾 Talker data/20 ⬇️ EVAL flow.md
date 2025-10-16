# ⬇️ Talker `EVAL` flow 

> Part of [Talker 😃](<../😃 Talker.md>)

<br/>


1. **What's an EVAL command?**

    An `EVAL` ⬇️
    * is a [Command ⌘](<../😃⚙️ Talker cmds/⌘ Command.md>) 
    * that evaluates strings, objects, and [`{Functions}`](<12 🐍 {Function}.md>)
    * into a placeholder.

    ---
    <br/>

1. **What's the EVAL syntax?**

    ```yaml
    # Objects
    - EVAL >> $output:
        {object}
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<object>` | Object to evaluate | `{A:1, B:$n}`
    |            | Or a simple string | `How nice!`
    |            | Or an interpolated string | `Hi, {$name}`
    | `$output`  | Placeholder for storage | `$my-var`


    ```yaml
    # Functions
    - EVAL|{function} >> $output:
        {input}
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `{function}`| [{Function}](<12 🐍 {Function}.md>) to be evaluated | `{f}` `{$p}` | 
    || Supports missing `{}` | `f` `$p`
    | `{input}`| Input for the `{function}` | `3` `[A,B]` `{A:1}` 
    || Passed as single argument | `f({input})`
    
    ---
    <br/>


1. **How to pass arguments to a function on EVAL?**

    ```yaml
    # Multi-position functions
    - EVAL|f(1,A,$p):
    ```
    
    ```yaml
    # Single-position functions
    - EVAL|f:
        x: 1
        y: A
        z: $p
    ````

    ---
    <br/>
    
1. **What's an object EVAL example?**


    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ The A placeholder has 3.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Placeholder B also has 3.


    ```yaml
    # 😃 Talker.
    💬 Example:
    
    # First message.
    - EVAL >> $A:
        3

    - INFO|The A placeholder has {$A}.

    # Second message.
    - EVAL >> $B:
        Placeholder B also has {$A} 
    - INFO|$B
    ```

    ---
    <br/>

1. **What's a code EVAL example?**
  
    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Add a database row? [Yes, No] | Yes
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ The database now has 9 rows.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Add a database row? [Yes, No] | Yes
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ The database now has 10 rows.
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Add a database row? 


    ```yaml
    # 😃 Talker.
    💬 Example:
    - CONFIRM|Add a database row?
    - EVAL|addRow >> $count
    - SUCCESS|The database now has {$count} rows.
    - REPEAT
    ```


    | [Command ⌘](<../😃⚙️ Talker cmds/⌘ Command.md>) | Purpose
    |-|-
    | 👍 [`CONFIRM`](<../../🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) | To pause for user confirmation.
    | 🔁 [`REPEAT`](<../😃⚙️ Talker cmds/REPEAT 🔁.md>) | To add more rows.


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


1. **What's a object EVAL example?**

    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Welcome to Any Business! <br/> - We are a 3.6 M£ business  <br/> &nbsp;&nbsp; based out of London, UK.


    ```yaml
    # 😃 Talker.
    💬 Example:
    
    # Prepare the data into an object.
    - EVAL >> $data:
        Input:
            Name: Any Business
            Revenue: {get-revenue}
            Address: 
                City: London
                Country: UK

    # Render the intro into a string.
    - EVAL >> $intro:
        Input:
            Welcome to {$data.Name}! \n
            We are a {$data.Revenue} M£ 
            business based out of 
            {$data.Address.City}, 
            {$data.Address.Country}

    # Show the intro.
    - INFO|$intro
    ```

  