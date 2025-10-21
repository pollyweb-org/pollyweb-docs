# 🤵📃 Update Domain 🪣

> Used by:
* [`Offer` 📃 script](<../...handlers/🤵📃 Offer 🎫 handler.md>)

<br/>

## Script

```yaml
📃 UpdateDomain:

# Ensure the parameters are given
- ASSERT:
    - $1.Domain
    - $1.Domain$

# Try to get the domain, if it exists
- GET >> $domain:
    Pool: Domains@Broker
    Key: $1.Domain
    Default: 
        Domain: $1.Domain

# Change the translation
- EVAL|$domain:
    Domain$: $1.Domain$

# Update the table
- SAVE|$domain
```

Commands: [`ASSERT`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/ASSERT 🚦.md>) [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/EVAL ⬇️ flow.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) 