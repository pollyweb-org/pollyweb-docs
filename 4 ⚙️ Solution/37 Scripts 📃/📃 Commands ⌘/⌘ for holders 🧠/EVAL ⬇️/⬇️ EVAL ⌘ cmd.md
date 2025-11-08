# 😃⬇️ Talker `EVAL` command 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ

1. **What's an EVAL command?**

    An `EVAL` ⬇️
    * is a [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that evaluates strings, objects, and [`{Functions}`](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
    * into a holder.

    ---
    <br/>

1. **What's the [`EVAL`](<⬇️ EVAL ⌘ cmd.md>) syntax?**

    |Variation| Behavior
    |-|-|
    | `EVAL\|{f(*)}` | Executes a [{code} 🐍 function](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>) with `*` args
    ||Same as `EVAL\|{f}: *`
    | `EVAL\|{f(*)} >> $out` | Puts [{code} 🐍](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>) results in a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    || Same as `EVAL\|{f} >> $out: *` 
    | `EVAL\|.f >> $out: *` | Executes a built-in [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>)
    || Same as `EVAL\|{.f} >> $out: *`
    | `EVAL\|$in >> $out` | Puts the content of a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) in another
    || Same as `EVAL >> $out: $in`
    | `EVAL\|*{$in}* >> $out` | Interpolates [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) into a [Text 🧠 holder](<../../../📃 Holders 🧠/🧠 Holder types/Text holders.md>)
    || Same a `EVAL >> $out: *{$in}*`
    | `EVAL\|$lst >> $out: *` | Formats a [List 🧠 holder](<../../../📃 Holders 🧠/🧠 Holder types/List holders.md>) with [`.List`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.List}.md>)
    || Same as `EVAL\|.List >> $out: $lst,*`
    | `EVAL\|$in: *` | Changes a [Pair 🧠 holder](<../../../📃 Holders 🧠/🧠 Holder types/Pair holders.md>) with [`.Set`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Set}.md>)
    || Same as `EVAL\|.Set: $in,*`
    | `EVAL\|* >> $out` | Puts simple content in a [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    || Same as `EVAL >> $out: *` 
    
    
    
    

    ---
    <br/>


1. **How to pass arguments to a [{Function} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) on [`EVAL`](<⬇️ EVAL ⌘ cmd.md>)?**

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
    ````

    ---
    <br/>
    
1. **What's an [`EVAL`](<⬇️ EVAL ⌘ cmd.md>) example with static values?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ The A holder has 3.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Holder B also has 3.

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    
    # First message.
    - EVAL >> $A:
        3

    - INFO|The A holder has {$A}.

    # Second message.
    - EVAL >> $B:
        Holder B also has {$A} 
    - INFO|$B
    ```

    ---
    <br/>

1. **What's an [`EVAL`](<⬇️ EVAL ⌘ cmd.md>) example with a [`{code}` function](<../../../📃 Functions 🐍/🐍 Functions types/🐍 {code}.md>)?**
  
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

    Commands: [`CONFIRM`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/CONFIRM 👍/CONFIRM 👍 prompt.md>) [`EVAL`](<⬇️ EVAL ⌘ cmd.md>) [`REPEAT`](<../../⌘ for control ▶️/REPEAT 🔁/🔁 REPEAT ⌘ cmd.md>) [`SUCCESS`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/SUCCESS ✅/SUCCESS ✅ prompt.md>)


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


1. **What's an EVAL example with [Pair 🧠 holders](<../../../📃 Holders 🧠/🧠 Holder types/Pair holders.md>)?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Welcome to Any Business! <br/> - We are a 3.6 M£ business  <br/> &nbsp;&nbsp; based out of London, UK.
    |

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

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

    Commands: [`EVAL`](<⬇️ EVAL ⌘ cmd.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>


1. **How to change a single property in a $holder?**
  
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    
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

    With a mix of dictionary values and [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) surrounded with `:`.
    
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # $partB: {B:2}
    - EVAL >> $partB:
        B: 2

    # $partC: {C:3}
    - EVAL >> $partC:
        C: 3

    # $output: {A:1, B:2, C:3, D:4}
    - EVAL >> $output:
        A: 1
        :{$partB}:
        :{$partC}:
        D: 4
    ```
    
    In the example above, `$output` has `{A:1,B:2,C:3,D:4}`.


    ---
    <br/>
