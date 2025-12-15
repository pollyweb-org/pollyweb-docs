# 😃📃 `.ASK` script

> Purpose
 
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`ASK` command](<🙋 ASK ⌘ cmd.md>)

## Flow

![alt text](<🙋 ASK ⚙️ uml.png>)

## How to call

Here are the outputs of the [`Parse@Hosted` 🚀 call](<../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 call.md>)

```yaml
- RUN .ASK:
    Options:
      - A: option-1
        B: Option One
    ID: A
    Title: B
    Text: Any statement
```

## Script

Here's the [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>)

```yaml
📃 .ASK:

# Assert the inputs
- ASSERT $.Inputs:
    AllOf: Options, ID, Title
    Lists: Options
    Texts: ID, Title, Text

# Format the options into {ID,Title}
- PUT $Options >> $options:
    ID: {$ID}
    Title: {$Title}

# Ask the user to select
- MANY >> $result:
    Text: $Text
    Options: $options

# Match the selected options
- SELECT >> $selected:
    From: $Options
    Where: $$ID.IsIn($result.ID)

# Return the list of items selected.
- RETURN: $selected
```

Uses||
|-|-
|[Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CALL`](<../../⌘ for async/CALL 🧮/🧮 CALL ⌘ cmd.md>) [`MANY`](<../../../📃 Prompts 🤔/🤔 Input ✏️ prompts/MANY 🔠/🔠 MANY ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) 
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>)

---
<br/>