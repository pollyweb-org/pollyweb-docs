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
    QUANTITY|<message> >> $placeholder:
        MinValue: <min-value>
        MaxValue: <max-value>
    ```
    
    ---
    <br/>



1. **What's an example?**

    Consider the following [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    QUANTITY|How many? >> $qt
    ```
    
    The corresponding [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) would be.

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How many? | 🔄 123
    [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 🫥 How many? | 🔄 123
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 🫥 How many? | 🔄 -54

    ---
    <br/>


1. **How to default quantities in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Table reservation.
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 For how many? [1, 2, more] | > more
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 😃 How many exactly? | 🔄 8
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ⏳ Checking availability... 
    |

    The corresponding [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>) is as follows.

    ```yaml
    💬 Walk-in:
    - INFO|Table reservation.
    - ONE|For how many?|1,2,more >> $qt
    - CASE|$qt:
        more: 
          - QUANTITY|How many exactly? >> $qt:
                MinValue: 3
                MaxValue: 12
    - TEMP|Checking availability...
    ```

    ---
    <br/>
