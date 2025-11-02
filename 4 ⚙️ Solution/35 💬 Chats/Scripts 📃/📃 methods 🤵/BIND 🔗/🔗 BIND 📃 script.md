# 😃📃 `.BIND` script

> [Script 📃](<../../📃 basics/Script 📃.md>) that implements the [`BIND`](<🔗 BIND ⌘ cmd.md>) command.

> Invokes the [`Bindable@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)


## How to call

```yaml
- RUN|.BIND:
    User: my-user
    Schemas:
      - schema-1
      - schema-n
```


## Script

```yaml
📃 .BIND:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: Schemas, User
    Lists: Schemas

# Save the callback hook
- SAVE|TalkerHooks >> hook:
    Hook: .UUID
    Broker: $.Chat.Broker
    Chat: $.Chat.ID
    PublicKey: $.Chat.PublicKey
    Schemas: $:Schemas
    User: $:User

# Send the message to the Broker
- SEND:
    Header:
        To: $.Chat.Broker
        Subject: Bindable@Broker
    Body:
        Hook: $hook.Hook
        Chat: $.Chat.ID
        Schemas: $:Schemas

# Wait for the shared data
#- WAIT >> $shared:
#    Hook: $hook.Hook

# Return the data
#- RETURN:
#    $shared
```

<!-- TODO: finish the code -->

> Followed by the [`Bound@Vault` 🅰️ method](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>) 


|Uses||
|-|-
| [Commands ⌘](<../../📃 basics/Command ⌘.md>) | [`ASSERT`](<../../📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Hook@Talker`](<../../../Talkers 😃/😃🪣 Talker tables/😃 TalkerHooks 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Bindable@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bindable 🗄️🐌🤵/🤵 Bindable 🐌 msg.md>)
| [Holders 🧠](<../../📃 basics/Holder 🧠.md>) | [`$.Chat`](<../../📃 holders 🧠/$.Chat 💬/💬 $.Chat 🧠 holder.md>)
|