# 🤵 Send Binds 📃 script.md

## Script

```yaml
📃 Send Binds:

# Merge existing with new
- PUT >> $send:
    $bound # already bound
    $binds # just created

# Send the created binds
- SEND:
    Header: 
        To: $.Msg.From
        Subject: Bound@Vault
    Body:
        Hook: $.Msg.Hook
        Binds: $send
```