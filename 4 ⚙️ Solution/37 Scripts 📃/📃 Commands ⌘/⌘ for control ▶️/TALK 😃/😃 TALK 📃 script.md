<!-- TODO -->

## Script

```yaml
# Get the handler
- READ >> $talker:
    Set: Talker.Handlers
    Key: 
        Domain: $.Hosted.Domain
        Schema: $.Chat.Schema

# Run the script
- RUN|$talker.Script
```