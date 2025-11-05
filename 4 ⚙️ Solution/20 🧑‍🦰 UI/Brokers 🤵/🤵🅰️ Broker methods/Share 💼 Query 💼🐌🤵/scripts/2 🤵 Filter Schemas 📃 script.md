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
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>) | [`ASSERT`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`IF`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PARALLEL`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/PARALLEL *️⃣/*️⃣ PARALLEL ⌘ cmd.md>) [`RETURN`](<../../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`SEND`](<../../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>)
| [Placeholder 🧠](<../../../../../35 💬 Chats/Scripts 📃/📃 basics/Holder 🧠.md>)  | [`$.Msg`](<../../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>)
| [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Trusts@Graph`](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Trusts.md>)
|