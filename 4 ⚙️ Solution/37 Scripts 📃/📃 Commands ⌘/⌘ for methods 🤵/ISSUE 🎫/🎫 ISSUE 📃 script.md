# 🎫 ISSUE 📃 script

[Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`ISSUE`](<🎫 ISSUE ⌘ cmd.md>) command.

## Flow

![alt text](<🎫 ISSUE ⚙️ uml.png>)

## How to call

```yaml
- RUN|.ISSUE:
    Schema: any-authority.dom/ANY-SCHEMA
    Starts: 2018-12-10T13:45:00.000Z
    Expires: 2018-12-10T13:45:00.000Z
    Properties: 
        {properties}
    Internals:
        {internals}
```

## Script

```yaml
📃 .ISSUE:

# Assert inputs
- ASSERT|$.Inputs:
    AllOf: Schema
    Texts: Schema
    Times: Starts, Expires

# Save the hook
- SAVE|Talker.Hooks >> $hook:
    Hook: .UUID
    Broker: $.Chat.Broker
    Chat: $.Chat.ID
    PublicKey: $.Chat.PublicKey
    Internals: $Internals
    Offer:
        Schema: $Schema
        Starts: $Starts
        Expires: $Expires
        Properties: $Properties
    
# Query the Broker
- SEND:
    Header:
        To: $.Chat.Broker
        Subject: Offer@Broker
    Body: 
        Chat: $.Chat.ID
        Hook: $hook.Hook
        Schema: $Schema
        Starts: $Starts
        Expires: $Expires

# Wait for the shared data
- WAIT >> $token:
    Hook: $hook.Hook

# Return the data
- RETURN:
    $token
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`WAIT`](<../../⌘ for async/WAIT 🧘/🧘 WAIT ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`TalkerHooks`](<../../../../35 💬 Chats/Talkers 😃/😃🪣 Talker tables/😃 Talker.Hooks 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`.Chat`](<../../../📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Offer@Broker` 🅰️ method](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Tokens 🎫 Issue 🎴🐌🤵/🤵 Issue 🐌 msg.md>) <br/> [`Issued@Issuer` 🅰️ method](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Issued 🧑‍🦰🚀🎴/🎴 Issued 🚀 call.md>) <br/> [`Accepted@Issuer` 🅰️ method](<../../../../41 🎭 Domain Roles/Issuers 🎴/🎴🅰️ Issuer methods/Offered 🤵🐌🎴/🎴 Offered 🐌 msg.md>)
|