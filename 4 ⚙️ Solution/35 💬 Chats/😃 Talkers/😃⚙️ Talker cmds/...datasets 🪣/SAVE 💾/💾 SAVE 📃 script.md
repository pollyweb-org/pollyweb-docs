# 😃📃 `.SAVE` 🗑️ script

> Implements the [`SAVE`](<💾 SAVE ⌘ cmd.md>)

> Invokes the [`Save@Itemizer`](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Save 👥🚀🛢/🛢 Save 🚀 request.md>) method


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
| [Commands ⌘](<../../...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../...placeholders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>)  [`SEND`](<../../...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RETURN`](<../../...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../...control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Save@Itemizer`](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Save 👥🚀🛢/🛢 Save 🚀 request.md>)
| [Placeholders 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Settings`](<../../...messages 📨/$.Settings 🎛️.md>)
|