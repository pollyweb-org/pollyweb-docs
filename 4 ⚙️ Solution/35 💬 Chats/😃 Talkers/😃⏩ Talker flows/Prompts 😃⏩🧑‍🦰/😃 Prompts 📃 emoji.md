# 🤗📃 Prompt Emoji script

> Purpose
* Calculates an emoji for a [Prompt 🤔](<../../../Prompts 🤔/🤔 Prompt.md>)
* Implements the logic in [Input emojis 😶 ](<../../../Prompts 🤔/🤔✏️ Prompt input features/😶 Input emojis.md>)


> Called by
* [`.PROMPT` 📃 script](<😃 Prompts 📃 script.md>)

## Script

```yaml
📃 PromptEmoji:

# Assert inputs
- ASSERT|$.Inputs:
    AllOf: Format
    Text: Format, Emoji

# Set the emoji
- CASE|$:Format:

    TEMP: RETURN|⏳

    FAILURE: RETURN|❌

    INFO: 
        CASE|$.Chat.Role:
            AGENT: RETURN|ⓘ
            $: RETURN|ℹ️

    SUCCESS: 
        CASE|$.Chat.Role:
            AGENT: RETURN|☑️
            $: RETURN|✅

    TEXT:
        CASE|$.Chat.Role:
            AGENT: RETURN|💭
            $: RETURN|💬

    $: 
        # Agents always ask with 🫥
        - IF|$.Chat.Role.Is(AGENT):
            RETURN|🫥

# Default emoji
- EVAL|😃 >> $emoji

# Override if in Chat
- IF|$.Chat.Emoji:
    EVAL|$.Chat.Emoji >> $emoji

# Override if in Prompt
- IF|$:Emoji: 
    EVAL|$:Emoji >> $emoji

# Block special emojis
- IF|$:Emoji.In(⏳❌ⓘℹ️☑️✅😃🫥💬💭):
    RETURN|😃

# Allow limited customizations
- IF|$:Emoji.In(😐😶😌😊😕🙁😔🥺🤣😅✏️):
    RETURN|$:Emoji

# Default
- RETURN 😃
```

Needs ||
|-|-
| [Commands ⌘](<../../😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | [`CASE`](<../../😃⚙️ Talker cmds/...control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`EVAL`](<../../😃⚙️ Talker cmds/...holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`IF`](<../../😃⚙️ Talker cmds/...control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`RETURN`](<../../😃⚙️ Talker cmds/...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) 
| [{Functions} 🐍](<../../😃⚙️ Talker cmds/...functions 🐍/{Function} 🐍.md>) | [`{.In}`](<../../😃⚙️ Talker cmds/...functions 🐍/🔩 {.In}.md>) [`{.Is}`](<../../😃⚙️ Talker cmds/...functions 🐍/🔩 {.Is}.md>)
| [Holders 🧠](<../../😃⚙️ Talker cmds/...holders 🧠/$Holder 🧠.md>) | [`$.Chat`](<../../😃⚙️ Talker cmds/...holders 🧠/$.Chat 💬/💬 $.Chat 🧠 holder.md>)
|