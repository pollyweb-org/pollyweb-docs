```yaml
📃 OnQueryDetailed:

# Load the Chat
- CHAT|$Query.Chat

# Stop if no candidates are available.
CASE|$Query.Candidates.Length:
    0: 
        - SAVE|$Query:
            Status: SUGGEST
    1: 
        - CONFIRM|Share?:
```