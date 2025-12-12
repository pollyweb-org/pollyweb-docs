# 🤵 OnPromptInserted 📃 handler

> About
* Part of the [`Broker.Prompts` 🪣 table](<../🪣 Prompts/🤵🤔 Broker.Prompts 🪣 table.md>)
* Reacts to the [`Prompt@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>)
* Calculates an emoji for a [Prompt 🤔](<../../../../../35 💬 Chats/Chats 💬/🤔 Prompt.md>)
* Implements the logic in [Input emojis 😶 ](<../../../../../35 💬 Chats/Prompts 🤔/🤔✏️ Prompt inputs/😶 Input emojis.md>)


<br/>

## Diagram

![alt text](<🤵 OnPromptInserted ⚙️ uml.png>)
  
<br/>

## Script

```yaml
📃 OnPromptInserted:

# Set the emoji
- RUN OnPromptEmoji >> $emoji:
    $Prompt

# Update the Prompt with the emoji
- SAVE $Prompt:
    .State: EMOJIED
    Emoji: $emoji
```
Uses: [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) 

```yaml
📃 OnPromptEmoji:

# Verify the Prompt
- ASSERT $Prompt:
    AllOf: Format, Role
    Texts: Format, Role, PromptEmoji, ChatEmoji

# Set the emoji
- CASE $Prompt.Format:

    TEMP: RETURN ⏳

    FAIL: RETURN ❌

    INFO: 
        CASE $Prompt.Role:
            VAULT: RETURN ⓘ
            $: RETURN ℹ️

    DONE: 
        CASE $Prompt.Role:
            VAULT: RETURN ☑️
            $: RETURN ✅

    TEXT:
        CASE $Prompt.Role:
            VAULT: RETURN 💭
            $: RETURN 💬

    $: 
        # Agents always ask with 🫥
        - IF:
            $Prompt.Role: VAULT
        - THEN:
            RETURN: 🫥

# Default emoji
- PUT: 😃 >> $emoji

# Override if in Chat
- IF $Prompt.ChatEmoji:
    PUT $Prompt.ChatEmoji >> $emoji

# Override if in Prompt
- IF $Prompt.PromptEmoji: 
    PUT $Prompt.PromptEmoji >> $emoji

# Block special emojis
- IF:
    $emoji.IsIn: ⏳❌ⓘℹ️☑️✅😃🫥💬💭
- THEN:
    RETURN: 😃

# Allow limited customizations
- IF:
    $emoji.IsIn: 😐😶😌😊😕🙁😔🥺🤣😅✏️
- THEN:
    RETURN: $emoji

# Default
- RETURN: 😃
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) 
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`{.IsIn}`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`{.Is}`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Is ⓕ.md>)
|