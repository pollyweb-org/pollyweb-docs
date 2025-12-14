# 🔐 Talker `VERIFY` Schema 🧩

> About
* Part of the [`VERIFY` ⌘ command](<../🔐 VERIFY ⌘ cmd.md>)

<br/>

## Diagram

![alt text](<🔐 VERIFY Schema ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .VERIFY-Schema:
    Data: {...}
    Schema: any-authority.dom/ANY/SCHEMA:1.0.0
```

## Script 

```yaml
📃 .VERIFY-Schema:

# Assert the data structure
- ASSERT $.Inputs:
    AllOf: Schema        # Allows for empty data
    Schema.IsSchema:     # Valid schema code

# Get the schema definition
- GRAPH Schema >> $definition:
    Schema: $Schema

# Assert that the Data matches the Schema definition
- ASSERT: 
    $Data.Conforms: $definition   
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`GRAPH`](<../../GRAPH 🕸/🕸 GRAPH ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Conforms`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/Conforms ⓕ.md>) [`.IsSchema`](<../../../../📃 Functions 🐍/🐍 System 🔩 functions/IsSchema ⓕ.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) |  [`$.Inputs`](<../../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
