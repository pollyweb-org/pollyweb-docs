# 😃📃 `.DELETE` 🗑️ script

> Implements the [`DELETE`](<🗑️ DELETE ⌘ cmd.md>) command

> Invokes the [`Delete@Itemizer` 🅰️ method](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)


## How to call

```yaml
# 📃 With multiple parameters
- RUN|.DELETE >> $deleted:
    Set: MySet
    Key: [Key1, Key2]
    Script: MyScript    
    Undo: 30 days # Optional
```

```yaml
# 📃 With an item
- RUN|.DELETE >> $deleted:
    Set: $item.Set
    Key: $item.Key
    Script: MyScript 
    Undo: 30 days # Optional
```

## Script

```yaml
📃 .DELETE:

# Fill the $item
- ASSERT|.Inputs:
    AllOf: Set, Key
    Texts: Set
    Lists: Key, Undo, Script

# Send the request and wait.
- SEND >> $deleted:
    Header:
        To: $.Settings.Itemizer
        Subject: Delete@Itemizer
    Body:
        Set: $:Set
        Key: $:Key
        Undo: $:Undo
        Script: $:Script

# Return the deleted object
RETURN|$deleted
```


Needs||
|-|-
| [Commands ⌘](<../../...commands ⌘/Command ⌘/⌘ Command.md>) | [`ASSERT`](<../../...placeholders 🧠/ASSERT 🚦/🚦 ASSERT ⌘ cmd.md>) [`SEND`](<../../...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RETURN`](<../../...control ▶️/RETURN ⤴️/⤴️ RETURN ⌘ cmd.md>) [`RUN`](<../../...control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Messages 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Delete@Itemizer`](<../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/Item Delete 👥🚀🛢/🛢 Delete 🚀 request.md>)
| [Placeholders 🧠](<../../...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Settings`](<../../...placeholders 🧠/$.Settings 🎛️/🎛️ $.Settings 🧠 holder.md>)
|