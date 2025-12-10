# 😃🧠 Talker.Holders 🪣 table

> Data access
* [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) by the [`Place` 📃 handler](<../../😃📨 Talker msgs/Place 🧑‍💻🚀😃/😃 Place 📃 handler.md>)
* [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) by the [`Placed` 📃 handler](<../../😃📨 Talker msgs/Placed 🧑‍💻🚀😃/😃 Placed 📃 handler.md>)

## Schema

```yaml
# Holders.yaml

Prefix: Talker
Table: Holders
Keys: Hook, Holder
Parents: 
    Hook: {Hooks.ID: Holders.Hook}
```

| Relationship | Table | Contains
|-|-|-
| Parent | [`Hooks`](<../Wait 🧘 » Race 🏁/😃 Talker.Waits 🪣 table.md>)
|

## Example

```yaml
Hook: <hook-uuid>
Holder: my-holder
Schema: .ITEMIZER/ITEM
Value: {...}
```

|Property|Type|Details|
|-|-|-
|`Hook`| uuid | [`TalkerHooks` 🪣 table](<../Wait 🧘 » Race 🏁/😃 Talker.Waits 🪣 table.md>) ID
|`Holder`|text| [Holder 🧠](<../../../Scripts 📃/Holder 🧠.md>) name
|`Schema`|text| [Schema Code 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|`Value` | any | Content of the [Holder 🧠](<../../../Scripts 📃/Holder 🧠.md>)
|