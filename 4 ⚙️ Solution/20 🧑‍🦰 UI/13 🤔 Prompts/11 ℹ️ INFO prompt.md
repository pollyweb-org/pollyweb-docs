# Non-blocking info ℹ️ ⓘ

> Part of [Non-blocking status prompts 🤔](<02 Non-blocking prompts.md>)

<br/>

1. **What is a non-blocking INFO?**

    This is an informative [Prompt 🤔](<01 🤔 Prompt.md>) that does not require the user input.

    ---
    <br/>

1. **How do INFO emojis work?**
   
    |Emoji | Details
    |-|-
    ℹ️ | The strong info emoji ℹ️ represents the chat's [Host 🤗 domain](<../12 💬 Chats/04 🤗🎭 Host role.md>) and any [Helper 🛠️ domains](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) that it may [invite ⏩](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite.md>).
    ⓘ | The faded info emoji ⓘ represents the user's [Agent 🫥 vaults](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>).

    ---
    <br/>



2. **What's an example in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    Consider the following [Talker 😃](<../14 😃 Talkers/01 😃 Talker.md>).
    
    ```yaml
    INFO|Simple info.
    ```

    | Domain | [Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ Simple info.
    | [🛠️ Helper](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>) | ℹ️ Simple info.
    | [🫥 Agent](<../24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>) | ⓘ Simple info.
    
    
    
    ---
    <br/>


3. **What's an example with non-blocking options in a [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>)?**

    ```yaml
    INFO|With options|[Cancel] later, [Play] music >> answer
    ```

    | Domain | [Prompt 🤔](<../13 🤔 Prompts/01 🤔 Prompt.md>) | User
    | - | - | - |
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | ℹ️ With options:<br/>- [ Cancel ] later <br>- [ Play ] music | > Cancel

    ---
    <br/>


4. **What's the format for a [Talker 😃](<../14 😃 Talkers/01 😃 Talker.md>)?**

    ```yaml
    INFO|<message>|<options> >> <key>
    ```
    
    ---
    <br/>


3. **What's the response in the [Prompted@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/04 🧑‍🦰🚀🤗 Prompted.md>) method?**

    ```yaml
    Format: INFO
    Message: <message>
    Options: <options>
    ```

    ---
    <br/>

4. **What's the Answer in the [Reply@Host](<../../../6 🅰️ APIs/50 🤗🅰️ Host/05 🧑‍🦰🐌🤗 Reply.md>) method?**

    ```yaml
    Answer: <selected-option> # if any
    ```

    ---
    <br/>