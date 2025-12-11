# 😃🔗 Talker `BIND` command

> About
* Part of [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)
* Part of the [🧑‍🦰 `Bind Vault` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind Vault ⏩ flow.md>)
* Implemented by the [`.BIND` 📃 script](<🔗 BIND 📃 script.md>)

<br/>

## FAQ

1. **What is the BIND message command?**

    `BIND`
    * is a message [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) 
    * that invokes the [🧑‍🦰 `Bind Vault` ⏩ flow](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind Vault ⏩ flow.md>).

    ---
    <br/>


1. **What does a [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) look like?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - |
    | 🗄️ [Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) |  😃 Hi! What do you need? <br/>- [ Bind ]  | > Bind
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | 🫥 [Bind?](<🔗 BIND ⌘ cmd.md>) [Yes, No] <br/> - Some schema 🧩 <br/> - By Any Vault <br/> - Description: Bla, bla | > Yes
    | 🗄️ [Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️ Vault/🗄️🎭 Vault role.md>) | ✅ [Done!](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)

    ---
    <br/>


1. **What's the BIND syntax?**

    ```yaml
    # Comprehensive
    - BIND >> $bind:
        Schema: $schema
        Reference: $reference
        Internals: $internals

    # Simple multi-line
    - BIND >> $bind:
        $schema

    # Simplest inline
    - BIND $schema
    ```
    | Input| Purpose 
    |-|-
    | `Schema` | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) for [`Bind@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>) 
    | `Reference` | [Hosted 📦 domain](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) internal reference to the [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
    | `Internals` | [Hosted 📦 domain](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) internal data about the [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
    | `$bind`  | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) item accepted, or empty if declined.
    
    ---
    <br/>

1. **What's the BIND syntax?**


    ```yaml
    # For a required schema.
    - BIND $schema
    - DONE Bound!
    ```

    | Input| Purpose 
    |-|-
    | `$schema` | [Schema 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) from [`Bind@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵📨 Broker msgs/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>) 

    ```yaml
    # For an optional schema.
    - BIND $schema >> $bound
    - IF $bound:
        Then: DONE Bound.
        Else: FAIL Not bound.
    ```

    | Input| Purpose
    |-|-
    | `$bound`  | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) item created.

    
    ---
    <br/>

1. **What does the dot mean in a schema?**

    Given that the [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) defined by `nlweb.dom` will be widely used, 
    * [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) accept a dot as a prefix of `nlweb.dom/`.
    
    Consider the following equal examples.

    ```yaml
    BIND|.IDENTITY/OVER21
    ```
    ```yaml
    BIND|nlweb.dom/IDENTITY/OVER21
    ```

    ---
    <br/>

1. **What does a Talker look like for static codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Bind:

   # Offer a bind.
   - BIND >> $bound:
       some-authority.dom/SOME-CODE

   # Verify it was bound.
   - IF $bound:
       Then: DONE Your wallet is bound.
       Else: FAIL Not bounded.
   ```

   Uses: [`BIND`](<🔗 BIND ⌘ cmd.md>) [`FAIL`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>) 

   ---
   <br/>




1. **What does a Talker look like for holder codes?**
    
   ```yaml
   # 😃 Talker 
   💬 Bind:

   # Offer the schemas
   - BIND $schema >> $bound

   # Check if any was bound
   - IF $bound:
       Then: DONE Your wallet is bound.
       Else: FAIL Not bounded.
   ```

   Uses: [`BIND`](<🔗 BIND ⌘ cmd.md>) [`FAIL`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/FAIL ❌/FAIL ❌ prompt.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)
   
   ---
   <br/>

