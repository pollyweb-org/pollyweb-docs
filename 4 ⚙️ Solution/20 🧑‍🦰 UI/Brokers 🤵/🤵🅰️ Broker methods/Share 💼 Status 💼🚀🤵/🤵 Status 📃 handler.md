# 🤵 Status 📃 handler

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Status@Broker` 🅰️ method](<🤵 Status 🚀 request.md>).

## Handler

```yaml
# Verify the Consumer message
- VERIFY|$.Msg

# Get the Token
- READ >> $token:
    Set: BrokerTokens
    Key: $.Msg.Token

# Check the trust
- TRUSTS|$.Msg.From:
    Schema: $token.Schema
    Role: CONSUMER

# Return the Status
- REEL:
    Status: $token.Status
    Starting: $token.Starting
    Ending: $token.Ending
    Locator: $token.Locator
```