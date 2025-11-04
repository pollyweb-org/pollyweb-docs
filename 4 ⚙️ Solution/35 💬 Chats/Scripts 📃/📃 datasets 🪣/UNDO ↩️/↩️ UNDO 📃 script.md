# 😃📃 `.UNDO` ↩️ script

> Implements the [`UNDO`](<↩️ UNDO ⌘ cmd.md>) command

> Invokes the [`Undo@Itemizer` 🅰️ method](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Undo 👥🚀🛢/🛢 Undo 🚀 request.md>)

## How to call

```yaml
# With an item
- RUN|.DELETE:
    Set: $deleted.Set
    Key: $deleted.Key
    Script: MyScript 
```

## Script

```yaml
📃 .UNDO:

# Fill the $item
- ASSERT|$.Inputs:
    AllOf: Set, Key
    Texts: Set
    Lists: Key

# Send the request and wait.
- SEND >> $undone:
    Header:
        To: $.Hosted.Itemizer
        Subject: Undo@Itemizer
    Body:
        Set: $Set
        Key: $Key
        Script: $Script
```


Uses||
|-|-
| [Commands ⌘](<../../📃 basics/Command ⌘.md>) | [`ASSERT`](<../../📃 holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RUN`](<../../📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Undo@Itemizer` 🅰️ method](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Undo 👥🚀🛢/🛢 Undo 🚀 request.md>)
| [Holders 🧠](<../../📃 basics/Holder 🧠.md>) | [`$.Hosted`](<../../📃 holders 🧠/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
|