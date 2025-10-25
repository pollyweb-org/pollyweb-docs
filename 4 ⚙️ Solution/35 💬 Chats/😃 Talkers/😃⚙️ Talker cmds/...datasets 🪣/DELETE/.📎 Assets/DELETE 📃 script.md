# 😃📃 `.DELETE` 🗑️ script

> Implements the [`DELETE`](<../DELETE 🗑️ item.md>) command

> Invokes the [`Delete@Itemizer` 🅰️ method](<../../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Delete.md>)


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
- ASSERT:
    AllOf: $:Set, $:Key
    Texts: $:Set
    Lists: $:Key, $:Undo, $:Script

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
| [Commands ⌘](<../../../...commands ⌘/Command ⌘/Command ⌘.md>) | [`ASSERT`](<../../../...placeholders 🧠/ASSERT 🚦/ASSERT 🚦.md>) [`SEND`](<../../../...messages 📨/SEND 📬 msg.md>) [`RETURN`](<../../../...control ▶️/RETURN ⤴️/RETURN ⤴️.md>) [`RUN`](<../../../...control ▶️/RUN ▶️/RUN ▶️.md>)
| [Messages 📨](<../../../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Delete@Itemizer`](<../../../../../../45 🤲 Helper domains/Itemizers 🛢/🛢🅰️ Itemizer methods/...for Items/👥🚀🛢 Delete.md>)
| [Placeholders 🧠](<../../../...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Settings`](<../../../...messages 📨/$.Settings 🎛️.md>)
|