# 🤵📃 Join

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements the [`Join@Broker`](<../../🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🐌🤵 Join.md>) method.

## Script

```yaml
📃 Join@Broker:

# Verify the required inputs
- ASSERT:
    - One:
        $.Msg.Chat
        $.Msg.Token
        Chat: <chat-uuid>
        Host: any-host.dom
        Token: <token-uuid>
        Issuer: any-issuer.dom
        Bind: <bind-uuid>
        Vault: any-vault.dom
```