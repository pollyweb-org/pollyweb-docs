# 🔠 TEXT prompt

> Part of [blocking input prompts 🤔](<03 Blocking input prompts.md>)

<br/>

1. **What's a `TEXT` prompt?**

    This is a blocking input [Prompt 🤔](<01 🤔 Prompt.md>) that allows the user to type something instead of having to follow a structured format;
    - it allows for large-language models (LLMs) to interpret the user's intent from natural language text, while also providing a structured input to facilitate the user's interaction;
    - e.g., a user may select the `Yes` option, or type `that's fine` in the textbox.

    ---
    <br/>

1. **How do emojis work?**

   |Emoji|Usage
   |-|-
   |💬| The speech emoji 💬 represent the chat's [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) and any [Helper 🛠️ domains](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) that it may [invite ⏩](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite.md>).
   |💭| The thought emoji 💭 represents user [Agent 🫥 vaults](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>).

    ---
    <br/>

1. **What's an example of a TEXT prompt?**

    Consider the following [Talker 😃](<../33 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    TEXT|How are you today? >> msg
    ```

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 💬 How are you today? | `I'm fine`
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 💬 How are you today? | `I'm fine`
    | [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 💭 How are you today? | `I'm fine`
   

    ---
    <br/>

1. **What agents implement text?**
   
    |Agent| Purpose
    |-|-
    |🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)| To search for the right agent for a job.
    🔎 [Finder](<../../../4 ⚙️ Solution/30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) | To search for a host of a service or place.
    🧭 [Navigator](<../../30 🫥 Agents/07 🧭 Navigators/01 🧭🫥 Navigator agent.md>) | To report on something suspicious.
    |[💖 Vitalogist](<../../../4 ⚙️ Solution/30 🫥 Agents/09 💖 Vitalogists/01 💖🫥 Vitalogist agent.md>)| To register food intake.

    ---
    <br/>
1. **What are business cases?**

    |Category|Use case
    |-|-
    |`Curator`| [Order a burger at a fast food 🍔](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/25 🍔 Fast food/21 🪑 Seat: Order burger 🍔.md>)
    |`Reviewer`| [Get details on a bad review ⭐](<../../../3 🤝 Use Cases/04 🛒 Shop/01 🛍️ Shop for clothes/01 Customer @ Item/01 Item price.md>)
    |`Broker`| [Delegate finding a bar 🍸](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>)
    |`Finder` | [Ask alternatives to navigate 🧭](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/11 🌐 Web: Find a bar.md>)
    |`Generic`|[Report an accident 🆘](<../../../3 🤝 Use Cases/08 🏛️ Public Services/01 🆘 Call emergency/1 @ Anywhere/10. Emergency.md>)

    ---
    <br/>



1. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: FAILURE
    Message: <message>
    Options: <options>
    ```

    ---
    <br/>

1. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    Answer: 
        Option: <selected-option> # if any
        Text: <typed-text>
    ```