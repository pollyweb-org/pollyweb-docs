# 🤔 Prompts with `Details`

> Part of [Prompts 🤔](<../../10 📘 Talker specs/2 🤔 Prompt.md>)

<br/>

1. **What are expandable details?**

    Expandible details
    * are additional notes of any [Prompt 🤔](<../../10 📘 Talker specs/2 🤔 Prompt.md>)
    * rendered in Markdown format by [Wallet 🧑‍🦰 apps](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    * that are initially collapsed to users.

    ---
    <br/>

1. **What are example use cases?**
   
    * [Finder 🔎 vault](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>)
    * [Book restaurant table online 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
  
    ---
    <br/>



1. **What's the format for a [Talker 😃](<../../10 📘 Talker specs/1 😃 Talker.md>)?**

    ```yaml
    <PROMPT>|<statement>:
        Details: <details>
    ```

    
    | Argument| Purpose | Example
    |-|-|-
    | `<PROMPT>` | A [Prompt 🤔](<../../10 📘 Talker specs/2 🤔 Prompt.md>) format. | `INFO` `TEMP`
    | `<statement>` |  Message to show to the user. | `Hi!`
    | `<details>` |  Details to show to the user. | `Bla, bla.`
    
    
    
    ---
    <br/>


1. **How to defined details with multiple lines?**

    Use Markdown syntax.

    | Syntax | Details
    |-|-
    | `Details:` | Broken lines appear render as a single line.
    | `Details: \|` | Broken lines appear as multiple lines.
    | `Details: >` | Also renders  a single line, but with paragraphs.
    | `Details: >-` | Same as above, but removes the trailing newline.

    ---
    <br/>

1. **What's an example in a [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>)?**
   
    | [Domain](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../../10 📘 Talker specs/2 🤔 Prompt.md>) | [User](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Expandable info [+] | > +
    | [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Expandable info [-]<br/>&nbsp;&nbsp;&nbsp;1. Markdown bullet one  <br/>&nbsp;&nbsp;&nbsp;2. Markdown bullet two
    |

    Here's the [Talker 😃](<../../10 📘 Talker specs/1 😃 Talker.md>).
    
    ```yaml
    - INFO|Expandable info:
        Details: |
            1. Markdown bullet one
            1. Markdown bullet two
    ```

    | [Command ⌘](<../../30 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<../4 ⚠️ Status prompts/21 ℹ️ INFO prompt.md>) | To show the messages and details.
    

    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) response.

    ```yaml
    Format: INFO
    Statement: ℹ️ Expandable info
    Details: |
        1. Markdown bullet one
        1. Markdown bullet two
    ```

    ---
    <br/>