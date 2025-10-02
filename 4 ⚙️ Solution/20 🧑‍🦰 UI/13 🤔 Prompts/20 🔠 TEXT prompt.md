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

    Consider the following [Talker 😃](<../14 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    TEXT|How are you today? >> msg
    ```

    | Service | Prompt | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | 💬 How are you today? | `I'm fine`
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | 💬 How are you today? | `I'm fine`
    | [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | 💭 How are you today? | `I'm fine`
   

    ---
    <br/>

2. **What are business cases?**

    |Category|Use case
    |-|-
    |

    ---
    <br/>


3. **What's the content for a [Talker 😃](<../14 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    
    ```

    |Parameter|Details
    |-|-
    | 
    
    ---
    <br/>


4. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    
    ```

    ---
    <br/>

5. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    
    ```