```yaml
# Assert the inputs
- ASSERT:
    AllOf: $trusted, $schema

# Find a matching Token
- FILTER|$trusted >> $tokens:
    Schema: $schema
    Type: TOKEN

# Leave if there's no Token for the Schema 
- IF|$tokens.IsEmpty:
    - RETURN

# Set the prompt question
- CASE|$tokens.AreMany >> $text:
    False: Share {$tokens.First.Schema} token?
    True: Which {$tokens.First.Schema} tokens to share?

- IF|$tokens.AreMany >> $options:

# Send if it's the only one.
- IF|$tokens.IsOne:
    - RUN|Disclose-Bind:
        $chat, 
    - BREAK

```
Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>)| [`FILTER`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/FILTER 🔽/🔽 FILTER ⌘ cmd.md>)