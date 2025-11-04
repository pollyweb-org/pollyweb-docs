
```yaml


# Assert the inputs
- ASSERT:
    AllOf: $trusted, $schema

# Find a matching Token
- EVAL|$trusted >> $tokens:
    WHERE 
        Schema: $schema
        Type: TOKEN

# Send if it's the only one.
- IF|$tokens.IsOne:
    - RUN|Disclose-Bind:
        $chat, 
    - BREAK


# If more than one, ask for selection
- IF|$trusts.AreMany:
    - ONE >> $vault:
        Text: Which vault to use?
        Options: 


```