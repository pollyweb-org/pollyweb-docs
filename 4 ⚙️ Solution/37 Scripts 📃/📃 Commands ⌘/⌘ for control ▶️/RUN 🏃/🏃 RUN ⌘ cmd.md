# 😃🏃 Talker `RUN` flow 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

## FAQ


1. **What's a RUN flow?**

    A `RUN` 🏃
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that runs a  [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ---
    <br/>

1. **What's the RUN syntax?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    |Syntax | Behavior
    |-|-
    |`RUN\|script` | Runs the `script` [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
    |`RUN: script` | Equals `RUN\|script`
    |`RUN\|$holder` | Runs the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) named by the [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    |`RUN\|script: *` | Runs `script` with [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>)(`*`) inputs
    |`RUN\|script(*)` | Same as `RUN\|script: *`
    |`RUN\|s1(*),s2(*)` | Runs the `s1` and `s2` [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) in sequence
    |`RUN: s1(*),s2(*)` | Equals `RUN\|s1(*),s2(*)`
    |`RUN\|script >> $out` | Puts the [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) in the `$out` [Holder 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)
    |`RUN\|script >> $out: *` | Runs `script` with `*` args into `$out` 
    |`RUN\|script(*) >> $out` | Same as `RUN\|script >> $out: *`
    
    ---
    <br/>

1. **What do the inputs mean?**

    | Input| Purpose | Example
    |-|-| -
    | `script`| [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to execute | `MyScript`
    | `$out`| Optional [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) holder | `$return`
    | `*`  | Optional inputs to [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) | `1,2` `A,$B` `{A:1,$B}`
    |           | Read `$n`  inside the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | `$1` `$2`
    | | Read `$name` in the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | `$B`|
    | | Read with [`{.Inputs}`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>) | `.Inputs.B` `$.Inputs.B`
    
    ---
    <br/>

1. **What's an example with static arguments?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ [Hi, Alice! I'm happy.](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ [Hi David! I'm glad.](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ [Example finished.](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
    |

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # 1st call
    - RUN Great:
        Name: Alice
        Felling: happy

    # 2nd call
    - RUN Great:
        Name: David
        Felling: glad

    - DONE: Example finished.
    ```

    ```yaml
    📃 Great:
    - INFO: Hi, {$Name}! I'm {$Feeling}.
    ```

    Uses: [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`RUN`](<🏃 RUN ⌘ cmd.md>) [`DONE`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)

    ---
    <br/>

1. **What's an example with holder arguments?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Give me a number. | ↕️ 12
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ You gave me number 12.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | 😃 Give me another. | ↕️ 34
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ You gave me number 34.
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Example finished.
    |
    
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    
    ```yaml
    📃 Example:
    
    # Get a number
    - QUANTITY Give me a number. >> $n1

    # Show the number
    - RUN ShowNumber:
        n: $n1

    # Get another number
    - QUANTITY Give me another. >> $n2

    # Show the second number
    - RUN ShowNumber:
        n: $n2

    - DONE: Example finished.
    ```

    ```yaml
    📃 ShowNumber:
    - INFO: You gave me number {$n}.
    ```

    Uses: [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`QUANTITY`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/QUANTITY ↕️/↕️ QUANTITY ⌘ cmd.md>) [`RUN`](<🏃 RUN ⌘ cmd.md>) [`DONE`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)


    ---
    <br/>



1. **What's an example with function arguments?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) |  ℹ️ [Here's number  3512596.](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) |  ℹ️ [Here's number  52364.](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>)
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ Example finished.
    |

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # Get the 1st random number
    - RUN ShowNumber: 
        n: {get-random-number}

    # Get the second random number
    - RUN ShowNumber:
        n: {get-random-number}

    # Finish the script
    - DONE: Example finished.
    ```

    ```yaml
    📃 ShowNumber:
    - INFO: Here's number {$n}.
    ```

    Uses: [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`DONE`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)

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



    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) |  ✅ Congrats, you won!
    |
    
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:

    # Calculate 
    - RUN Calculate >> result

    # Check the result
    - CASE {$result}:
        Won: DONE Congrats, you won!
        Lost: FAIL Sorry, you lost! 
    ```

    ```yaml
    📃 Calculate:

    # Exit with a result
    - RETURN: Won

    # It should't get to this line
    - FAIL: This is a bug.
    ```

    Uses: [`CASE`](<../CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`FAIL`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`DONE`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)



    ---
    <br/>
    


1. **What's an example with a calculated RETURN?**


    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) |  ℹ️ Adding 5 to 2...
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) |  ✅ [The first result is 7.](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) |  ℹ️ Adding 5 to 4...
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) |  ✅ [The second result is 9.](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
    |
    
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

    ```yaml
    📃 Example:

    # First calculation
    - RUN AddFive(2) >> n
    - DONE: The first result is {$n}.

    # Second calculation
    - RUN AddFive(3) >> n
    - DONE: The second result is {$n}.
    ```

    ```yaml
    📃 AddFive:

    # Calculate and exit the script
    - INFO: Adding 5 to {$1}...
    - RETURN: .Add($1, 5)

    # It shouldn't get to this line
    - FAIL: This is a bug.
    ```

    Uses: [`FAIL`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`RETURN`](<../RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`DONE`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)



    ---
    <br/>
    


1. **How to simplify argument names?**

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).
    
    ```yaml
    📃 Example:
    
    # Option 1, name the arguments
    - RUN Handler:
        Name: $Name
        City: $City

    # Option 2, just pass the holders
    - RUN Handler:
        $Name, $City

    # Option 3, pass holder properties 
    - RUN Handler:
        $user.Name
        $user.City
    ```

    ```yaml
    📃 Handler:
    - INFO:|Hi, {$Name}! How's {$City}?
    ```

    ---
    <br/>

1. **How does scope work?**

    [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) behavior is as follow:
    * they only exist in the context of a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>), 
    * unless passed to another [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) as a [`RUN`](<🏃 RUN ⌘ cmd.md>) parameter.

    Here's a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to exemplify it.

    ```yaml
    📃 Main:
    - PUT: 1 >> $a    # set $a:1
    - PUT: 2 >> $b    # set $b:2
    - RUN Sub($a)     # pass only $a
    ```

    ```yaml
    📃 Sub:
    - ASSERT:
        - $a.Is(1)    # $a exists with 1
        - $b.IsEmpty  # $b does not exist
    ```
    
    Uses: [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PUT`](<../../⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>)

    ---
    <br/>