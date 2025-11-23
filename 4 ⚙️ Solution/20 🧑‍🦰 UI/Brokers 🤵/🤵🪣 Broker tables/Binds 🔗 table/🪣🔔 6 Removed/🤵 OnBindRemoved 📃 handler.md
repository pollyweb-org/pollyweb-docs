# 🤵 OnBindRemoved 📃 handler

> Purpose

* [Script 📃](<../../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that plans the [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to be deleted in a random future.
  
## Diagram

![alt text](<🤵 OnBindRemoved ⚙️ uml.png>)

## Script

```yaml
📃 OnBindRemoved:
    
# Schedule a random deletion time for the Bind
#  to block Vaults from guessing why users unbound
- PUT >> $hrs:
    .Random(1,90)

# Save the bind
- SAVE|$Bind:
    .Delete: .Now.Add({$hrs} hours)  
```

Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`PUT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PUT ⬇️/⬇️ PUT ⌘ cmd.md>) [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>)
|[Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Broker.Binds` 🪣 table](<../🪣 Binds/🤵 Broker.Binds 🪣 table.md>)
| [{Functions} 🐍](<../../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.Now`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Now ⓕ.md>) [`.Add`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Add ⓕ.md>) [`.Random`](<../../../../../37 Scripts 📃/📃 Functions 🐍/🐍 System 🔩 functions/Random ⓕ.md>) 
|

<!-- Verify the functions translations -->