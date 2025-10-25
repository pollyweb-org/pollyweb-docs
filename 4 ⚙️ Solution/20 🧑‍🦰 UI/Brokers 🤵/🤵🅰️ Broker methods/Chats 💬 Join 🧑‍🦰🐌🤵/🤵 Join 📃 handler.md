# 🤵📃 Join

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Join@Broker`](<🤵 Join 🐌 msg.md>) method.

## Script

```yaml
📃 Join@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    - One: Chat, Host, Token, Issuer, Bind, Vault
    - Uuid: Chat, Token, Bind
    - Text: Host, Issuer, Vault
```