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

```yaml
📃 OnPromptEmoji:

# Set the emoji
- CASE|$Prompt.Format:

    TEMP: RETURN|⏳

    FAILURE: RETURN|❌

    INFO: 
        CASE|$Prompt.Role:
            VAULT: RETURN|ⓘ
            $: RETURN|ℹ️

    SUCCESS: 
        CASE|$Prompt.Role:
            VAULT: RETURN|☑️
            $: RETURN|✅

    TEXT:
        CASE|$Prompt.Role:
            VAULT: RETURN|💭
            $: RETURN|💬

    $: 
        # Agents always ask with 🫥
        - IF|$Prompt.Role.Is(VAULT):
            RETURN|🫥

# Default emoji
- PUT|😃 >> $emoji

# Override if in Chat
- IF|$ChatEmoji:
    PUT|$ChatEmoji >> $emoji

# Override if in Prompt
- IF|$PromptEmoji: 
    PUT|$PromptEmoji >> $emoji

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
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`CALL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`{.IsIn}`](<../../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/IsIn ⓕ any.md>) [`{.Is}`](<../../../../../37 Scripts 📃/📃 Holders 🧠/Any 📚 holders/Is ⓕ any.md>)
|