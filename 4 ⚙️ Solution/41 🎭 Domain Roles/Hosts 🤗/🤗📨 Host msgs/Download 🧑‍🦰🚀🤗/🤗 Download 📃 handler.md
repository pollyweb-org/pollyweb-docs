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
- ASSERT|$.Msg:
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
- VERIFY|$.Msg:
    Key: $.Chat.PublicKey

# Format the appendix content
- CASE|$appendix.Type:

    PDF: # allow PDF pagination
        SET|$appendix:
            Content.Page: $.Msg.Page

    PNG,JPEG: # allow image resizing
        SET|$appendix:
            Content.MaxWidth: $.Msg.MaxWidth
            Content.MaxHeight: $.Msg.MaxHeight

# Return the appendix content
- RETURN:
    $appendix.Content
```

[`.Or`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Or ⓕ.md>) [`.Is`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>) [`.Page`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Page ⓕ.md>) [`.MaxWidth`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/MaxWidth ⓕ.md>) [`.MaxHeight`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/MaxHeight ⓕ.md>)