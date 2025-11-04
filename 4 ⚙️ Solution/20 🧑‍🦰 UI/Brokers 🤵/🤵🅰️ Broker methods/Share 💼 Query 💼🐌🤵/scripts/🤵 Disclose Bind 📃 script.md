# 🤵 Disclose Bind 📃 script

> Part of [`Query` 📃 handler](<../🤵 Query 📃 handler.md>)

## Script

```yaml
# Assert the inputs
- ASSERT|.Inputs:
    AllOf: chat, Domain, Bind

# Send the message to the vault
- SEND:
    Header:
        From: $Domain
        Subject: Disclose@Vault
        
    Body:
        Chat: $chat.ID
        Consumer: $.Msg.From
        Language: $chat.Language
        Bind: $Bind
```

Uses||
|-|-
|{{Commands}}| {{ASSERT}} {{SEND}}
|{{Holders}} | {{.Inputs}}