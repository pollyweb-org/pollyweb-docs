# 🗄️ OnBindBound 📃 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the [`Bound@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>).
* Returns a [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) item to the [`BIND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) command.
 
<br/>

## Diagram

![alt text](<🗄️ OnBindBound ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindBound:

# Assert the inputs
- ASSERT|$Bind:
    AllOf: Answer
    Answer.IsIn: ACCEPTED, DECLINED

# Return the call
- CASE|$Bind.Answer:

    ACCEPTED: # Return the Bind if accepted
        REEL|$Bind.ID:
            $Bind

    DECLINED: # Return empty if declined
        REEL|$Bind.ID
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`REEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>)
|