# 😃📃 `.DELETE` 🗑️ script

> Implements the [`DELETE`](<🗑️ DELETE ⌘ cmd.md>) command

> Invokes the [`Delete@Itemizer` 🚀 call](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢📨 Itemizer msgs/Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>)


## How to call

```yaml
# 📃 With multiple parameters
- RUN .DELETE >> $deleted:
    Set: MySet
    Key: [Key1, Key2]
    Script: MyScript    
    Undo: 30 days # Optional
```

```yaml
# 📃 With an item
- RUN .DELETE >> $deleted:
    Set: $item.Set
    Key: $item.Key
    Script: MyScript 
    Undo: 30 days # Optional
```

## Script

```yaml
📃 .DELETE:

# Fill the $item
- ASSERT $.Inputs:
    AllOf: Set, Key
    Texts: Set
    Lists: Key, Undo, Script

# Send the request and wait.
- SEND >> $deleted:
    Header:
        To: $.Hosted.Itemizer
        Subject: Delete@Itemizer
    Body:
        Set: $Set
        Key: $Key
        Undo: $Undo
        Script: $Script

# Return the deleted object
- RETURN: $deleted
```


Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Delete@Itemizer`](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢📨 Itemizer msgs/Item Delete 👥🚀🛢/🛢 Delete 🚀 call.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Hosted`](<../../../📃 Holders 🧠/System holders 🔩/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>) [`$.Inputs`](<../../../📃 Holders 🧠/System holders 🔩/$.Inputs 🏃/🏃 $.Inputs 🧠 holder.md>)
|