# 🤗📃 Prompt Emoji script

> Purpose
* Calculates an emoji for a [Prompt 🤔](<../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)
* Implements the logic in [Input emojis 😶 ](<../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/😶 Input emojis.md>)


> Called by
* [`.PROMPT` 📃 script](<../../../../35 💬 Chats/Talkers 😃/😃⏩ Talker flows/Send Prompts 😃⏩🧑‍🦰/😃 Prompts 📃 script.md>)

## Script

```yaml
📃 PromptEmoji:

# Assert inputs
- ASSERT|$.Inputs:
    AllOf: Format, Role
    Text: Format, Role, PromptEmoji, ChatEmoji

# Set the emoji
- CASE|$Format:

    TEMP: RETURN|⏳

    FAILURE: RETURN|❌

    INFO: 
        CASE|$Role:
            VAULT: RETURN|ⓘ
            $: RETURN|ℹ️

    SUCCESS: 
        CASE|$Role:
            VAULT: RETURN|☑️
            $: RETURN|✅

    TEXT:
        CASE|$Role:
            VAULT: RETURN|💭
            $: RETURN|💬

    $: 
        # Agents always ask with 🫥
        - IF|$Role.Is(VAULT):
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
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`CASE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`EVAL`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/EVAL 🧮/🧮 EVAL ⌘ cmd.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RETURN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) 
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`{.IsIn}`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.IsIn}.md>) [`{.Is}`](<../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/🔩 {.Is}.md>)
|