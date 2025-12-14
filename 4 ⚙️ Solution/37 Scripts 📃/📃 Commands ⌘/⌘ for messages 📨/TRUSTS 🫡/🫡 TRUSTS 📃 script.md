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
    Texts: Schema, Trusted, Truster
    Role.IsIn: VAULT, CONSUMER, ANY

# Send the request
- SEND >> $answer:
    Header:
        To: $.Hosted.Graph
        Subject: Trusted@Graph
    Body:
        Truster: $Truster
        Trusted: $Trusted
        Role: $Role
        Schema: $Schema

# Assert if it's trusted
- ASSERT $answer:
    Trusted: True
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DEFAULT`](<../../⌘ for holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>) [`SEND`](<../SEND 📬/📬 SEND ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`$.Hosted`](<../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/▶️ $.Inputs 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Trusts@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸📨 Graph msgs/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>)
|
