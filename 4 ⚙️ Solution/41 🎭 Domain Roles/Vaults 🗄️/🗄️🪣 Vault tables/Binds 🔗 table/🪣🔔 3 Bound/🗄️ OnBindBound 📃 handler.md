# 🗄️ OnBindBound 📃 handler

> Purpose
* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that reacts to the [`Bound@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>).
 
<br/>

## Diagram

![alt text](<🗄️ OnBindBound ⚙️ uml.png>)

<br/>

## Script

```yaml
📃 OnBindBound:

# Assert the inputs
- ASSERT|$Bind:
    - AllOf: Answer
    - Answer.IsIn(ACCEPTED, DECLINED)

# Return the call
- REEL|$Bind.ID:
    $Bind.Answer.Is(ACCEPTED)
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`REEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/REEL 🎣/🎣 REEL ⌘ cmd.md>)
|