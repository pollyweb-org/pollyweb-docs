# 🔄 QUANTITY prompt

> Part of [blocking input prompts 🤔](<11 ✏️ Input behavior.md>)


<br/>

1. **What's an QUANTITY prompt?**

    It's a [Prompt 🤔](<01 🤔 Prompt.md>) that shows up and down arrows - e.g.:
    * [Book a restaurant table online 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    * [Split the bill at a restaurant ✂️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/74 💳 Pay: Split bill ✂️.md>)
    * [Walk into a full restaurant 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/44 🚪 Door: Walk in full.md>)

    ---
    <br/>


1. **What features does QUANTITY implement?**

    | Feature | Details
    |-|-
    | [`Details`](<03 🤔⊕ with Details.md>) | Has expandable [+] details.
    | [`Attachment`](<05 🤔📎 with Attachments.md>) | Has a PDF, PNG, or JPEG attachment.
    | [`Input` behavior](<11 ✏️ Input behavior.md>) | Waits for an answer from users.
    
    ---
    <br/>

1. **What's the syntax on a [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    # Simplest.
    QUANTITY|<message> 
    ```

    ```yaml
    # Comprehensive.
    QUANTITY >> $placeholder:
        Message: <message>
        MinValue: <min-value>
        MaxValue: <max-value>
    ```

    | Argument| Purpose | Example
    |-|-|-
    | `<message>`| Message to show to the user
    | `$placeholder`| Placeholder with the user's answer
    | `<min-value>` | Optional minimum value | `1`
    | `<max-value>` | Optional maximum value | `5`
    
    
    ---
    <br/>



1. **What's an example?**

    Here's a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>).

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How many? | 🔄 123
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 How many? | 🔄 123
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 How many? | 🔄 -54
    |
    
    <br/>

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    # 😃 Talker 
    - QUANTITY >> $qt:
        Message: How many? 
        MinValue: -100
        MaxValue: 100
    ```

    <br/>

    Here's the [`Prompted@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>).

    ```yaml
    Format: QUANTITY
    Message: 😃 How many?
    MinValue: -100
    MaxValue: 100
    ```

    <br/>
    
    Here's the answer in [`Reply@Host`](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>).

    ```yaml
    Answer: -54
    ```

    ---
    <br/>


1. **How to default quantities in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    Use the [`ONE`](<55 1️⃣ ONE prompt.md>) prompt.

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Table reservation.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 For how many? [1, 2, more] | > more
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How many exactly? | 🔄 8
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ⏳ Checking availability... 
    |

    Here's the [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).

    ```yaml
    # 😃 Talker 

    💬 Walk-in:
    
    - INFO:
        Message: Table reservation.
    
    - ONE >> $qt:
        Message: For how many?
        Options: 1,2,more

    - CASE|{$qt}:
        more: 
          - QUANTITY|How many exactly? >> $qt:
                MinValue: 3
                MaxValue: 12

    - TEMP|Checking availability...
    ```

    | [Command ⌘](<../33 😃 Talkers/10 ⌘ Command.md>) | Purpose
    |-|-
    | ℹ️ [`INFO`](<21 ℹ️ INFO prompt.md>) | To show the result.
    | 1️⃣ [`ONE`](<55 1️⃣ ONE prompt.md>) | To show the options.
    | 🔀 [`CASE`](<../33 😃 Talkers/22 🔀 CASE flow.md>) | To check the selected option.
    | ⏳ [`TEMP`](<22 ⏳ TEMP prompt.md>) | To show work in progress.
    

    ---
    <br/>
