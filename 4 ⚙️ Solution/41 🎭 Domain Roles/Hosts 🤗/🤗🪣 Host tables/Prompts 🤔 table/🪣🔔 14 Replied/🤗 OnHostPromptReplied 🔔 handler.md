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
- REEL|$Prompt.ID:
    $Prompt.Result
    $Prompt.Answer
```