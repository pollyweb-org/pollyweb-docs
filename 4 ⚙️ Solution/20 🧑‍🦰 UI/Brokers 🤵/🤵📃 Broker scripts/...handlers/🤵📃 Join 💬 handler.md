# 🤵📃 Join

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/📃 Script.md>) that implements the [`Join@Broker`](<../../🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Join.md>) method.

## Script

```yaml
📃 Join@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    - One: Chat, Host, Token, Issuer, Bind, Vault
    - Uuid: Chat, Token, Bind
    - Text: Host, Issuer, Vault
```