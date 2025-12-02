# 🤗 OnPromptReplied 🔔 handler

> About
* Reacts to the [`Reply@Host` 📃 handler](<../../../🤗🅰️ Host methods/Reply 🧑‍🦰🐌🤗/🤗 Reply 📃 handler.md>)

<br/>

## Diagram

![alt text](<🤗 OnHostPromptReplied ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnPromptReplied:

# Continue the caller script
- CASE|$Prompt.OnReply:

    RACE: # There's a WAIT command pending
        RACE|$Prompt.ID:
            $Prompt.Answer

    REEL: # There's a HOOK return-point set
        REEL|$Prompt.ID:
            $Prompt.Answer
```