# 💼 Talker SHARE command

> Part of [Talker 😃](<../10 📘 Talker specs/10 😃 Talker.md>)

<br/>

1. **What is a SHARE message command?**

    A `SHARE`
    * is a message [Command ⌘](<../40 🌊 Talker flows/10 ⌘ Command.md>) 
    * that asks for user data in [Schema Codes 🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
    * triggering the following flows:
      * [🧑‍🦰👉💼 Share Bind @ Wallet](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>)
      * [🧑‍🦰👉💼 Share Token @ Wallet](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>)
      * [🧑‍🦰👉💼 Share Token+ID @ Wallet](<../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/40 👉🎫 Tokens/05 🧑‍🦰👉💼 Share Token+ID.md>)

    ---
    <br/>


1. **What's the SHARE syntax?**

    ```yaml
    SHARE|<code> >> $shared
    ```

    ```yaml
    SHARE >> $shared:
        Code: <code>
        Context: {context}
    ```

    ```yaml
    SHARE >> $shared:
        Codes:
            - <code-1>
            - <code-n>
        Context: {context}
    ```

   
    | Argument| Purpose
    |-|-
    | `<code-n>`  | [Schema Codes 🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) for [`Query@Broker`](<../../6 🅰️ APIs/15 🤵🅰️ Broker/60 🤵🅰️ Share/61 💼🐌🤵 Query.md>) <br/>For readability, a dot replaces `nlweb.org/`
    | `{context}`| Object with context, when applicable.
    | `$shared`| An object returned by [`Collect@Vault`](<../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🅰️ Vault methods/💼🚀🗄️ Collect.md>).<br/> Or a Token list from [`Receive@Consumer`](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/💼🅰️ Consumer methods/🧑‍🦰🐌💼 Receive.md>).


    ---
    <br/>

1. **What does the dot mean in a code?**

    Given that the [Schema Codes 🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) defined by `nlweb.org` will be widely used, 
    * [Talkers 😃](<../10 📘 Talker specs/10 😃 Talker.md>) accept a dot as a prefix of `nlweb.org/`.
    * Consider the following equal examples.

        ```yaml
        SHARE|.IDENTITY/OVER21 >> $social          
        SHARE|nlweb.org/IDENTITY/OVER21 >> $social 
        ```

    ---
    <br/>

1. **What does a [Chat 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) look like?**

    | [Domain](<../../4 ⚙️ Solution/40 👥 Domains/$ 👥 Domains/👥 Domain.md>) | [Prompt](<../10 📘 Talker specs/20 🤔 Prompt.md>) | [User](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 💼 [Consumer](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) | ℹ️ Tell me your name.
    | 🧢 [Persona](<../../4 ⚙️ Solution/50 🫥 Agent domains/70 🧢 Personas/$ 🧢🫥 Persona agent.md>) | 🫥 Share social name? [No] <br/> - [ Personal ] 🧑‍🦰 <br/> - [ Work ] 💼       | > Personal
    | 💼 [Consumer](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) | ℹ️ Received: [Change] <br/> - Name: Alice <br/> - Pronouns: she/her
    | 💼 [Consumer](<../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/💼🎭 Consumer role.md>) | ✅ Hi, Alice!

    

    ```yaml
    # 😃 Talker
    INFO|Tell me your name.
    SHARE|.PERSONA/NAME/SOCIAL >> $social
    SUCCESS|Hi, {$social.Name}!
    ```

    | [Command ⌘](<../40 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
    |-|-
    | ⤵️ [`IF`](<../40 🌊 Talker flows/21 ⤵️ IF flow.md>) | To verify the result.  


    The structure of the shared data is as follows.
   
    | Data | [Schema Code 🧩](<../../4 ⚙️ Solution/30 🧩 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
    |-|-
    | Social Name |  [`nlweb.org/PERSONA/NAME/SOCIAL` 🧩](<../../7 🧩 Codes/PERSONA/🧩 PersonaNameSocial.md>)
   
    ---
    <br/>


1. **What are use cases of SHARE?**

    |Data | Use case|
    |-|-
    | 🆔 [Identity](<../../4 ⚙️ Solution/50 🫥 Agent domains/45 🆔 Identities/$ 🆔🫥 Identity agent.md>)  |[Prove 21+ to enter a casino 🎰](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    | 🧚 [Curator](<../../4 ⚙️ Solution/50 🫥 Agent domains/30 🧚 Curators/🧚🫥 Curator agent.md>) | [Drinking preferences at a bar 🍸](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/21 🪑 Seat: Order water.md>)
    | 🧢 [Persona](<../../4 ⚙️ Solution/50 🫥 Agent domains/70 🧢 Personas/$ 🧢🫥 Persona agent.md>) | [Name to be called when food is ready 🌭](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    | [🗓️ Scheduler](<../../4 ⚙️ Solution/50 🫥 Agent domains/75 🗓️ Schedulers/$ 🗓️🫥 Scheduler agent.md>) | [Date and time for a table reservation 🍽️](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    | 🧢 [Persona](<../../4 ⚙️ Solution/50 🫥 Agent domains/70 🧢 Personas/$ 🧢🫥 Persona agent.md>) | [Booking contacts to reserve a table 🍽️](<../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)

    ---
    <br/>