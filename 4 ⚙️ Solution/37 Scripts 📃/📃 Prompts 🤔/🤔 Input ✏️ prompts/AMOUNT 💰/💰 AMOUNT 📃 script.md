# 💰 AMOUNT 📃 script

## Script

```yaml
📃 .AMOUNT:

# Send the prompt to the user
- RUN|.PROMPT >> $reply:
    $.Inputs

# Return the reply.
- RETURN|$reply
```