# 🤵 OnChatInserted 📃 handler

> Flow
* Triggered by [`Locate@Broker` 🅰️ method](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)

<br/>

## Diagram

![alt text](<🤵 OnChatInserted ⚙️ uml.png>)

<br/>

## Script 

```yaml
📃 OnChatInserted:

# Assert the Chat
- ASSERT|$Chat:
    OneOf: Locator, Key
    Texts: Locator, Key

# If already resolved, set state and exit
- IF|$Chat.Key:
    - SAVE|$Chat:
        .State: RESOLVED
    - RETURN

# Parse the locator
- PARSE >> $locator:
    Locator: $Chat.Locator

# Resolve any ALIAS locator
- WHILE|$locator.IsAlias:

    # Send the request to the Printer
    - SEND >> $resolved:
        Header:
            To: $locator.Host
            Subject: Resolve@Printer
        Body:
            Locator: $Chat.Locator

    # Parse the locator again
    - PARSE >> $locator:
        Locator: $resolved

# Finally, set the Chat to RESOLVED
- SAVE|$Chat:
    .State: RESOLVED
    Host: $locator.Host
    Key: $locator.Key
    Inputs: $locator.Inputs
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PARSE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`WHILE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/WHILE/🔄 WHILE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) |  [`$.Hosted`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`About@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 About/🕸 About 🚀 call.md>) 
|