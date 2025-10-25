# 💼 Talker `SHARE` command

> Part of [Talker 😃](<../../../😃 Talker role.md>)

<br/>

1. **What is a SHARE message command?**

    A `SHARE`
    * is a message [Command ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) 
    * that asks for user data in [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
    * triggering the following flows:
      * [🧑‍🦰👉💼 Share Bind @ Wallet](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Bind 🔗.md>)
      * [🧑‍🦰👉💼 Share Token @ Wallet](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Token 🎫.md>)
      * [🧑‍🦰👉💼 Share Token+ID @ Wallet](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/👉💼 Share Token+ID.md>)

    ---
    <br/>


1. **What's the SHARE syntax?**

    ```yaml
    SHARE|<code> >> $shared
    ```

    ```yaml
    SHARE >> $shared:
        Schema: <code>
        Context: {context}
    ```

    ```yaml
    SHARE >> $shared:
        Schemas:
            - <code-1>
            - <code-n>
        Context: {context}
    ```

   
    | Argument| Purpose
    |-|-
    | `<code-n>`  | [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) for [`Query@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/...for Share 💼/Query 💼🐌🤵/Query 🐌 msg.md>) <br/>For readability, a dot replaces `nlweb.dom/`
    | `{context}`| Object with context, when applicable.
    | `$shared`| An object returned by [`Collect@Vault`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Collect/💼🚀🗄️ Collect.md>).<br/> Or a Token list from [`Receive@Consumer`](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼🅰️ Consumer methods/🧑‍🦰🐌💼 Receive.md>).


    ---
    <br/>

1. **What does the dot mean in a code?**

    Given that the [Schema Codes 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) defined by `nlweb.dom` will be widely used, 
    * [Talkers 😃](<../../../😃 Talker role.md>) accept a dot as a prefix of `nlweb.dom/`.
    * Consider the following equal examples.

        ```yaml
        SHARE|.IDENTITY/OVER21 >> $social          
        SHARE|nlweb.dom/IDENTITY/OVER21 >> $social 
        ```

    ---
    <br/>

1. **What does a [Chat 💬](<../../../../💬 Chats/💬 Chat.md>) look like?**

    | [Domain](<../../../../../40 👥 Domains/👥 Domain.md>) | [Prompt](<../../../../🤔 Prompts/🤔 Prompt.md>) | [User](<../../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
    | - | - | - |
    | 💼 [Consumer](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | ℹ️ Tell me your name.
    | 🧢 [Persona](<../../../../../50 🫥 Agent domains/Personas 🧢/🧢🫥 Persona agent.md>) | 🫥 Share social name? [No] <br/> - [ Personal ] 🧑‍🦰 <br/> - [ Work ] 💼       | > Personal
    | 💼 [Consumer](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | ℹ️ Received: [Change] <br/> - Name: Alice <br/> - Pronouns: she/her
    | 💼 [Consumer](<../../../../../41 🎭 Domain Roles/Consumers 💼/💼🎭 Consumer role.md>) | ✅ Hi, Alice!

    

    ```yaml
    # 😃 Talker
    INFO|Tell me your name.
    SHARE|.PERSONA/NAME/SOCIAL >> $social
    SUCCESS|Hi, {$social.Name}!
    ```

    Commands: [`INFO`](<../../../../🤔 Prompts/🤔📢 Prompt status/INFO ℹ️/INFO ℹ️ prompt.md>) [`SHARE`](<SHARE 💼 msg.md>) [`SUCCESS`](<../../../../🤔 Prompts/🤔📢 Prompt status/SUCCESS ✅/SUCCESS ✅ prompt.md>)


    The structure of the shared data is as follows.
   
    | Data | [Schema 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
    |-|-
    | Social Name |  [`nlweb.dom/PERSONA/NAME/SOCIAL` 🧩](<../../../../../50 🫥 Agent domains/Personas 🧢/🧢🧩 Persona schemas/🧩 NAME'SOCIAL.md>)
   
    ---
    <br/>


1. **What are use cases of SHARE?**

    |Data | Use case|
    |-|-
    | 🆔 [Identity](<../../../../../50 🫥 Agent domains/Identities 🆔/🆔🫥 Identity agent.md>)  |[Prove 21+ to enter a casino 🎰](<../../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    | 🧚 [Curator](<../../../../../50 🫥 Agent domains/Curators 🧚/🧚🫥 Curator agent.md>) | [Drinking preferences at a bar 🍸](<../../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/21 🪑 Seat: Order water.md>)
    | 🧢 [Persona](<../../../../../50 🫥 Agent domains/Personas 🧢/🧢🫥 Persona agent.md>) | [Name to be called when food is ready 🌭](<../../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    | [🗓️ Scheduler](<../../../../../50 🫥 Agent domains/Schedulers 🗓️/$ 🗓️🫥 Scheduler agent.md>) | [Date and time for a table reservation 🍽️](<../../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    | 🧢 [Persona](<../../../../../50 🫥 Agent domains/Personas 🧢/🧢🫥 Persona agent.md>) | [Booking contacts to reserve a table 🍽️](<../../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)

    ---
    <br/>