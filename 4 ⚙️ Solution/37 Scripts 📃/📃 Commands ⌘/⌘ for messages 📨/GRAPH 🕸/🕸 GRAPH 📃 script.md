# 🕸 GRAPH 📃 script 

> About
* Invokes methods on a [Graph 🕸 domain](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>)
* Implements the [`GRAPH`](<🕸 GRAPH ⌘ cmd.md>) command

<br/>


## Diagram

![alt text](<🕸 GRAPH ⚙️ uml.png>)

<br/>


## Script

```yaml
📃 .GRAPH: 

# Assert the inputs
- ASSERT $.Inputs:
    AllOf: Subject, Payload
    Texts: Subject
    Subject.IsIn: About, PublicKey, Schema, Trusts

# Assert the Hosted Graph configuration
- ASSERT $.Hosted:
    AllOf: Graph
    Graph.IsDomain:  

# Call the Graph domain 
- SEND >> $response:
    Header: 
        To: $.Hosted.Graph
        Subject: '{$Subject}@Graph'
    Body: $Payload

# Return
- RETURN: $response
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SEND`](<../SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsIn`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.IsDomain`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>)
|
