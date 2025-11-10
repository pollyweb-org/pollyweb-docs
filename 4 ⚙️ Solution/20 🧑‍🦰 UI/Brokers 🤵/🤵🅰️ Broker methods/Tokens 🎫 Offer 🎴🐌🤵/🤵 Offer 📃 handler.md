<!-- TODO: add a script diagram -->

# 🤵📃 Offer

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Offer@Broker` 🅰️ method](<🤵 Offer 🐌 msg.md>)

> Part of the [`Save Token` 👉 flow](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Save Token 👉🎴🎫/🧑‍🦰 Save token ⏩ flow.md>).
> 
<br/>

## Script

```yaml
📃 Offer:

# Verify the Issuer's message
- VERIFY|$.Msg

# Assert the required inputs
- ASSERT|$.Msg:
    - AllOf: Chat, Hook, Schema
    - UUIDs: Chat, Hook
    - Texts: Schema
    - Times: Starts, Expires
    - Starts.IsBelow(Expires)
    - Expires.IsAbove(.Now)

# Get the Chat
- READ >> $chat:
    Set: BrokerChats
    Key: $.Msg.Chat

# Only allow offers from the Host
- ASSERT|$.Msg:
    From: $chat.Host

# Translate the Issuer and Schema
- SEND >> $translation:
    Header:
        To: $.Hosted.Graph
        Subject: Translate@Graph
    Body:
        Domain: $.Msg.From
        Schema: $.Msg.Schema

# Save the Offer
- SAVE|BrokerOffers:
    
    # Set the cache expiration
    .Delete: 1 hour
    
    # Set the key
    ID: .UUID
    Wallet: $chat.Wallet.ID

    # Add given inputs
    Hook: $.Msg.Hook
    Issuer: $.Msg.From
    Issuer$: $translation.Domain
    Schema: $.Msg.Schema
    Schema$: $translation.Schema
    Starts: $.Msg.Starts
    Expires: $.Msg.Expires

# Update the domain translation
- RUN|Update-Domain:
    Name: $.Msg.From
    Title: $translation.Domain
```

> Run [`Update Domains` 📃 script](<../../🤵🪣 Broker tables/Domains 👥 table/🤵 Update Domain 📃 script.md>)

<!-- TODO: Finish the detail -->

```yaml
- CONFIRM|Save token? >> $saved:
    Details: 
```

<br/>

Uses||
-|-
[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Domain`](<../../🤵🪣 Broker tables/Domains 👥 table/🤵 BrokerDomains 🪣 table.md>) [`Tokens`](<../../🤵🪣 Broker tables/Tokens 🎫 table/🤵 BrokerTokens 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`$.Hosted`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`Update Domains` 📃 script](<../../🤵🪣 Broker tables/Domains 👥 table/🤵 Update Domain 📃 script.md>)
|