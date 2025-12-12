# 😃⤴️ Talker `RETURN` command 

> Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

<br/>


1. **What's a RETURN command?**

    A `RETURN` ⤴️
    * is a flow [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that leaves a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) to its parent, 
    * and returns one of the following expressions.
    
    |Expression|Examples
    |-|-
    |`<string>`| `3` `Alice`
    [`{Function}`](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | `{$holder}` `{handler(1)}` `{.helper(1)}` 

    ---
    <br/>


1. **What's the RETURN syntax?**

    > This follows the [`.Evaluate`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Evaluate ⓕ.md>) syntax.

    ```yaml
    # On-line syntax
    - RETURN {expression}

    # Multi-line syntax
    - RETURN:
        {object}
    ```

    | Input| Purpose | Example
    |-|-|-
    | `{expression}`| String or [{Function}](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) to be evaluated | `A` `{f}` `{$p}`
    || Supports missing `{}` in functions | `f()` `$p`
    | `{object}` | Any object  | `{A:1,B:2}` 
    || or `{expression}` | `A` `f()` `$p`
    
    ---
    <br/>



1. **What happens after a RETURN?**

    Nothing runs on a [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) after the `RETURN`.

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ✅ No failure occurred.
    |
    
    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    📃 Example:
    - RUN: Test 
    - DONE: No failure occurred.
    
    📃 Test:
    - RETURN
    - FAIL: This command never runs.
    ```

    Uses: [`FAIL`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>) [`RUN`](<../RUN 🏃/🏃 RUN ⌘ cmd.md>) [`DONE`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
    
    ---
    <br/>


1. **How to read the result from a RETURN?**



    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ String return `Bla Bla`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Holder return `123`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) | ℹ️ Function return 1+2+3= `6`
    |

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    💬 Example:

    # Run without arguments
    - RUN: StringProc >> $x
    - INFO: String return `{$x}`
    
    # Run with 123
    - RUN: PlaceholderProc(123) >> $x
    - INFO: Holder return `{$x}`
    
    # Run with 1,2,3
    - RUN: FunctionProc(1,2,3) >> $x
    - INFO: Function return 1+2+3= {$x}
    ```

    ```yaml
    📃 StringProc:
    - RETURN Bla Bla
    ```

    ```yaml
    📃 PlaceholderProc:
    - RETURN $1
    ```

    ```yaml
    📃 FunctionProc:
    - RETURN .Add($1, $2, $3)
    ```

    Uses: [`.Add`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>) [`INFO`](<../../../📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`RUN`](<../RUN 🏃/🏃 RUN ⌘ cmd.md>) 

    ---
    <br/>

