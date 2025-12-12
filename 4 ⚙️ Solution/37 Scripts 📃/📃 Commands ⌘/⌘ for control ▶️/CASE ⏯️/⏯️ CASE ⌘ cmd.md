# 😃⏯️️ Talker `CASE` flow 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<br/>


1. **What's a CASE flow?**

    A `CASE` ⏯️️
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  
    * that runs a matching [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) or [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)
    * based on the evaluation of a [{Function}](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>).

    ---
    <br/>

1. **What's the syntax?**

    ```yaml
    # Simplest
    - CASE {function}:
        <value>: <action>
    ```


    | Input| Purpose | Example
    |-|-|-
    | `{function}` | Optional [{Function}](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) to evaluate | `{f}` `{$p}`
    || Allows for missing `{}` in functions | `f()` `$p`
    || Defaults to the last [input prompt ✏️](<../../../../35 💬 Chats/Prompts 🤔/🤔⚙️ Prompt features/9 ✏️ as Input.md>) | `TEXT\|Id?`
    | `<value>`| [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) to be matched with | `ABC`
    | `<action>`| Run a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | `MyProc`
    || or a one-line [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>). | `INFO\|OK`
    
    <br/>

    ```yaml
    # One line values
    - CASE {function}:
        $: <action-$>
        <value-1>: <action-1>
        <value-n>: <action-n>
    ```

    | Input| Purpose
    |-|-
    | `$` | Catch-all clause if unmatched with any other value.
    
    <br/>

    ```yaml 
    # Multi-line values
    - CASE {function}:
        $: 
            - <cmd-$>
        <value-1>: 
            - <cmd-1>
            - <cmd-2>
        <value-n>: 
            - <cmd-n>
    ```

    | Input| Purpose
    |-|-
    | `<cmd-n>`| Run a multi-line [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) list.
    
    <br/>

    ```yaml 
    # Attributions
    - CASE $input >> $output:
        <when-1>: <then-1>
        <when-n>: <then-n>
    ```

    | Input| Purpose
    |-|-
    | `$input`  | Optional context to [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>)            | `1,2,3`
    | `<when>`  | Independent or contextualized [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) to match against     | `1`
    | `<then>`  | Resulting output if matched   | `one`
    | `$output` | Output [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)  | -

    ---
    <br/>

1. **What's an example with function logic?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Hi, premium customer!
    |

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    # 😃 Talker

    💬 Example:
    - CASE {customer-type}:
        STANDARD: ShowStandardOptions
        ADVANCED: ShowAdvancedOptions
        PREMIUM: ShowPremiumOptions

    ShowPremiumOptions:
    - INFO: Hi, premium customer!
    ```


    ```python
    # 🐍 Python handler
    def talkerHandler(args):
      match args['Function']:
        case 'customer-type':
          return context.CustomerType
    ```

    ---
    <br/>

1. **What's an example with inputs?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 [Select an option.](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/1️⃣ ONE ⌘ cmd.md>) <br/> - [ A ] <br/> - [ B ] <br/> - [ C ] | > B
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ You selected option B.
    |

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
   
    ```yaml
    # 😃 Talker

    💬 Example:

    - ONE >> $x:
        Text: Select an option.
        Options: A,B,C 

    - CASE: # Default to last input.
        B: INFO You selected option B.
        $: WhenUnmatched

    WhenUnmatched:
    - INFO: You selected option {$x}.
    ```
    Uses: [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>

1. **What's an example of an attribution?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Number from 1 to 3? | `3`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ You said `three`
    |

    <br/>

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

    ```yaml 
    📃 Example: 

    # Collect a number
    - DIGITS Number from 1 to 3? >> $input

    # Translate the number
    - CASE $input >> $output:
        1: one
        2: two
        3: three

    # Show the translation 
    - INFO: You said `{$output}`
    ```    
    Uses: [`DIGITS`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/DIGITS 🔢/🔢 DIGITS ⌘ cmd.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)

    ---
    <br/>


1. **Can CASE replace an IF chain for a holder?**

    Yes, a [`CASE`](<⏯️ CASE ⌘ cmd.md>) flow can replace multiple [`IF`](<../IF ⤵️/⤵️ IF ⌘ cmd.md>) flows when:
    * you have multiple conditions to check over a command [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    * each condition results in a different action

    Consider the following [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) using [`IF`](<../IF ⤵️/⤵️ IF ⌘ cmd.md>) and [`PUT`](<../../⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>).

    ```yaml
    📃 Using multiple IFs:
    - IF $holder.Is(0):
        PUT ZERO >> $result
    - IF $holder.IsAbove(0):
        PUT POSITIVE >> $result
    - IF $holder.IsBelow(0):
        PUT NEGATIVE >> $result
    ```

    `CASE` makes the script more readable and easier to maintain.

    ```yaml
    📃 Using CASE with a common holder:
    - CASE $holder >> $result:
        .Is(0): ZERO
        .IsAbove(0): POSITIVE
        .IsBelow(0): NEGATIVE
    ```

    ---
    <br/>

1. **Can CASE replace an IF chain without a common base value?**

    Yes, a [`CASE`](<⏯️ CASE ⌘ cmd.md>) flow can replace multiple [`IF`](<../IF ⤵️/⤵️ IF ⌘ cmd.md>) flows even without a common base value by using functions in the `when` clauses.
    
    Consider the following [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) using [`IF`](<../IF ⤵️/⤵️ IF ⌘ cmd.md>) and [`PUT`](<../../⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>).

    ```yaml
    📃 Using multiple IFs:
    - IF $A.Is(0):
        PUT ZERO >> $result
    - IF $B.IsAbove(0):
        PUT POSITIVE >> $result
    - IF $C.IsBelow(0):
        PUT NEGATIVE >> $result
    ```

    `CASE` makes the script more readable and easier to maintain.
    
    ```yaml
    📃 Using CASE:
    - CASE >> $result:
        A.Is(0): ZERO
        B.IsAbove(0): POSITIVE
        C.IsBelow(0): NEGATIVE
    ```

    ---
    <br/>