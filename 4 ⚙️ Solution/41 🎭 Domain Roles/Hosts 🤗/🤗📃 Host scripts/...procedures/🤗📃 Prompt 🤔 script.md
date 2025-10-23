
```yaml
📃 Prompt

# Save the prompt.
- SAVE|Prompts@Host >> $prompt:

    # Hook
    Prompt: .UUID
    PublicKey: $.Chat.PublicKey
    
    # Prompt
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