# ⬇️ Talker `EVAL` flow 

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>


1. **What's an EVAL command?**

    An `EVAL` ⬇️
    * is a [Command ⌘](<10 ⌘ Command.md>) 
    * that evaluates strings, objects, and [`{Functions}`](<12 🐍 {Function}.md>)
    * into a placeholder.

    ---
    <br/>

1. **What's the EVAL syntax?**

    ```yaml
    # Functions
    - EVAL|{function} >> $output
        {input}

    # Objects
    - EVAL >> $output
        {object}

    # Strings
    - EVAL|<string> >> $output
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `{function}`| [{Function}](<12 🐍 {Function}.md>) to be evaluated. | `{MyFunction}` | 
    | `{arguments}`| Single input for functions. | `3` `[A,B]` `{A:1}` 
    | `<object>` | Object to evaluate. | `{A:1, B:$n}`
    | `<string>` | String to evaluate. | `A` `I'm {$name}`
    | `$output` | Placeholder for storage. | `$out`
    
    ---
    <br/>


1. **How to pass arguments to a function on EVAL?**

    ```yaml
    # Multi-position functions
    - EVAL|{f(1,A,$p)}:
    
    # Single-position functions
    - EVAL|{f}:
        x: 1
        y: A
        z: $p
    ````

    ---
    <br/>
    
1. **What's a string EVAL example?**


    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ The A placeholder has 3.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Placeholder B also has 3.


    ```yaml
    # 😃 Talker.
    💬 Example:
    
    # First message.
    - EVAL|3 >> $A
    - INFO|The A placeholder has {$A}.

    # Second message.
    - EVAL|Placeholder B also has {$A} >> $B
    - INFO|{$B}
    ```

    ---
    <br/>

1. **What's a code EVAL example?**
  
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
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
    - EVAL|{addRow} >> $count
    - SUCCESS|The database now has {$count} rows.
    - REPEAT
    ```


    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | 👍 [`CONFIRM`](<../31 🤔 Prompts/24 👍 CONFIRM prompt.md>) | To pause for user confirmation.
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


4. **What's a object EVAL example?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../31 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Welcome to Any Business! <br/> - We are a 3.6 M£ business  <br/> &nbsp;&nbsp; based out of London, UK.


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
    - INFO|{$intro}
    ```

  