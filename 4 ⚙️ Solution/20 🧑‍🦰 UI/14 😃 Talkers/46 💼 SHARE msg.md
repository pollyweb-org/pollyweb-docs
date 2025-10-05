# 💼 Talker SHARE command

> Part of [Talker 😃](<01 😃 Talker.md>)

<br/>

1. **What is a SHARE message command?**

    A `SHARE`
    * is a message [Command ⌘](<10 ⌘ Command.md>) 
    * that asks for user data in [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>)
    * triggering the following flows:
      * [🧑‍🦰👉💼 Share Bind @ Wallet](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind.md>)
      * [🧑‍🦰👉💼 Share Token @ Wallet](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token.md>)
      * [🧑‍🦰👉💼 Share Token+ID @ Wallet](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/05 🧑‍🦰👉💼 Share Token+ID.md>)

    ---
    <br/>


3. **What's the SHARE syntax?**

    ```yaml
    SHARE|<code> >> $shared
        Codes:
            - <code-1>
            - <code-n>
        Context:
            {context}
    ```

   
    | Argument| Purpose
    |-|-
    | `<code-n>`  | [Schema Codes 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>) for [`Query@Broker`](<../../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>)
    | `{context}`| Object with context, when applicable.
    | `$shared`| An object returned by [`Collect@Vault`](<../../../6 🅰️ APIs/95 🗄️🅰️ Vault/01 💼🚀🗄️ Collect.md>).<br/> Or a Token list from [`Receive@Consumer`](<../../../6 🅰️ APIs/30 💼🅰️ Consumer/03 🧑‍🦰🐌💼 Receive.md>).


    ---
    <br/>

4. **What does a Chat look like?**

    | [Domain](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | [Prompt](<../13 🤔 Prompts/01 🤔 Prompt.md>) | [User](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 💼 [Consumer](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | ℹ️ Tell me your name.
    | 🧢 [Persona](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | 🫥 Share social name? [No] <br/> - [ Personal ] 🧑‍🦰 <br/> - [ Work ] 💼       | > Personal
    | 💼 [Consumer](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | ℹ️ Received: [Change] <br/> - Name: Alice <br/> - Pronouns: she/her
    | 💼 [Consumer](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | ✅ Hi, Alice!

    

    ```yaml
    # 😃 Talker
    INFO|Tell me your name.
    SHARE|nlweb.org/PERSONA/NAME/SOCIAL >> $social
    SUCCESS|Hi, {$social.Name}!
    ```

    | [Command ⌘](<10 ⌘ Command.md>) | Purpose
    |-|-
    | ⤵️ [`IF`](<21 ⤵️ IF flow.md>) | To verify the result.  


    The structure of the shared data is as follows.
   
    | Data | [Schema Code 🧩](<../24 🗄️ Vaults/02 🧩 Schema Code.md>)
    |-|-
    | Social Name |  [`nlweb.org/PERSONA/NAME/SOCIAL` 🧩](<../../../8 📜 Manifests/👥 nlweb.org/{codes}/PERSONA/🧩 PersonaNameSocial.md>)
   
    ---
    <br/>


5. **What are use cases of SHARE?**

    |Data | Use case|
    |-|-
    | 🆔 [Identity](<../../../4 ⚙️ Solution/30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>)  |[Prove 21+ to enter a casino 🎰](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    | 🧚 [Curator](<../../../4 ⚙️ Solution/30 🫥 Agents/03 🧚 Curators/01 🧚🫥 Curator agent.md>) | [Drinking preferences at a bar 🍸](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/21 🪑 Seat: Order water.md>)
    | 🧢 [Persona](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | [Name to be called when food is ready 🌭](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    | [🗓️ Scheduler](<../../../4 ⚙️ Solution/30 🫥 Agents/38 🕓 User Timeline/04 🗓️🗄️ Scheduler agent.md>) | [Date and time for a table reservation 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    | 🧢 [Persona](<../../../4 ⚙️ Solution/30 🫥 Agents/02 🧢 Personas/02 🧢🫥 Persona agent.md>) | [Booking contacts to reserve a table 🍽️](<../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)

    ---
    <br/>