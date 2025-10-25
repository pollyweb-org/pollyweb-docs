# 😃📃 `.UNDO` ↩️ script

> Implements the [`UNDO`](<../UNDO ↩️.md>) command

> Invokes the [`Undo@Itemizer` 🅰️ method](<../../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Undo.md>)

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
- ASSERT:
    AllOf: $:Set, $:Key
    Texts: $:Set
    Lists: $:Key

# Send the request and wait.
- SEND >> $undone:
    Header:
        To: $.Settings.Itemizer
        Subject: Undo@Itemizer
    Body:
        Set: $:Set
        Key: $:Key
        Script: $:Script
```


Needs||
|-|-
| [Commands ⌘](<../../../...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`SEND`](<../../../...messages 📨/SEND 📬 msg.md>) [`RUN`](<../../../...control ▶️/RUN ▶️/RUN ▶️.md>)
| [Messages 📨](<../../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Undo@Itemizer` 🅰️ method](<../../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Undo.md>)
| [Placeholders 🧠](<../../../...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Settings`](<../../../...messages 📨/$.Settings 🎛️.md>)
|