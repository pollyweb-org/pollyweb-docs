# 💼 Talker SHARE command

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What is a SHARE message command?**

    A `SHARE`
    * is a message [Command](<10 Command.md>) 
    * that asks for user data in [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>)
    * triggering the following flows:
      * [🧑‍🦰👉💼 Share Bind @ Wallet](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind.md>)
      * [🧑‍🦰👉💼 Share Token @ Wallet](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token.md>)
      * [🧑‍🦰👉💼 Share Token+ID @ Wallet](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/05 🧑‍🦰👉💼 Share Token+ID.md>)

    ---
    <br/>


3. **What's the SHARE syntax?**

    ```yaml
    # Inline, single code
    SHARE|<code> >> <shared>

    # Multi-line, multiple codes
    SHARE >> <shared>:
        - <code-1>
        - <code-n>
    ```

   
    | Argument| Purpose
    |-|-
    | `<code>`  | 
    | `<shared>`| 


    ---
    <br/>

4. **What does a Chat look like?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 💼 [Consumer](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | ℹ️ Tell me your name.
    | 🧢 [Persona](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share social name? [No] <br/> - [ Personal ] 🧑‍🦰 <br/> - [ Work ] 💼       | > Personal
    | 💼 [Consumer](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | ℹ️ Hi, Alice!


    ```yaml
    INFO|Tell me your name.
    SHARE >> name
        - nlweb.org/PERSONA/NAME/SOCIAL
    ```

    ---
    <br/>