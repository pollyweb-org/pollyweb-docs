# 😃📃 `.SAVE` 🗑️ script

> Implements the [`SAVE`](<../SAVE 💾 item.md>)

> Invokes the [`Save@Itemizer`](<../../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Save.md>) method


## How to call

```yaml
# With multiple parameters
- RUN|.SAVE >> $saved:
    Item: {A:1, B:1}
    Set: MySet
    Script: SaveToken       
    Version: <version-uuid> # Optional
    Delete: 30 days         # Optional
```

```yaml
# With an item
- RUN|.SAVE >> $saved:
    Item: 
        :$item:
    Set: $item.Set
    Script: SaveToken
    Version: <version-uuid> # Optional
    Delete: 30 days         # Optional
```

## Script

```yaml
📃 .SAVE:

# Fill the $item
- ASSERT:
    AllOf: $:Set, $:Item
    Texts: $:Set
    Lists: $:Script, $:Delete
    UUIDs: $:Version

# Send the request and wait.
- SEND >> $saved:
    Header:
        To: $.Settings.Itemizer
        Subject: Save@Itemizer
    Body:
        Item: $:Item
        Set: $:Set
        Version: $:Version
        Script: $:Script
        Delete: $:Delete

# Return the saved item
- RETURN|$saved
```


Needs||
|-|-
| [Commands ⌘](<../../../...commands ⌘/⌘ Command.md>) | [`ASSERT`](<../../../...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>)  [`SEND`](<../../../...messages 📨/SEND 📬 msg.md>) [`RETURN`](<../../../...control ▶️/RETURN ⤴️/RETURN ⤴️.md>) [`RUN`](<../../../...control ▶️/RUN ▶️/RUN ▶️.md>)
| [Messages 📨](<../../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Save@Itemizer`](<../../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Save.md>)
| [Placeholders 🧠](<../../../...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Settings`](<../../../...messages 📨/$.Settings 🎛️.md>)
|