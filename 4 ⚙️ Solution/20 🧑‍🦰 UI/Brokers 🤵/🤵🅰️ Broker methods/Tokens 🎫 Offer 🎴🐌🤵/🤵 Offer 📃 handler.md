<!-- TODO: add a script diagram -->

# 🤵 Offer 📃 handler

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
    Set: Broker.Chats
    Key: $.Msg.Chat

# Only allow offers from the Host
- ASSERT|$.Msg:
    From: $chat.Host

# Translate the Issuer and Schema
- TRANSLATE >> $graph:
    Domain: $.Msg.From
    Schema: $.Msg.Schema
    To: $chat.Wallet.Language

# Get the title
- TRANSLATE >> $title:
    Text: (({$graph.Schema})), 
       by (({$graph.Domain}))
    To: $chat.Wallet.Language

# Save the Offer
- SAVE|Broker.Tokens:
        
    # Set the key
    ID: .UUID
    Wallet: $chat.Wallet.ID

    # Add given inputs
    Hook: $.Msg.Hook
    Issuer: $.Msg.From
    Schema: $.Msg.Schema
    Starts: $.Msg.Starts
    Expires: $.Msg.Expires
    
    # Add translations
    Issuer$: $graph.Domain
    Schema$: $graph.Schema
    Title: $title

    # Set the status
    Status: OFFERED

    # Set the cache expiration
    .Delete: 
        .Lower:
            $.Msg.Expires,
            Now.Add(30 days)


# Update the domain translation
- RUN|Update-Domain:
    Name: $.Msg.From
    Title: $translation.Domain

- CONFIRM|Save token? >> $saved:
    Details: 
```

<!-- TODO: Finish the detail -->

Uses||
-|-
[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Domain`](<../../🤵🪣 Broker tables/Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) [`Tokens`](<../../🤵🪣 Broker tables/Tokens 🎫 table/🪣 Tokens/🤵 Broker.Tokens 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsAbove`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsAbove}.md>) [`.IsBelow`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsBelow}.md>) [`.Lower`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Lower}.md>) [`.Now`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Now}.md>) [`.UUID`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.UUID}.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Chat 💬/💬 $.Chat 🧠 holder.md>) [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`$.Hosted`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`Update Domain` 📃 script](<../../🤵🪣 Broker tables/Domains 👥 table/🪣🔔 OnDomainAdded/🤵 OnDomainAdded 📃 trigger.md>)
|