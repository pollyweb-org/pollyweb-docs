# 🤔 Prompts with `Details`

> Part of [Prompts 🤔](<01 🤔 Prompt.md>)

<br/>

1. **What are expandable details?**

    Expandible details
    * are additional notes of any [Prompt 🤔](<01 🤔 Prompt.md>)
    * rendered in Markdown format by [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    * that are initially collapsed to users.

    ---
    <br/>

1. **What are example use cases?**
   
    * [Finder 🔎 vault](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>)
    * [Book restaurant table online 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
  
    ---
    <br/>



1. **What's the format for a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    <PROMPT>|<message>:
        Details: <details>
    ```

    
    | Argument| Purpose | Example
    |-|-|-
    | `<PROMPT>` | A [Prompt 🤔](<01 🤔 Prompt.md>) format. | `INFO` `TEMP`
    | `<message>` |  Message to show to the user. | `Hi!`
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

1. **What's an example in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**
   
    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Expandable info [+] | > +
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Expandable info [-]<br/>&nbsp;&nbsp;&nbsp;1. Markdown bullet one  <br/>&nbsp;&nbsp;&nbsp;2. Markdown bullet two
    |

    The corresponding [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) would be.
    
    ```yaml
    INFO|Expandable info:
        Details: |
            1. Markdown bullet one
            1. Markdown bullet two
    ```

    

    ---
    <br/>


1. **What's the response in the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: <PROMPT>
    Message: <message>
    Details: <details>
    ```

    ---
    <br/>