# 🤵 Resolve Alias 📃 script

> Part of the [`Locate@Broker` 📃 script](<../🤵 Locate 📃 handler.md>)


## Diagram

![alt text](<🤵 Resolve Alias ⚙️ uml.png>)

## Script

```yaml
📃 Resolve-Alias:

# Verify the required inputs
- ASSERT|$.Inputs:
    AllOf: Locator
    
# Parse the locator
- PARSE >> $locator:
    Locator: $Locator

# Resolve any ALIAS locator
- IF|$locator.IsAlias:

    # Send the request to the Printer
    - SEND >> $resolved:
        Header:
            To: $locator.Host
            Subject: Resolve@Printer
        Body:
            Locator: $.Msg.Locator

    # Parse the locator again
    - PARSE >> $locator:
        Locator: $resolved

- RETURN|$locator
```

<br/>

| Uses | |
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PARSE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) 
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Resolve@Printer` 🅰️](<../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Resolve 👥🚀🖨️/🖨️ Resolve 🚀 call.md>) 
| [Schemas 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)   | [`ALIAS` 🧩](<../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
| 