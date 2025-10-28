# 🤔 Prompts with `Details`

> Part of [Prompts 🤔](<../🤔 Prompt.md>)

<br/>

1. **What are expandable details?**

    Expandible details
    * are additional notes of any [Prompt 🤔](<../🤔 Prompt.md>)
    * rendered in Markdown format by [Wallet 🧑‍🦰 apps](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    * that are initially collapsed to users.

    ---
    <br/>

1. **What are example use cases?**
   
    * [Finder 🔎 vault](<../../../50 🫥 Agent domains/Finders 🔎/🔎🫥 Finder agent.md>)
    * [Book restaurant table online 🍽️](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
  
    ---
    <br/>



1. **What's the format for a [Talker 😃](<../../😃 Talkers/😃 Talker role.md>)?**

    ```yaml
    <PROMPT>|<statement>:
        Details: <details>
    ```

    
    | Input| Purpose | Example
    |-|-|-
    | `<PROMPT>` | A [Prompt 🤔](<../🤔 Prompt.md>) format. | `INFO` `TEMP`
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

1. **What's an example in a [Chat 💬](<../../💬 Chats/💬 Chat.md>)?**
   
    | [Domain](<../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Expandable info [+] | > +
    | [🤗 Host](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) | ℹ️ Expandable info [-]<br/>&nbsp;&nbsp;&nbsp;1. Markdown bullet one  <br/>&nbsp;&nbsp;&nbsp;2. Markdown bullet two
    |

    Here's the [Talker 😃](<../../😃 Talkers/😃 Talker role.md>).
    
    ```yaml
    - INFO|Expandable info:
        Details: |
            1. Markdown bullet one
            1. Markdown bullet two
    ```

    | [Command ⌘](<../../😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<../🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) | To show the messages and details.
    

    <br/>

    Here's the [`Prompted@Host`](<../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Prompted 🧑‍🦰🚀🤗/🤗 Prompted 🚀 request.md>) response.

    ```yaml
    Format: INFO
    Text: ℹ️ Expandable info
    Details: |
        1. Markdown bullet one
        1. Markdown bullet two
    ```

    ---
    <br/>