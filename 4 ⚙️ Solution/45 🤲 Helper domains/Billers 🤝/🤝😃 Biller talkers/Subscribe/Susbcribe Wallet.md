
1. **What does the registration Chat look like?**

    | [Domain](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) | [Prompt](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>) | [User](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
    | - | - | - 
    | 🛠️ [Helper](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) | 😃 Hi! What do you need? <br/>- [ Register ]  | > Register
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 [Ready to register?](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⏩ Consumer flows/Inform 💼⏩📝/💼 Inform ⏩ flow.md>) [Yes, No] <br>- Your broker binds with us 🔗 <br/>- You choose a billing plan 🤝 <br/>- Your payer adds a method 💳 <br/>- Your identity signs the terms 🆔 | > Yes
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 [Bind?](<../../../../20 🧑‍🦰 UI/Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind vault ⏩ flow.md>) [Yes, No, +] <br/>- [Vault 🧩](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🧩 Vault schemas/🧩 VAULT'SELF.md>) | > Yes 
    | 🤵 [Broker](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵/🤵 Broker 🤲 helper.md>) | 🫥 [Allow guest domain?](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⏩ Host flows/Invite 🤗⏩🤲/🤗 Invite ⏩ flow.md>) [Yes, No]  <br/> - Any Biller 🤝<br/>- [ Always ] for Any Helper 🤲 | > Always
    | 🤝 [Biller](<../../🤝 Biller/🤝 Biller 🤲 helper.md>) | 😃 What plan to subscribe? <br/>- [ Simple ] pay-as-you-go  <br/>- [ Monthly ] commitment | > Simple
    | 💳 [Payer](<../../../../41 🎭 Domain Roles/Payers/💳🎭 Payer role.md>) | 🫥 Link to Any Biller? [Yes, No, +] <br/>- [ card ABC ] + $0.10<br/>- [ card DEF ] (free) | > card ABC 
    | 🆔 [Identifier](<../../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) | 🫥 [Sign terms?](<../../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/5 Verify Signatures 🆔⏩🔏/🆔⏩ Verify Signatures 🔏.md>) 📄 [Yes, No] | > Yes
    | 🆔 [Identifier](<../../../../50 🫥 Agent domains/Identifiers 🆔/🆔 Identifier agent/🆔 Identifier 🫥 agent.md>) | 🫥 Let me see if it's you. | [📸 selfie](<../../../../50 🫥 Agent domains/Identifiers 🆔/🆔⏩ Identifier flows/6 Face scan 🆔⏩😶/6 🆔⏩😶 Face scan.md>)
    | 🛠️ [Helper](<../../../../41 🎭 Domain Roles/Helpers 🤲/🤲 Helper/🤲🎭 Helper role.md>) | ✅ Done!
    |

    Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>).

    ```yaml
    💬 Register:                # Entry menu
    - INFORM: Register           # Provide instructions
    - BIND: .VAULT               # Bind to Wallet

    - INVITE >> $billed:        
        Invitee: any-biller.dom # Invite the Biller
        Schema: .BILLER/SUBSCRIBE # Run the subscription
    
    - FREEZE >> $inputs:        # Freeze all inputs
        Billed: $billed         # Add billing info
        Chat: $.Chat            # Add context

    - CALL Save($inputs)        # Save the register

    - DONE: Done!             # Inform success
    - GOODBYE                   # Show advertisement
    ```
    Uses: [`BIND`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⌘ Vault cmds/BIND 🔗/🔗 BIND ⌘ cmd.md>) [`CALL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`FREEZE`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/FREEZE ❄️/❄️ FREEZE ⌘ cmd.md>) [`GOODBYE`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗⌘ Host cmds/GOODBYE 👋/👋 GOODBYE ⌘ cmd.md>) [`INFORM`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INFORM 📝/📝 INFORM ⌘ cmd.md>) [`INVITE`](<../../../../41 🎭 Domain Roles/Consumers 💼/💼⌘ Consumer cmds/INVITE 🤲/🤲 INVITE ⌘ cmd.md>) [`DONE`](<../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/DONE ✅/DONE ✅ prompt.md>)    

    ---
    <br/>
