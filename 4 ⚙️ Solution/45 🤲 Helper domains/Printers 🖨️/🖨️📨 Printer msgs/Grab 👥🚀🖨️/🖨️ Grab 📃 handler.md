# 🖨️ Grab 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Grab@Printer` 📨 msg](<🖨️ Grab 🚀 call.md>).

## Flow

![alt text](<🖨️ Grab ⚙️ uml.png>)

## Script

```yaml
# Verify the signature
- VERIFY|$.Msg

# Assert the inputs
- ASSERT|$.Msg:
    AllOf: Alias, Locator
    Texts: Alias, Locator

# Parse the locator
- PARSE >> $locator:
    Locator: $.Msg.Locator

# Only create Alias for Hosts
- IFNOT|$locator.Schema.Is(.HOST):
    RETURN:
      Status: UNHOST

# Save on the table
- SAVE|Printer.Aliases >> $locator:
    Alias: $.Msg.Alias
    Locator: $.Msg.Locator 
    .OnBlocked: $blocked

# Check if blocked
- IF|$blocked:

    # Return blocked
    Then: 
      RETURN:
        Status: BLOCKED

    # Respond with the Locator
    Else: 
      RETURN:
        Status: OK
```

| Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) |  [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`PARSE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`REEL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>)  [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Printer.Aliases` 🪣 table](<../../🖨️🪣 Printer tables/Aliases 🔆/🖨️ Printer.Aliases 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Schemas 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)  | [`HOST`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)
|