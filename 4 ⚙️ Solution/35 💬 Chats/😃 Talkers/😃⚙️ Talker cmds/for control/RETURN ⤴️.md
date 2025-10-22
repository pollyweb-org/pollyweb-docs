# 😃⤴️ Talker `RETURN` flow 

> Part of [Talker 😃](<../../😃 Talker.md>)

<br/>


1. **What's a RETURN flow?**

    A `RETURN` ⤴️
    * is a flow [Command ⌘](<⌘ Command.md>) 
    * that leaves a [Script 📃](<📃 Script.md>) to its parent, 
    * and returns one of the following expressions.
    
    |Expression|Examples
    |-|-
    |`<string>`| `3` `Alice`
    [`{Function}`](<../for data/{Function} 🐍.md>) | `{$placeholder}` `{handler(1)}` `{.helper(1)}` 

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

    | Argument| Purpose | Example
    |-|-|-
    | `{expression}`| String or [{Function}](<../for data/{Function} 🐍.md>) to be evaluated | `A` `{f}` `{$p}`
    || Supports missing `{}` in functions | `f()` `$p`
    | `{object}` | Any object  | `{A:1,B:2}` 
    || or `{expression}` | `A` `f()` `$p`
    
    ---
    <br/>



1. **What happens after a RETURN?**

    Nothing runs on a [Script 📃](<📃 Script.md>) after the `RETURN`.

    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ✅ No failure occurred.
    |
    
    Here's the [Script 📃](<📃 Script.md>).

    ```yaml
    📃 Example:
    - RUN|Test 
    - SUCCESS|No failure occurred.
    
    📃 Test:
    - RETURN
    - FAILURE|This command never runs.
    ```

    Commands: [`FAILURE`](<../../../🤔 Prompts/🤔📢 Prompt status/FAILURE ❌ prompt.md>) [`RUN`](<RUN ▶️.md>) [`SUCCESS`](<../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅ prompt.md>)
    
    ---
    <br/>


1. **How to read the result from a RETURN?**



    | [Domain](<../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ String return `Bla Bla`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Placeholder return `123`
    | [🤗 Host](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Function return 1+2+3= `6`
    |

    Here's the [Script 📃](<📃 Script.md>).

    ```yaml
    # 😃 Talker 

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
    StringProc:
    - RETURN|Bla Bla
    ```

    ```yaml
    PlaceholderProc:
    - RETURN|!1
    ```

    ```yaml
    FunctionProc:
    - RETURN|.Sum([!1,!2,!3])
    ```

    Commands: [`INFO`](<../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️ prompt.md>) [`RUN`](<RUN ▶️.md>) [`{.Sum}`](<{Function} 🐍.md>)

    ---
    <br/>

