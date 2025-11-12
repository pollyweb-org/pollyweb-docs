# 😃🧠 Talker.Holders 🪣 table

> Data access
* [`SAVE`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) by the [`Place` 📃 handler](<../😃🅰️ Talker methods/Place 🧑‍💻🚀😃/😃 Place 📃 handler.md>)
* [`READ`](<../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) by the [`Placed` 📃 handler](<../😃🅰️ Talker methods/Placed 🧑‍💻🚀😃/😃 Placed 📃 handler.md>)

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
| Parent | [`Hooks`](<😃 Talker.Hooks 🪣 table.md>)
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
|`Hook`| uuid | [`TalkerHooks` 🪣 table](<😃 Talker.Hooks 🪣 table.md>) ID
|`Holder`| string | [Holder 🧠](<../../Scripts 📃/Holder 🧠.md>) name
|`Schema`| string | [Schema Code 🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|`Value` | any | Content of the [Holder 🧠](<../../Scripts 📃/Holder 🧠.md>)
|