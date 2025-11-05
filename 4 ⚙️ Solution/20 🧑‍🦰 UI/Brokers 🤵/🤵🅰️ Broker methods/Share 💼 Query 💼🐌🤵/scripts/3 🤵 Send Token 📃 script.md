```yaml
# Assert the inputs
- ASSERT:
    AllOf: $trusted, $schema
    Lists: $trusted
    Texts: $schema

# Assert the list items
- ASSERT|$trusted:
    AllOf: Schema, Schema$, Domain, Type, ID
    UUIDs: ID
    Texts: Schema, Schema$, Domain, Type

# Assert the expected types
- ASSERT|$trusted.Type:
    Enum: TOKEN, BIND

# Find a matching Token
- FILTER|$trusted >> $tokens:
    Schema: $schema
    Type: TOKEN

# Leave if there's no Token for the Schema 
- IF|$tokens.IsEmpty:
    - RETURN

# Ask for confirmation if there is only one
- IF|$tokens.IsOne:
    - EVAL|$tokens.First >> $token
    - CONFIRM|Share {$token.Schema} token?

# Ask for selection if there are many
- IF|$tokens.AreMany:
    ONE|Which {$tokens.First.Schema} token to share?:
            Options: 

# Send the token.
- RUN|Disclose-Bind:
    $chat, ..

- RETURN ...
```
Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`FILTER`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/FILTER 🔽/🔽 FILTER ⌘ cmd.md>)