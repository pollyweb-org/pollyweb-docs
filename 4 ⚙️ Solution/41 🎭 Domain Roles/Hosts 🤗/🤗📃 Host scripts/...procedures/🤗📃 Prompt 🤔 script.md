
```yaml
📃 Prompt@Host:

# Save the prompt.
- SAVE|Prompts@Host >> $prompt:
    Prompt: .UUID
    PublicKey: $.Chat.PublicKey
    Prompted:
        Format: $:Format
        Statement: $:Statement
        Options: $:Options
        Details: $:Details
        Appendix: $:Appendix    

# Send it to the Broker.
- SEND:
    To: $.Chat.Broker
    Subject: Prompt@Broker
    Chat: $.Chat.Chat
    Prompt: $saved.Prompt
    TTL: 

- WAIT
```