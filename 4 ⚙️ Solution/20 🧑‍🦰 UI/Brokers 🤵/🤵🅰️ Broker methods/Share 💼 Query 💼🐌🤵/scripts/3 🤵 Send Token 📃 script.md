```yaml
# Assert the inputs
- ASSERT:
    AllOf: $trusted
    Lists: $trusted

# Assert the list items
- ASSERT|$trusted:
    - AllOf: Schema, Schema$, Domain, Type, ID
    - UUIDs: ID
    - Texts: Schema, Schema$, Domain, Type
    - Type.IsIn(TOKEN,BIND)

# Get all tokens
- FILTER|$trusted >> $tokens:
    Type: TOKEN

# Leave if there are no Tokens
- IF|$tokens.IsEmpty:
    - RETURN

# Get the schema title
- TRANSLATE >> $title:
    Schema: $schema

# Ask for confirmation if there is only one
- IF|$tokens.IsOne:
    - CONFIRM|Share {$title} token?

# Ask for selection if there are many
- IF|$tokens.AreMany:
    ASK: 
        Text: Which {$title} token to share?
        Options: $tokens
        ID: ID


# Send the token.
- RUN|Disclose-Bind:
    $chat, ..

- RETURN ...
```
Uses||
|-|-
|[Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)| [`ASK`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/ASK 🙋/🙋 ASK ⌘ cmd.md>) [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`FILTER`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/FILTER 🔽/🔽 FILTER ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsEmpty`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍🧠 Holder functions/🔩 {Holder.IsEmpty}.md>) [`.IsOne`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍🧠 List functions/🔩 {List.IsOne}.md>)  [`.AreMany`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.AreMany}.md>) 
|