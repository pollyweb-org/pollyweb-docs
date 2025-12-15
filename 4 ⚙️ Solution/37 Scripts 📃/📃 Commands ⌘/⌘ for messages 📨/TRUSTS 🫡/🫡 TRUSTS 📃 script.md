# 🫡 `.TRUSTS` 📃 script

> About
* [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`TRUSTS`](<🫡 TRUSTS ⌘ cmd.md>) command.
* Calls the [`Trusts@Graph` 🚀 call](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>)

<br/>

## Diagram

![alt text](<🫡 TRUSTS ⚙️ uml.png>)

<br/>

## How to call

```yaml
- RUN .TRUSTS:
    Error: Untrusted domain
    Schema: my-schema
    Trusted: trusted-entity.dom
    Truster: optional-truster.dom   # Optional
    Role: CONSUMER                  # Optional
```

## Script 

```yaml
📃 .TRUSTS:

# Default inputs
- DEFAULT $.Inputs:
    Truster: $.Msg.To 
    Role: ANY

# Assert inputs
- ASSERT $.Inputs:
    AllOf: Schema, Trusted
    Texts: Schema, Trusted, Truster, Error
    Role.IsIn: VAULT, CONSUMER, ANY

# Send the request
- GRAPH Trusted >> $answer:
    Truster: $Truster
    Trusted: $Trusted
    Role: $Role
    Schema: $Schema

# Assert if it's trusted
- ASSERT $answer:
    Error: $Error
    Trusted: True
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DEFAULT`](<../../⌘ for holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>) [`GRAPH`](<../GRAPH 🕸/🕸 GRAPH ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Trusts@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>)
|
