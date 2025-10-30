# 🪧 Prompt Text

> Part of [Prompts 🤔](<../🤔 Prompt.md>)

<br/>

1. **What are Prompt texts?**

    [Prompt 🤔](<../🤔 Prompt.md>) texts are the main message sent in a [Chat 💬](<../../Chats 💬/💬 Chat.md>).

    ---
    <br/>

1. **What's an example of a Prompt text?**
   
    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ This is the text
    |

    Here's the [Script 📃](<../../Scripts 📃/📃 basics/Script 📃.md>).
    
    ```yaml
    - INFO|This is the text
    ```

    ---
    <br/>

1. **What is supported in Prompt texts?**

    |Support | Details | Examples
    |-|-|-
    | Strings | Static text | `ABC` `123` `Any text`
    | [Holders 🧠](<../../Scripts 📃/📃 basics/Holder 🧠.md>) | Stored values | `$p` `$.Msg`
    | [Functions 🐍](<../../Scripts 📃/📃 basics/Function 🐍.md>) | Calculations | `f()` `f(*)` `{f}` `{f()}`
    | Interpolations   | Mixed text | `See {$p} and {f}.`

    ---
    <br/>


1. **What are the syntaxes supported for evaluation?**
   
    |Type| Scope | Evaluated ✅ | Text ❌
    |-|-|-|-
    | [Holders 🧠](<../../Scripts 📃/📃 basics/Holder 🧠.md>) | Custom |`$p` `{$p}`| `p` `$p *`
    | | Internal  |`$.Msg` `$.p` `{$.p}`| `.p` `$.p *`
    | [Functions 🐍](<../../Scripts 📃/📃 basics/Function 🐍.md>) | Custom |`f()` `f(*)` `{f}` | `f` `f() *`
    | | Internal |`.f()` `.f(*)` `{.f}` | `.f` `.f() *`
    | Interpolations | -  | `{$p} & {f}` | `$p & f()`

    ---
    <br/>