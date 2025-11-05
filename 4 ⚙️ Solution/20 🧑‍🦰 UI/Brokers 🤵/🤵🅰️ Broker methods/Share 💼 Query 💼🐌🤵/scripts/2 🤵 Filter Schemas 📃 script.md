# 🤵 Filter Schemas 📃 script

> Part of the [`Query` 📃 handler](<../🤵 Query 📃 handler.md>)

> Returns `{Schema, Domain}[]`

## Script 

```yaml
📃 Merge-Schemas:

# Assert the inputs
- ASSERT|$.Inputs:
    AllOf: merged

# Filter by trusts
- PARALLEL|$merges|$merge:
    
    #Check the trust
    - SEND >> $trusts:
        Header:
            To: .Hosted.Graph
            Subject: Trusts@Graph
        Body:
            Schema: $merge.Schema
            Truster: $merge.Domain
            Trusted: $.Msg.From
            Role: CONSUMER

    # Add to the output
    - IF|$trusts.Trusted:
        EVAL|$merge +> $trusted
    
# Return the trusted
- RETURN:
    $trusted
```

|Uses||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IF`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PARALLEL`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`RETURN`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SEND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Placeholder 🧠](<../../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>)  | [`$.Msg`](<../../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Trusts@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>)
|