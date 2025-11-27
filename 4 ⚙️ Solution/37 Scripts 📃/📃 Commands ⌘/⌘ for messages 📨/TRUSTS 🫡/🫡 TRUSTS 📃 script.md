# 😃📃 `.TRUSTS` 🫡 script

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`TRUSTS`](<🫡 TRUSTS ⌘ cmd.md>) command.

> Calls the [`Trusts@Graph` 🅰️ method](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>)

## How to call

```yaml
- RUN|.TRUSTS:
    Schema: my-schema
    Trusted: trusted-entity.dom
    Truster: optional-truster.dom   # Optional
    Role: CONSUMER                  # Optional
```

## Script 

```yaml
📃 .TRUSTS:

# Default inputs
- DEFAULT|$.Inputs:
    Truster: $.Msg.To 
    Role: *

# Assert inputs
- ASSERT|$.Inputs:
    AllOf: Schema, Trusted
    Texts: Schema, Trusted, Truster
    Role.IsIn: VAULT, CONSUMER, *

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
- ASSERT|$answer:
    Trusted: True
```

Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`DEFAULT`](<../../⌘ for holders 🧠/DEFAULT 📭/📭 DEFAULT ⌘ cmd.md>) [`SEND`](<../SEND 📬/📬 SEND ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Trusts@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts/🕸 Trusts 🚀 call.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Msg`](<../../../📃 Holders 🧠/System holders 🔩/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`$.Hosted`](<../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|
