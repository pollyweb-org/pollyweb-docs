# 😃⬇️ Talker `EVAL` command 

> Part of [Talker 😃](<../../😃 Talker role.md>)

<br/>


1. **What's an EVAL command?**

    An `EVAL` ⬇️
    * is a [Command ⌘](<../...commands/⌘ Command.md>) 
    * that evaluates strings, objects, and [`{Functions}`](<../...functions/{Function} 🐍.md>)
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

    <br/>

    ```yaml
    # Functions
    - EVAL|{function} >> $output:
        {input}
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `{function}`| [{Function}](<../...functions/{Function} 🐍.md>) to be evaluated | `{f}` `{$p}` | 
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
    
1. **What's an EVAL example with static values?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ The A placeholder has 3.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Placeholder B also has 3.


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

1. **What's an EVAL example with code?**
  
    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Add a database row? [Yes, No] | Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ The database now has 9 rows.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Add a database row? [Yes, No] | Yes
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ The database now has 10 rows.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Add a database row? 


    ```yaml
    # 😃 Talker.
    💬 Example:
    - CONFIRM|Add a database row?
    - EVAL|addRow >> $count
    - SUCCESS|The database now has {$count} rows.
    - REPEAT
    ```

    Commands: [`CONFIRM`](<../../../🤔 Prompts/🤔✏️ Prompt inputs/31 👍 CONFIRM prompt.md>) [`EVAL`](<EVAL ⬇️ flow.md>) [`REPEAT`](<../for control/REPEAT 🔁.md>) [`SUCCESS`](<../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>)


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


1. **What's an EVAL example with objects?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Welcome to Any Business! <br/> - We are a 3.6 M£ business  <br/> &nbsp;&nbsp; based out of London, UK.


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

    Commands: [`EVAL`](<EVAL ⬇️ flow.md>) [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️ prompt.md>)

    ---
    <br/>


1. **How to change a single property in a $placeholder?**
  
    ```yaml
    # Create {a:1, b:2}
    - EVAL >> $p: 
        a: 1
        b: 2

    # Change to {a:1, b:x, c:z}
    - EVAL|$p:
        b: x
        c: z
    ```

    ---
    <br/>



1. **How to merge objects in an EVAL?**

    With a mix of dictionary values and [Placeholder 🧠](<$Placeholder 🧠.md>) surrounded with `:`.
    
    ```yaml
    - EVAL >> $partB:
        B: 2

    - EVAL >> $partC:
        C: 3

    - EVAL >> $output:
        A: 1
        :{$partB}:
        :{$partC}:
        D: 4
    ```
    
    In the example above, `$output` has `{A:1,B:2,C:3,D:4}`.


    ---
    <br/>


1. **How to format a list of objects?**

    Here's the syntax.

    ```yaml
    # Syntax - fails if $list was never set
    EVAL|$list >> $output:
        {object}
    ```

    ||Arguments| Purpose
    |-|-|-
    || `$list` | [Placeholder 🧠](<$Placeholder 🧠.md>) list of objects
    ||| Fails if `$list` was never set
    |

    Here's a list.

    ```yaml
    | A  | B  | C  |
    | -- | -- | -- |
    | 10 | 11 | 12 |
    | 20 | 21 | 22 |
    ```

    Here's the [Script 📃](<../for control/📃 Script.md>).

    ```yaml
    # Extract only A and B properties.
    - EVAL|$list >> $output:
        Alpha: A
        Beta: B
    ```

    Here's the `$output`.

    ```yaml
    | Alpha | Beta |
    | ----- | ---- |
    |    10 |   11 |
    |    20 |   21 |
    ```

    ---
    <br/>



1. **How to create a value array from a list of objects?**
  
    Here's the syntax.

    ```yaml
    # Syntax
    EVAL|$list >> $output:
        <property>
    ```
    
    Here's a list.

    ```yaml
    | A  | B  | C  |
    | -- | -- | -- |
    | 10 | 11 | 12 |
    | 20 | 21 | 22 |
    ```
    
    Here's the [Script 📃](<../for control/📃 Script.md>).

    ```yaml   
    # Extract only A properties.
    - EVAL|$list >> $output:
        A
    ```

    Here's the `$output`.

    ```yaml
    [10, 20]
    ```



    ---
    <br/>