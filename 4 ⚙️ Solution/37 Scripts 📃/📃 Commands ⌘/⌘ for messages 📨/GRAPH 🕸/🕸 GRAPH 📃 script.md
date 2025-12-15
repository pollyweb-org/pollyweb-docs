# 🕸 GRAPH 📃 script 

> About
* Invokes methods on a [Graph 🕸 domain](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸 Graph helper/🕸🤲 Graph helper.md>)
* Implements the [`GRAPH`](<🕸 GRAPH ⌘ cmd.md>) command

<br/>


## Diagram

![alt text](<🕸 GRAPH ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .GRAPH >> $response:
    Subject: About
    Error: Domain not found
    Payload: 
        Domain: any-domain.dom
```
Uses: [`RUN`](<../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)

<br/>

## Script

```yaml
📃 .GRAPH: 

# Assert the inputs
- ASSERT $.Inputs:
    Error: Invalid GRAPH inputs
    AllOf: Subject, Payload
    Texts: Subject, Error

# Assert the Subject is valid
- ASSERT $.Inputs:
    Error: Invalid Graph subject 
    Subject.IsIn: About, Form, PublicKey, Schema, Trusts

# Assert the Hosted Graph configuration
- ASSERT $.Hosted:
    Error: Invalid Hosted Graph setup
    AllOf: Graph
    Graph.IsDomain:  

# Call the Graph domain 
- SEND >> $response:
    Header: 
        To: $.Hosted.Graph
        Subject: '{$Subject}@Graph'
    Body: 
        $Payload

# Customize error messages
- CASE $Subject >> $msg:
    Form: Unknown form
    About: Unknown domain
    Schema: Unknown schema
    Trusts: Unknown domain(s)
    PublicKey: Unknown domain or DKIM
    $: Empty Graph response

# Fail if not found
- ASSERT $response:
    Error: 
        $Error.Default: $msg

# Return
- RETURN: $response
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SEND`](<../SEND 📬/📬 SEND ⌘ cmd.md>)
| [{Functions} 🐍](<../../../../35 💬 Chats/Scripts 📃/Function 🐍.md>) | [`.IsIn`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/IsIn ⓕ.md>) [`.IsDomain`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/IsDomain ⓕ.md>) [`.Minus`](<../../../📃 Functions 🐍/🐍 System 🔩 functions/Minus ⓕ.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>)
|
