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

# Read the appendix
- READ >> $appendix:
    Set: Host.Appendixes
    Key: $.Msg.Appendix
    Assert: # only if the chat is active
        Chat.State: ACTIVE

# Verify the signature
- VERIFY|$.Msg:
    Key: $.Chat.PublicKey

# Return the appendix content
- RETURN|$appendix:
```