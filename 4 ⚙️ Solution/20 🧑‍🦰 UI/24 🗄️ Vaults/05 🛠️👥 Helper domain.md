🛠️ Helper domain
===

1. **What are Helper domains?**

    A [Helper 🛠️👥](<05 🛠️👥 Helper domain.md>) is
    - any [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) that support other [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) 
    - by offloading common undifferentiated responsibilities.

    ---
    <br/>

1. **How do Helpers compare to Vaults?**

    * They are similar to [Vault 🗄️ domains](<03 🗄️🎭 Vault role.md>), 
        * but focused on [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) 
        * instead of [Wallet 🧑‍🦰 apps](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).
    * Given the similarity, 
        * some [Vault 🗄️ domains](<03 🗄️🎭 Vault role.md>) may also be Helpers 🛠️ 
        * e.g., [Payer 💳 domains](<../../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>).

    ---
    <br/>

1. **What are examples of Helper domains?**
   
    | Helper 🛠️ | Example | Responsibilities
    |-|-|-
    | [👀 Ads](<../../30 🫥 Agents/10 🔎 Finders/03 👀👥 Advertiser helper.md>) | GoogleAds | Intermediates ad workflows for [Brokers 🤵](<../03 🤵 Brokers/03 🤵 Broker domain.md>)
    | [🤝 Biller](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>) | ApplePay | Manages billing cycles between [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>)
    | [🤵 Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | WhatsApp | Manages [Chats](<../12 💬 Chats/01 💬 Chat.md>) between [Wallets 🧑‍🦰](<../01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) and [Hosts 🤗](<../12 💬 Chats/04 🤗🎭 Host role.md>)
    | [⏳ Buffer](<../../40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) | Kafka | Throttles [Streamers 🌬️](<../../40 👥 Domains/41 📨 Comms/02 🌬️🎭 Streamer role.md>) for [Subscribers 🔔](<../../40 👥 Domains/41 📨 Comms/04 🔔🎭 Subscriber role.md>)
    | [🏦 Collector](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | CapitalOne | Collects money from [Payers 💳](<../../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) for [Sellers 💵](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>)
    | [🔐 Keymaker](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/05  🔐🏭 Keymaker supplier.md>) | - | Manages [Padlocks 🔒](<../../70 🌳 Ambient/75 🔒 Brand Padlocks/01 🔒 Padlock device.md>) for [Brands 🍏](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>)
    | [💳 Payer](<../../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | PayPal | Pays [Collectors 🏦](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) for [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>)
    | [🖨️ Printer](<../../70 🌳 Ambient/71 💠 Brand Things/08 🖨️🏭 Printer helper.md>) | - | Prints [Locators 🔆](<../11 🔆 Locators/01 🔆 Locator.md>) for [Brand 🍏](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>) and [Host 🤗](<../12 💬 Chats/04 🤗🎭 Host role.md>)
    | [🛰️ Relayer](<../../60 🧰 Edge/61 🔌 Pluggables/04 🛰️🛠️ Relayer helper.md>)
    | [🪄 Wand](<../../70 🌳 Ambient/71 💠 Brand Things/09 🪄🛠️ Wand helper.md>) | - | Manages [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) for [Things 💠](<../../70 🌳 Ambient/71 💠 Brand Things/01 💠 Thing.md>) for [Brands 🍏](<../../70 🌳 Ambient/71 💠 Brand Things/07 🍏🎭 Brand role.md>)

    ---
    <br/>


1. **What roles do Helpers implement?**

    | [Role 🎭](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | Purpose
    |-|-
    | [🤗 Host](<../12 💬 Chats/04 🤗🎭 Host role.md>) | To open [Chats 💬](<../12 💬 Chats/01 💬 Chat.md>) with domain-admin users
    | [🪢 Integrator](<../12 💬 Chats/06 🪢🎭 Integrator role.md>) | To manifest its services to  [Finder 🔎 domains](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>)
    | [🗄️ Vault](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | To store user profiles with [HOST/PROFILE 🧩](<../../../7 🧩 Codes/HOST/🧩 HostPersonalize.md>)
    | [💵 Seller](<../../30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) | To sell the usage plans via a [Biller 💳 helper domain](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>)
    

    ---
    <br/>


1. **What other Helpers do Helpers leverage?**

    | [Helper 🛠️](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)  | Purpose 
    |-|-
    | [🤝 Biller](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>) | To manage usage and subscription plans.
    | [🏦 Collector](<../../30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | To collect usage and subscription payments.
    
    ---
    <br/>
    
    

1. **How can domain-admin users register with a Helper?**

    |#| Group | Step
    |-|-|-
    |1| `Find` | [Find 🔎](<../../30 🫥 Agents/10 🔎 Finders/02 🔎🫥 Finder vault.md>) a [Helper 🛠️ ](<05 🛠️👥 Helper domain.md>) with the desired services
    |2| `Chat` | [Chat 💬](<../12 💬 Chats/01 💬 Chat.md>) with the Helper's [Host 🤗 role](<../12 💬 Chats/04 🤗🎭 Host role.md>)
    |3| `Bind`| [Bind 🔗](<../24 🗄️ Vaults/01 🔗 Bind.md>) to the Helper's [Vault 🗄️ role](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
    |4| `Bill` | Subscribe a plan in the Helper's [Biller 🤝](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>)
    |5| `Link` | Link a [Payer 💳](<../../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) with the Helper's [Biller 🤝](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>)


    ---
    <br/>

1. **What does the registration Chat look like?**

    | Service | Prompt  | User 
    | - | - | - 
    | 🛠️ [Helper](<05 🛠️👥 Helper domain.md>) | 😃 Hi! What do you need? <br/>- [ Register ]  | > Register
    | 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Ready to register?](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/05 🤗⏩🧑‍🦰 Form 📝.md>) [Yes, No] <br>- Your broker binds with us 🔗 <br/>- You choose a billing plan 🤝 <br/>- Your payer adds a method 💳 <br/>- Your identity signs the terms 🆔 | > Yes
    | 🤵 [Broker](<../03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Bind?](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind.md>) [Yes, No, +]<br/>- [Host Profile 🧩](<../../../7 🧩 Codes/HOST/🧩 HostPersonalize.md>) | > Yes 
    | 🤵 [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) | 🫥 [Allow guest domain?](<../../../5 ⏩ Flows/50 🤗⏩ Hosts/03 🤗⏩🧑‍🦰 Invite 🛠️.md>) [Yes, No]  <br/> - Any Biller 🤝<br/>- [ Always ] for Any Helper 🛠️ | > Always
    | 🤝 [Biller](<../../30 🫥 Agents/04 💳 Payers/06 🤝🛠️ Biller helper.md>) | 😃 What plan to subscribe? <br/>- [ Simple ] pay-as-you-go  <br/>- [ Monthly ] commitment | > Simple
    | 💳 [Payer](<../../30 🫥 Agents/04 💳 Payers/03 💳🎭 Payer role.md>) | 🫥 Link to Any Biller? [Yes, No, +] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC 
    | 🆔 [Identity](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 [Sign terms?](<../../30 🫥 Agents/05 🆔 Identities/16 🆔🔏 Verify Signatures.md>) 📄 [Yes, No] | > Yes
    | 🆔 [Identity](<../../30 🫥 Agents/05 🆔 Identities/01 🆔🫥 Identity agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../30 🫥 Agents/05 🆔 Identities/21 🆔😶 Face scan.md>)
    | 🛠️ [Helper](<05 🛠️👥 Helper domain.md>) | ✅ Done!
    |

    Here's the [Talker 😃](<../../../9 😃 Talkers/10 📘 Talker specs/10 😃 Talker.md>).

    ```yaml
    💬 Register:                # Entry menu
    - FORM|Register             # Provide instructions
    - BIND|@HOST/PROFILE        # Bind to Wallet

    - INVITE >> $billed:        
        Invitee: any-biller.com # Invite the Biller
        Code: @BILLER/SUBSCRIBE # Run the subscription
    
    - FREEZE >> $inputs:        # Freeze all inputs
        Billed: {$billed}       # Add billing info
        Chat: {.Chat}           # Add context

    - EVAL|{Save($inputs)}      # Save the register

    - SUCCESS|Done!             # Inform success
    - GOODBYE                   # Show advertisement
    ```

    | [Command ⌘](<../../../9 😃 Talkers/40 🌊 Talker flows/10 ⌘ Command.md>) | Purpose
    |-|-
    | 📝 [`FORM`](<../../../9 😃 Talkers/60 ⏩ Msg flows/41 📝 FORM msg.md>) | To provide instructions
    | 🔗 [`BIND`](<../../../9 😃 Talkers/60 ⏩ Msg flows/44 🔗 BIND msg.md>) | To create a user profile
    | 🛠️ [`INVITE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/46 🛠️ INVITE msg.md>) | To subscribe the user to plan
    | ❄️ [`FREEZE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/42 ❄️ FREEZE msg.md>) | To disable past inputs
    | ⬇️ [`EVAL`](<../../../9 😃 Talkers/30 🗃️ Talker data/20 ⬇️ EVAL flow.md>) | To register on the database
    | ✅ [`SUCCESS`](<../../../9 😃 Talkers/20 🤔 Prompts/4 ⚠️ Status prompts/23 ✅ SUCCESS prompt.md>) | To say that it was successful
    | 👋 [`GOODBYE`](<../../../9 😃 Talkers/60 ⏩ Msg flows/50 👋 GOODBYE.md>) | To show advertising
    

    ---
    <br/>

