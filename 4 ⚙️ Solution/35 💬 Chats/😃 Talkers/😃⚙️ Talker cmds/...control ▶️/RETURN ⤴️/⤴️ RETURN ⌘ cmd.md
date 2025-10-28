# 😃⤴️ Talker `RETURN` command 

> Part of [Talker 😃](<../../../😃 Talker role.md>)

<br/>


1. **What's a RETURN command?**

    A `RETURN` ⤴️
    * is a flow [Command ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) 
    * that leaves a [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) to its parent, 
    * and returns one of the following expressions.
    
    |Expression|Examples
    |-|-
    |`<string>`| `3` `Alice`
    [`{Function}`](<../../...functions 🐍/{Function} 🐍.md>) | `{$placeholder}` `{handler(1)}` `{.helper(1)}` 

    ---
    <br/>





1. **What's the RETURN syntax?**

    ```yaml
    # On-line syntax
    - RETURN|{expression}

    # Multi-line syntax
    - RETURN:
        {object}
    ```

    | Input| Purpose | Example
    |-|-|-
    | `{expression}`| String or [{Function}](<../../...functions 🐍/{Function} 🐍.md>) to be evaluated | `A` `{f}` `{$p}`
    || Supports missing `{}` in functions | `f()` `$p`
    | `{object}` | Any object  | `{A:1,B:2}` 
    || or `{expression}` | `A` `f()` `$p`
    
    ---
    <br/>



1. **What happens after a RETURN?**

    Nothing runs on a [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) after the `RETURN`.

    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ No failure occurred.
    |
    
    Here's the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    📃 Example:
    - RUN|Test 
    - SUCCESS|No failure occurred.
    
    📃 Test:
    - RETURN
    - FAILURE|This command never runs.
    ```

    Commands: [`FAILURE`](<../../../../🤔 Prompts/🤔📢 Prompt status/FAILURE ❌/FAILURE ❌ prompt.md>) [`RUN`](<../RUN ▶️/▶️ RUN ⌘ cmd.md>) [`SUCCESS`](<../../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)
    
    ---
    <br/>


1. **How to read the result from a RETURN?**



    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ String return `Bla Bla`
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Placeholder return `123`
    | [🤗 Host](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Function return 1+2+3= `6`
    |

    Here's the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>).

    ```yaml
    💬 Example:

    # Run without arguments
    - RUN|StringProc >> $x
    - INFO|String return `{$x}`
    
    # Run with 123
    - RUN|PlaceholderProc(123) >> $x
    - INFO|Placeholder return `{$x}`
    
    # Run with 1,2,3
    - RUN|FunctionProc(1,2,3) >> $x
    - INFO|Function return 1+2+3= {$x}
    ```

    ```yaml
    📃 StringProc:
    - RETURN|Bla Bla
    ```

    ```yaml
    📃 PlaceholderProc:
    - RETURN|$:1
    ```

    ```yaml
    📃 FunctionProc:
    - RETURN|.Add($:1, $:2, $:3)
    ```

    Commands: [`.Add`](<../../...functions 🐍/🔩 {.Add}.md>) [`INFO`](<../../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`RUN`](<../RUN ▶️/▶️ RUN ⌘ cmd.md>) 

    ---
    <br/>

