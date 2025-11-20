# 🤵 OnPromptInserted 📃 handler

> Purpose
* Calculates an emoji for a [Prompt 🤔](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)
* Implements the logic in [Input emojis 😶 ](<../../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/😶 Input emojis.md>)
  

## Script

```yaml
📃 OnPromptInserted:

# Set the emoji
- RUN|OnPromptEmoji >> $emoji:
    $Prompt

# Update the Prompt with the emoji
- SAVE|$Prompt:
    .State: Emojied
    Emoji: $emoji
```
Uses: [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 

```yaml
📃 OnPromptEmoji:

# Verify the Prompt
- ASSERT|$Prompt:
    AllOf: Format
    Texts: Format, Emoji

# Verify the Prompt's Chat
- ASSERT|$Prompt.Chat:
    Text: Emoji

# Verify the Prompt's Chatter
- ASSERT|$Prompt.Chatter:
    AllOf: Role
    Text: Role

# Set the emoji
- CASE|$Prompt.Format:

    TEMP: RETURN|⏳

    FAILURE: RETURN|❌

    INFO: 
        CASE|$Prompt.Chatter.Role:
            VAULT: RETURN|ⓘ
            $: RETURN|ℹ️

    SUCCESS: 
        CASE|$Prompt.Chatter.Role:
            VAULT: RETURN|☑️
            $: RETURN|✅

    TEXT:
        CASE|$Prompt.Chatter.Role:
            VAULT: RETURN|💭
            $: RETURN|💬

    $: 
        # Agents always ask with 🫥
        - IF|$Prompt.Chatter.Role.Is(VAULT):
            RETURN|🫥

# Default emoji
- PUT|😃 >> $emoji

# Override if in Chat
- IF|$Prompt.Chat.Emoji:
    PUT|$Prompt.Chat.Emoji >> $emoji

# Override if in Prompt
- IF|$Prompt.Emoji: 
    PUT|$Prompt.Emoji >> $emoji

# Block special emojis
- IF|$emoji.IsIn(⏳❌ⓘℹ️☑️✅😃🫥💬💭):
    RETURN|😃

# Allow limited customizations
- IF|$emoji.IsIn(😐😶😌😊😕🙁😔🥺🤣😅✏️):
    RETURN|$emoji

# Default
- RETURN 😃
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`{.IsIn}`](<../../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/IsIn ⓕ any.md>) [`{.Is}`](<../../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/Is ⓕ any.md>)
|