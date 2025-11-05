# 😃📃 `.SAVE` 💾 script

> Implements the [`SAVE`](<💾 SAVE ⌘ cmd.md>)

> Invokes the [`Save@Itemizer`](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Save 👥🚀🛢/🛢 Save 🚀 request.md>) method


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
- ASSERT|$.Inputs:
    AllOf: Set, Item
    Texts: Script, Set, OnBlocked, Delete
    UUIDs: Version

# Send the request and wait.
- SEND >> $saved:
    Header:
        To: $.Hosted.Itemizer
        Subject: Save@Itemizer
    Body:
        Item: $Item
        Set: $Set
        Version: $Version
        Script: $Script
        Delete: $Delete

# Check the status
- CASE|$saved.Status:

    # Return the saved item
    OK: RETURN|$saved.Item

    # Ask for a rerun
    OUTDATED: HTTP|412|Outdated

    # If blocked, see if there's a handler
    BLOCKED: 
        IF|$OnBlocked:
            Then: EVAL|True >> $OnBlocked
            Else: HTTP|423|Blocked
```


Uses||
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`ASSERT`](<../../⌘ for holders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`CASE`](<../../⌘ for control ▶️/CASE ⏯️/⏯️ CASE ⌘ cmd.md>) [`HTTP`](<../../⌘ for control ▶️/HTTP 💥/💥 HTTP ⌘ cmd.md>) [`SEND`](<../../⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RETURN`](<../../⌘ for control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../⌘ for control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Holders 🧠](<../../../../35 💬 Chats/Scripts 📃/Holder 🧠.md>) | [`$.Inputs`](<../../../📃 Holders 🧠/🧠 System holders/$.Inputs ▶️/▶️ $.Inputs 🧠 holder.md>) [`$.Hosted`](<../../../📃 Holders 🧠/🧠 System holders/$.Hosted 📦/📦 $.Hosted 🧠 holder.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Save@Itemizer`](<../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Save 👥🚀🛢/🛢 Save 🚀 request.md>)
|