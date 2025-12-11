# 🤗 Download@Host 📃 handler

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Download@Host` 🚀 call](<🤗 Download 🚀 call.md>)

<br/>

## Diagram

![alt text](<🤗 Download ⚙️ uml.png>)

<br/>

## Handler

```yaml
📃 Download@Host:

# Assert the message
- ASSERT $.Msg:
    AllOf: Appendix
    UUIDs: Appendix
    Nums: Page, MaxWidth, MaxHeight

# Read the appendix
- READ >> $appendix:
    Set: Host.Appendixes
    Key: $.Msg.Appendix
    Assert: # only if the chat is active
        Chat.State: ACTIVE

# Verify the wallet signature
- VERIFY $.Msg:
    Key: $.Chat.PublicKey

# Format the appendix content
- CASE $appendix.Type >> $content:

    PDF: # allow PDF pagination
        $appendix.Content:
            .Page: $.Msg.Page

    PNG,JPEG: # allow image resizing
        $appendix.Content:
            .MaxWidth: $.Msg.MaxWidth
            .MaxHeight: $.Msg.MaxHeight

# Return the appendix content
- RETURN:
    $content
```

|Uses||
|-|-
| [Command ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SET`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SET ↘️/↘️ SET ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Host.Appendixes`](<../../🤗🪣 Host tables/Appendixes 📎 table/🪣 Appendixes/🤗 Host.Appendixes 🪣 table.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) |  [`.Page`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Page ⓕ.md>) [`.MaxWidth`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/MaxWidth ⓕ.md>) [`.MaxHeight`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/MaxHeight ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>)