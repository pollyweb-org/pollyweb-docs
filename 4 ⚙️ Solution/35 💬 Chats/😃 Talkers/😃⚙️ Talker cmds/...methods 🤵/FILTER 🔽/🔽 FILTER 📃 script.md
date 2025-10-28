# 😃📃 `.FILTER` 🔽 script

> Purpose
 
* [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>) that implements the [`FILTER` 🔽 command](<🔽 FILTER ⌘ cmd.md>)

## Flow

![alt text](<🔽 FILTER ⚙️ uml.png>)

## How to call

Here are the outputs of the [`Parse@Hosted` 🅰️ method](<../../../../../55 👷 Build domains/Hosteds 📦/📦🅰️ Hosted methods/Parse 😃🚀📦/📦 Parse 🚀 request.md>)

```yaml
- RUN|.FILTER:
    Options:
      - A: option-1
        B: Option 1
    ID: A
    Title: B
    Text: Any statement
```

## Script

Here's the [Script 📃](<../../...commands ⌘/Script 📃/📃 Script.md>)

```yaml
📃 .FILTER:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: Options, ID, Title
    Lists: Options
    Texts: ID, Title, Text

# Format the options into {ID,Title}
- EVAL|$:Options >> $options:
    ID: {$:ID}
    Title: {$:Title}

# Ask the user to select
- MANY >> $result:
    Text: $:Text
    Options: $options

# Match the selected options
- EVAL|$result >> $selected:
    FROM $:Options
    MATCH ID, $:Options.{$:ID}

# Return the list of items selected.
- RETURN|$selected
```

Commands: [`ASSERT`](<../../...holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`EVAL`](<../../...holders 🧠/EVAL ⬇️/⬇️ EVAL ⌘ cmd.md>) [`MANY`](<../../../../🤔 Prompts/🤔✏️ Prompt inputs/MANY 🔠/🔠 MANY ⌘ cmd.md>) [`RETURN`](<../../...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../...control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)

---
<br/>