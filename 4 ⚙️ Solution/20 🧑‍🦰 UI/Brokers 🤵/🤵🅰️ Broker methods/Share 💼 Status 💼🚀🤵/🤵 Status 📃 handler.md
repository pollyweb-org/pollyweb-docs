# 🤵 Status 📃 handler

> [Script 📃](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Status@Broker` 🅰️ method](<🤵 Status 🚀 request.md>).

## Handler

```yaml
# Verify the Consumer message
- VERIFY|$.Msg

# Get the Token
- GET >> $token:
    Set: BrokerTokens
    Key: $.Msg.Token

# Return the Status
- REEL:
    Status: $token.Status
    Starting: $token.Starting
    Ending: $token.Ending
    Locator: $token.Locator
```