# ↩️ Talker `RETURN` flow 

> Part of [Talker 😃](<../10 😃 Talker.md>)

<br/>


1. **What's a RETURN flow?**

    A `RETURN` ↩️
    * is a flow [Command ⌘](<10 ⌘ Command.md>) 
    * that leaves a [Procedure ⚙️](<11 ⚙️ Procedure.md>) to its parent, 
    * and returns one of the following expressions.
    
    |Expression|Examples
    |-|-
    |`<string>`| `3` `Alice`
    [`{Function}`](<../😃🗃️ Talker data/12 🐍 {Function}.md>) | `{$placeholder}` `{handler(1)}` `{.helper(1)}` 

    ---
    <br/>





1. **What's the RETURN syntax?**

    ```yaml
    - RETURN|{expression}
    ```

    | Argument| Purpose
    |-|-
    | `{expression}`| Optional string or [{Function}](<../😃🗃️ Talker data/12 🐍 {Function}.md>) to be evaluated.
    
    ---
    <br/>



1. **What happens after a RETURN?**

    Nothing runs on a [Procedure ⚙️](<11 ⚙️ Procedure.md>) after the `RETURN`.

    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | ✅ No failure occurred.
    |
    
    Here's the [Talker 😃](<../10 😃 Talker.md>).

    ```yaml
    # 😃 Talker 

    💬 Example:
    - RUN|Test 
    - SUCCESS|No failure occurred.
    
    Test:
    - RETURN
    - FAILURE|This command never runs.
    ```

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | ▶️ [RUN](<24 ▶️ RUN flow.md>) | To run the procedures.
    
    ---
    <br/>


1. **How to read the result from a RETURN?**



    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | ℹ️ String return `Bla Bla`
    | [🤗 Host](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | ℹ️ Placeholder return `123`
    | [🤗 Host](<../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🎭 Host role.md>) | ℹ️ Function return 1+2+3= `6`
    |

    Here's the [Talker 😃](<../10 😃 Talker.md>).

    ```yaml
    # 😃 Talker 

    💬 Example:
    - RUN|StringProc >> $x
    - INFO|String return `{$x}`
    - RUN|PlaceholderProc(123) >> $x
    - INFO|Placeholder return `{$x}`
    - RUN|FunctionProc(1,2,3) >> $x
    - INFO|Function return 1+2+3= {$x}

    StringProc:
    - RETURN|Bla Bla

    PlaceholderProc:
    - RETURN|{$1}

    FunctionProc:
    - RETURN|{.Sum($1,$2,$3)}
    ```

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | ▶️ [RUN](<24 ▶️ RUN flow.md>) | To run the procedures.

    ---
    <br/>

