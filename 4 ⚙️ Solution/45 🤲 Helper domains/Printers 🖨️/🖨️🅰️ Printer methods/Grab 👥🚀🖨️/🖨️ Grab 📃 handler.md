# 🖨️ Grab 📃 handler

> Purpose

* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/📃 Script.md>) that implements the [`Grab@Printer` 🅰️ method](<🖨️ Grab 🚀 request.md>).

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
- PARSE|$.Msg.Locator >> $locator

# Only create Alias for Hosts
- IF|$locator.Schema.Is(.HOST):
    Else: 
      RETURN:
        Status: UNHOST

# Save on the table
- SAVE|PrinterAliases >> $locator:
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

| Needs||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/⌘ Command.md>) |  [`ASSERT`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`REEL`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/REEL 🎣/🎣 REEL ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`PrinterAliases` 🪣 table](<../../🖨️🪣 Printer tables/PrinterAliases 🪣 table.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$Holder 🧠.md>) | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Schemas 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)  | [`HOST`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>)
|