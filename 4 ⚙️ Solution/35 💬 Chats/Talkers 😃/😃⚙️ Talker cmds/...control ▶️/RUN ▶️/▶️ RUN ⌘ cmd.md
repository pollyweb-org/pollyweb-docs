# 😃▶️ Talker `RUN` flow 

> Part of [Talker 😃](<../../../😃 Talker role.md>)

<br/>


1. **What's a RUN flow?**

    A `RUN` ▶️
    * is a flow [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) 
    * that runs a  [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>).

    ---
    <br/>

1. **What's the RUN syntax?**

    ```yaml
    # Simplest in-line
    - RUN|<script>

    # Simplest multi-line
    - RUN:
        <script>

    # In batch
    - RUN:
        - <script-1>
        - <script-n>

    # Comprehensive in line args
    - RUN|<script>($arg-1, $arg-n) >> $return

    # Comprehensive appended args
    - RUN|<script> >> $return:
        {args}
    ```

    | Input| Purpose | Example
    |-|-| -
    | `<script>`| [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) to run | `MyScript`
    | `$arg-n`  | Optional positional arguments | `1,2` `s,$p`
    |           | Reads `$:n`  inside the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) | `$:1` `$:2`
    | `{args}`| Optional object arguments | `{A:1, B:2}`
    | | Reads `!name` in the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) | `$:A` `$:B`|
    | | Also reads with [`{.Inputs}`](<../../...holders 🧠/$.Inputs ▶️/▶️ $.Inputs 🧠 holder.md>) | `.Inputs.A`
    | `$return`| Optional [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) holder | `$return`
    
    ---
    <br/>

1. **What's an example with static arguments?**


    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ [Hi, Alice! I'm happy.](<../../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ [Hi David! I'm glad.](<../../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ [Example finished.](<../../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)
    |

    Here's the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    📃 Example:

    # 1st call
    - RUN|Great:
        Name: Alice
        Felling: happy

    # 2nd call
    - RUN|Great:
        Name: David
        Felling: glad

    - SUCCESS|Example finished.
    ```

    ```yaml
    📃 Great:
    - INFO|Hi, {$:Name}! I'm {$:Feeling}.
    ```

    Commands: [`INFO`](<../../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`RUN`](<▶️ RUN ⌘ cmd.md>) [`SUCCESS`](<../../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ---
    <br/>

1. **What's an example with holder arguments?**


    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Give me a number. | ↕️ 12
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ You gave me number 12.
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | 😃 Give me another. | ↕️ 34
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ You gave me number 34.
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ Example finished.
    |
    
    Here's the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>).
    
    ```yaml
    📃 Example:
    
    # Get a number
    - QUANTITY|Give me a number. >> $n1

    # Show the number
    - RUN|ShowNumber:
        n: $n1

    # Get another number
    - QUANTITY|Give me another. >> $n2

    # Show the second number
    - RUN|ShowNumber:
        n: $n2

    - SUCCESS|Example finished.
    ```

    ```yaml
    📃 ShowNumber:
    - INFO|You gave me number {$:n}.
    ```

    Commands: [`INFO`](<../../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`QUANTITY`](<../../../../Prompts 🤔/🤔✏️ Prompt inputs/QUANTITY ↕️/QUANTITY ↕️ prompt.md>) [`RUN`](<▶️ RUN ⌘ cmd.md>) [`SUCCESS`](<../../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)


    ---
    <br/>



1. **What's an example with function arguments?**


    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) |  ℹ️ [Here's number  3512596.](<../../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) |  ℹ️ [Here's number  52364.](<../../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>)
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ Example finished.
    |

    Here's the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    📃 Example:

    # Get the 1st random number
    - RUN|ShowNumber: 
        n: {get-random-number}

    # Get the second random number
    - RUN|ShowNumber:
        n: {get-random-number}

    # Finish the script
    - SUCCESS|Example finished.
    ```

    ```yaml
    📃 ShowNumber:
    - INFO|Here's number {$:n}.
    ```

    Commands: [`ASSERT`](<../../...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`INFO`](<../../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`SUCCESS`](<../../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)

    ```python
    # 🐍 Python handler
    def talkerHandler(args):
        match args['Function']:
            case 'get-random-number':
                return randomNumber()
    ```    

    ---
    <br/>
    

1. **What's an example with a static RETURN?**



    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) |  ✅ Congrats, you won!
    |
    
    Here's the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    📃 Example:

    # Calculate 
    - RUN|Calculate >> result

    # Check the result
    - CASE|{$result}
        Won: SUCCESS|Congrats, you won!
        Lost: FAILURE|Sorry, you lost! 
    ```

    ```yaml
    📃 Calculate:

    # Exit with a result
    - RETURN|Won

    # It should't get to this line
    - FAILURE|This is a bug.
    ```

    Commands: [`CASE`](<../CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`FAILURE`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SUCCESS`](<../../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)



    ---
    <br/>
    


1. **What's an example with a calculated RETURN?**


    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../Prompts 🤔/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) |  ℹ️ Adding 5 to 2...
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) |  ✅ [The first result is 7.](<../../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) |  ℹ️ Adding 5 to 4...
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) |  ✅ [The second result is 9.](<../../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)
    |
    
    Here's the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>)

    ```yaml
    📃 Example:

    # First calculation
    - RUN|AddFive(2) >> n
    - SUCCESS|The first result is {$n}.

    # Second calculation
    - RUN|AddFive(3) >> n
    - SUCCESS|The second result is {$n}.
    ````

    ```yaml
    📃 AddFive:

    # Calculate and exit the script
    - INFO|Adding 5 to {$:1}...
    - RETURN|.Add($:1, 5)

    # It shouldn't get to this line
    - FAILURE|This is a bug.
    ```

    Commands: [`FAILURE`](<../../../../Prompts 🤔/🤔📢 Prompt status/FAILURE ❌/FAILURE ❌ prompt.md>) [`INFO`](<../../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SUCCESS`](<../../../../Prompts 🤔/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)



    ---
    <br/>
    

1. **What happens when setting values into input args?**

    > Used in the [`SAVE` 📃 script](<../../...datasets 🪣/SAVE 💾/💾 SAVE 📃 script.md>)

    It depends if the current value of the input contains the name of a [Holder 🧠](<../../...holders 🧠/$Holder 🧠.md>).

    |Scenario | Result 
    |-|-
    | [Holders 🧠](<../../...holders 🧠/$Holder 🧠.md>) | Fills the [Holder 🧠](<../../...holders 🧠/$Holder 🧠.md>) 
    | Anything else | Throws an error
    |

    Here's a [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>).
    ```yaml
    📃 Example:

    # This will work
    - RUN|ShowValue:
        Holder: p
    
    # Shows "The value of $p is 123"
    - INFO|The value of $p is {$p}

    # This will throw an error
    - RUN|ShowValue:
        Holder:
        
    # Never reached
    - FAILURE|This line is never reached
    ```
    Commands: [`INFO`](<../../../../Prompts 🤔/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`FAILURE`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) 

    ```yaml
    📃 SetValue:
    
    # Only works with a holder name
    - EVAL|123 >> $:Holder
    ```
    Commands: [`EVAL`](<../../...holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>)
    
    ---
    <br/>