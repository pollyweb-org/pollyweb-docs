# 🪧 Prompt Statement

> Part of [Prompts 🤔](<../🤔 Prompt.md>)

<br/>

1. **What are Prompt statements?**

    [Prompt 🤔](<../🤔 Prompt.md>) statements are the main message sent in a [Chat 💬](<../../💬 Chats/💬 Chat.md>).

    ---
    <br/>

1. **What's an example of a Prompt statement?**
   
    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ This is the statement
    |

    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker.md>).
    
    ```yaml
    - INFO|This is the statement
    ```

    ---
    <br/>

1. **What is supported in Prompt statements?**

    |Support | Details | Examples
    |-|-|-
    | Strings | Static text | `ABC` `123` `Any text`
    | [Placeholders 🧠](<../../😃 Talkers/😃⚙️ Talker cmds/for data/$Placeholder 🧠.md>) | Stored values | `$p` `$.Msg`
    | [Functions 🐍](<../../😃 Talkers/😃⚙️ Talker cmds/for data/{Function} 🐍.md>) | Calculations | `f()` `f(*)` `{f}` `{f()}`
    | Interpolations   | Mixed text | `See {$p} and {f}.`

    ---
    <br/>


1. **What are the syntaxes supported for evaluation?**
   
    |Type| Scope | Evaluated ✅ | Text ❌
    |-|-|-|-
    | [Placeholders 🧠](<../../😃 Talkers/😃⚙️ Talker cmds/for data/$Placeholder 🧠.md>) | Custom |`$p` `{$p}`| `p` `$p *`
    | | Internal  |`$.Msg` `$.p` `{$.p}`| `.p` `$.p *`
    | [Functions 🐍](<../../😃 Talkers/😃⚙️ Talker cmds/for data/{Function} 🐍.md>) | Custom |`f()` `f(*)` `{f}` | `f` `f() *`
    | | Internal |`.f()` `.f(*)` `{.f}` | `.f` `.f() *`
    | Interpolations | -  | `{$p} & {f}` | `$p & f()`

    ---
    <br/>