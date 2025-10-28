# 😃📃 `.SAVE` 💾 script

> Implements the [`SAVE`](<💾 SAVE ⌘ cmd.md>)

> Invokes the [`Save@Itemizer`](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Save 👥🚀🛢/🛢 Save 🚀 request.md>) method


## How to call

```yaml
# With multiple parameters
- RUN|.SAVE >> $saved:
    Item: {A:1, B:1}
    Set: MySet
    Script: SaveToken       
    Version: <version-uuid>  # Optional
    Delete: 30 days          # Optional
    OnBlocked: myPlaceholder # Optional
```

```yaml
# With an item
- RUN|.SAVE >> $saved:
    Item: 
        :$item:
    Set: $item.Set
    Script: SaveToken
    Version: <version-uuid>  # Optional
    Delete: 30 days          # Optional
    OnBlocked: myPlaceholder # Optional
```

## Script

```yaml
📃 .SAVE:

# Fill the $item
- ASSERT|.Inputs:
    .AllOf: Set, Item
    .Texts: Script, Set, OnBlocked, Delete
    .UUIDs: Version

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

# Check the status
- CASE|$saved.Status:

    # Return the saved item
    OK: RETURN|$saved.Item

    # Ask for a rerun
    OUTDATED: HTTP|412|Outdated

    # If blocked, see if there's a handler
    BLOCKED: 
        IF|$:OnBlocked:
            Then: EVAL|True >> $:OnBlocked
            Else: HTTP|423|Blocked
```


Needs||
|-|-
| [Commands ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../...placeholders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../...control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`HTTP`](<../../...control ▶️/HTTP 💥/💥 HTTP ⌘ cmd.md>) [`SEND`](<../../...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RETURN`](<../../...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../...control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Save@Itemizer`](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Save 👥🚀🛢/🛢 Save 🚀 request.md>)
| [Placeholders 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Settings`](<../../...messages 📨/$.Settings 🎛️.md>)
|