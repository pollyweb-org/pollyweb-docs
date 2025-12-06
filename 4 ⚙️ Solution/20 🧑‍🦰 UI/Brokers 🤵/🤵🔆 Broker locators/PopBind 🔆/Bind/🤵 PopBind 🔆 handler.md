# 🤵 PopBind 🔆 handler

> About
* Pop-up menu for a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)

<br/>

## Diagram

![alt text](<🤵 PopBind ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 PopBind:

# Assert the inputs
- ASSERT:
    $.Chat.Wallet: 
    $.Chat.Inputs.Bind:

# Get the Bind
- SELECT >> $bind:
    From: Broker.Binds
    Where: 
        ID: $.Chat.Inputs.Bind
        Wallet: $.Chat.Wallet

# Show info about the bind
- INFO|Bind: ´{$bind.Title}´

# Add general options
- IF|$bind.State.IsIn(ACTIVE, REMOVED):
    PUT +> $options: /Tag Bind

# Add options of active binds
- IF|$bind.State.Is(ACTIVE):
    PUT +> $options: /Remove Bind

# Exit if there are no options available
- IFNOT|$options:
    RETURN

# Show the options
- ONE:
    Title: What do you need?
    Options: $options

# Handle the selection
- CASE >> $handler:
    Tag: PopBindTag
    Remove: PopBindRemove

# Handle the selection
- RUN|$handler: $bind
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`IFNOT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IFNOT ⤵️/⤵️ IFNOT ⌘ cmd.md>) [`INFO`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Status ⚠️ prompts/INFO ℹ️/INFO ℹ️ prompt.md>) [`ONE`](<../../../../../37 Scripts 📃/📃 Prompts 🤔/🤔 Input ✏️ prompts/ONE 1️⃣/ONE 1️⃣ prompt.md>) [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SELECT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/SELECT 🅾️/🅾️ SELECT ⌘ cmd.md>)
| [Holders 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Chat`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) 
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds`](<../../../🤵🪣 Broker tables/Binds 🔗 table/🪣 Binds/🤵 Broker.Binds 🪣 table.md>)