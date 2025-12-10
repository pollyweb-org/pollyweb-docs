# 💼 Talker `SHARE` command

> Implementation
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* Implemented by the [`SHARE` 📃 script](<💼 SHARE 📃 script.md>)



## FAQ

1. **What is a SHARE message command?**

    `SHARE`
    * is a message [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that asks for user data in [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
    * triggering the following flows:
      * [🧑‍🦰👉💼 Share Bind @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Bind 👉🔗💼/🧑‍🦰 Share Bind ⏩ flow.md>)
      * [🧑‍🦰👉💼 Share Token @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token 👉🎫💼/🧑‍🦰 Share Token ⏩ flow.md>)
      * [🧑‍🦰👉💼 Share Token+ID @ Wallet](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token+ID 👉🆔💼/🧑‍🦰 Share Token+ID ⏩ flow.md>)

    ---
    <br/>


1. **What's the SHARE syntax?**

    ```yaml
    # Comprehensive
    SHARE|<schema-1> >> $shared: # For a single inline schema
        Schema: <schema-2>       # For a single multiline schema
        Schemas:                 # For multiple alternatives
            - <schema-3>
            - <schema-n>
        Context: {context}       # Optional context
        Domain: {domain}         # Optional specific vault/issuer
    ```

    ```yaml
    # Single schema, no context
    SHARE|<code> >> $shared
    ```

    ```yaml
    # Single schema, with context
    SHARE|<code> >> $shared:
        Context: {context}
    ```

    ```yaml
    # Single schema, comprehensive
    SHARE >> $shared:
        Schema: <code>
        Context: {context}
    ```

   
    | Input| Purpose
    |-|-
    | `Schema`  | [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) for [`Query@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Share 💼 Query 💼🐌🤵/🤵 Query 🐌 msg.md>) 
    ||For readability, a dot replaces `nlweb.dom/`
    | `Context`| Object with context, when applicable
    | `Domain`| Optional specific domain for the [`Share Token+ID` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Share Token+ID 👉🆔💼/🧑‍🦰 Share Token+ID ⏩ flow.md>)
    | `$shared`| [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) data returned by [`Collect@Vault`](<../../../Vaults 🗄️/🗄️📨 Vault msgs/Collect 💼🚀🗄️/🗄️ Collect 🚀 call.md>)
    || Or a [Token 🎫](<../../../../30 🧩 Data/Tokens 🎫/🎫 Token/🎫 Token.md>) from [`Receive@Consumer`](<../../💼📨 Consumer msgs/Receive 🧑‍🦰🐌💼/💼 Receive 🐌 msg.md>)


    ---
    <br/>

1. **What does the dot mean in a code?**

    Given that the [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) defined by `nlweb.dom` will be widely used, 
    * [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) accept a dot as a prefix of `nlweb.dom/`.
    * Consider the following equal examples.

        ```yaml
        SHARE|.IDENTITY/OVER21 >> $social          
        SHARE|nlweb.dom/IDENTITY/OVER21 >> $social 
        ```

    ---
    <br/>

1. **What does a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) look like?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 💼 [Consumer](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) | ℹ️ Tell me your name.
    | 🧢 [Persona](<../../../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) | 🫥 Share social name? [No] <br/> - [ Personal ] 🧑‍🦰 <br/> - [ Work ] 💼       | > Personal
    | 💼 [Consumer](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) | ℹ️ Received: [Change] <br/> - Name: Alice <br/> - Pronouns: she/her
    | 💼 [Consumer](<../../../../41 🎭 Domain Roles/Consumers 💼/💼 Consumer/💼🎭 Consumer role.md>) | ✅ Hi, Alice!

    

    ```yaml
    # 😃 Talker
    INFO|Tell me your name.
    SHARE|.PERSONA/NAME/SOCIAL >> $social
    DONE|Hi, {$social.Name}!
    ```

    Uses: [`INFO`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`SHARE`](<💼 SHARE ⌘ cmd.md>) [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)


    The structure of the shared data is as follows.
   
    | Data | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
    |-|-
    | Social Name |  [`nlweb.dom/PERSONA/NAME/SOCIAL` 🧩](<../../../../50 🫥 Agent domains/Personas 🧢/🧢🧩 Persona schemas/🧩 NAME'SOCIAL.md>)
   
    ---
    <br/>


1. **What are use cases of SHARE?**

    |Data | Use case|
    |-|-
    | 🆔 [Identity](<../../../../50 🫥 Agent domains/Identities 🆔/🆔 Identity agent/🆔🫥 Identity agent.md>)  |[Prove 21+ to enter a casino 🎰](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/10 🎰 Casinos/11 🚪 Enter anonymously.md>)
    | 🧚 [Curator](<../../../../50 🫥 Agent domains/Curators 🧚/🧚 Curator/🧚🫥 Curator agent.md>) | [Drinking preferences at a bar 🍸](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/30 🍸 Bars/21 🪑 Seat: Order water.md>)
    | 🧢 [Persona](<../../../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) | [Name to be called when food is ready 🌭](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/50 🌭 Street food/21 🎪 Stall: Buy hot dog 🌭.md>)
    | [🗓️ Scheduler](<../../../../50 🫥 Agent domains/Schedulers 🗓️/$ 🗓️🫥 Scheduler agent.md>) | [Date and time for a table reservation 🍽️](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)
    | 🧢 [Persona](<../../../../50 🫥 Agent domains/Personas 🧢/🧢 Persona agent/🧢🫥 Persona agent.md>) | [Booking contacts to reserve a table 🍽️](<../../../../../3 🤝 Use Cases/02 🍲 Eat & Drink/60 🍽️ Restaurants/31 🌐 Web: Book table 🗓️.md>)

    ---
    <br/>