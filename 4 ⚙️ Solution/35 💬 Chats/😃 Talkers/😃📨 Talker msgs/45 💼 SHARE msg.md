# 💼 Talker SHARE command

> Part of [Talker 😃](<../😃 Talker.md>)

<br/>

1. **What is a SHARE message command?**

    A `SHARE`
    * is a message [Command ⌘](<../😃⚙️ Talker cmds/10 ⌘ Command.md>) 
    * that asks for user data in [Schema Codes 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
    * triggering the following flows:
      * [🧑‍🦰👉💼 Share Bind @ Wallet](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/30 👉🔗 Binds/04 🧑‍🦰👉💼 Share Bind 🔗.md>)
      * [🧑‍🦰👉💼 Share Token @ Wallet](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/40 👉🎫 Tokens/04 🧑‍🦰👉💼 Share Token 🎫.md>)
      * [🧑‍🦰👉💼 Share Token+ID @ Wallet](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰⏩ Wallet flows/40 👉🎫 Tokens/05 🧑‍🦰👉💼 Share Token+ID.md>)

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
    | `<code-n>`  | [Schema Codes 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) for [`Query@Broker`](<../../../20 🧑‍🦰 UI/3 🤵 Brokers/🤵🅰️ Broker methods/6 🤵🅰️ Share/💼🐌🤵 Query.md>) <br/>For readability, a dot replaces `nlweb.org/`
    | `{context}`| Object with context, when applicable.
    | `$shared`| An object returned by [`Collect@Vault`](<../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/💼🚀🗄️ Collect.md>).<br/> Or a Token list from [`Receive@Consumer`](<../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/🧑‍🦰🐌💼 Receive.md>).


    ---
    <br/>

1. **What does the dot mean in a code?**

    Given that the [Schema Codes 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) defined by `nlweb.org` will be widely used, 
    * [Talkers 😃](<../😃 Talker.md>) accept a dot as a prefix of `nlweb.org/`.
    * Consider the following equal examples.

        ```yaml
        SHARE|.IDENTITY/OVER21 >> $social          
        SHARE|nlweb.org/IDENTITY/OVER21 >> $social 
        ```

    ---
    <br/>

1. **What does a [Chat 💬](<../../💬 Chats/💬 Chat.md>) look like?**

    | [Domain](<../../../40 👥 Domains/👥 Domains/👥 Domain.md>) | [Prompt](<../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../20 🧑‍🦰 UI/1 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>)
    | - | - | - |
    | 💼 [Consumer](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | ℹ️ Tell me your name.
    | 🧢 [Persona](<../../../50 🫥 Agent domains/Personas 🧢/🧢🫥 Persona agent.md>) | 🫥 Share social name? [No] <br/> - [ Personal ] 🧑‍🦰 <br/> - [ Work ] 💼       | > Personal
    | 💼 [Consumer](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | ℹ️ Received: [Change] <br/> - Name: Alice <br/> - Pronouns: she/her
    | 💼 [Consumer](<../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | ✅ Hi, Alice!

    

    ```yaml
    # 😃 Talker
    INFO|Tell me your name.
    SHARE|.PERSONA/NAME/SOCIAL >> $social
    SUCCESS|Hi, {$social.Name}!
    ```

    | [Command ⌘](<../😃⚙️ Talker cmds/10 ⌘ Command.md>) | Purpose
    |-|-
    | ⤵️ [`IF`](<../😃⚙️ Talker cmds/21 ⤵️ IF flow.md>) | To verify the result.  


    The structure of the shared data is as follows.
   
    | Data | [Schema Code 🧩](<../../../30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>)
    |-|-
    | Social Name |  [`nlweb.org/PERSONA/NAME/SOCIAL` 🧩](<../../../50 🫥 Agent domains/Personas 🧢/🧢🧩 Persona schemas/🧩 NAME'SOCIAL.md>)
   
    ---
    <br/>


1. **What are use cases of SHARE?**

    |Data | Use case|
    |-|-
    | 🆔 [Identity](<../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>)  |[Prove 21+ to enter a casino 🎰](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    | 🧚 [Curator](<../../../50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) | [Drinking preferences at a bar 🍸](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/21 🪑 Seat: Order water.md>)
    | 🧢 [Persona](<../../../50 🫥 Agent domains/Personas 🧢/🧢🫥 Persona agent.md>) | [Name to be called when food is ready 🌭](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    | [🗓️ Scheduler](<../../../50 🫥 Agent domains/Schedulers 🗓️/$ 🗓️🫥 Scheduler agent.md>) | [Date and time for a table reservation 🍽️](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    | 🧢 [Persona](<../../../50 🫥 Agent domains/Personas 🧢/🧢🫥 Persona agent.md>) | [Booking contacts to reserve a table 🍽️](<../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)

    ---
    <br/>