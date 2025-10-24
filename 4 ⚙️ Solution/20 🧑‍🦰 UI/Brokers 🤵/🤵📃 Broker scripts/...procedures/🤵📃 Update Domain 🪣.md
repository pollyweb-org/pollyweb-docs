# 🤵📃 Update Domain 🪣

> Used by:
* [`Offer` 📃 script](<../...handlers/🤵📃 Offer 🎫 handler.md>)

<br/>

## Script

```yaml
📃 UpdateDomain:

# Ensure the parameters are given
- ASSERT:
    AllOf: !Domain, !Domain$
    Texts: !Domain, !Domain$

# Try to get the domain, if it exists
- GET >> $domain:
    Set: Domains@Broker
    Key: !Domain
    Default: 
        Domain: !Domain

# Change the translation
- EVAL|$domain:
    Domain$: !Domain$

# Update the table
- SAVE|$domain
```

Commands: [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/ASSERT 🚦.md>) [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/EVAL ⬇️ flow.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬ item.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE 💾 item.md>) 