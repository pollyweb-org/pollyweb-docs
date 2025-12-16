# 🆔 Stamps 🪣 table

> Part of [Identity 🆔 domain](<../../../🆔 Identifier agent/🆔 Identifier 🫥 agent.md>)

<br/>

## Schema

Here's the [Itemized 🪣 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Identity
Table: Stamps
Item: Stamp
```

<br/>

The [Item 🛢 Parents](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Parents.md>) are: [`Vault.Binds`](<../../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🪣 Vault tables/Binds 🔗 table/🪣 Binds/🗄️ Vault.Binds 🪣 table.md>) 

```yaml
Parents: 
    Bind  # Bind being stamped in the biostamp
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <stamp-uuid>
```

From the [`Biostamp` 😃 talker](<../../../🆔😃 Identifier talkers/Biostamp 🎫 disclose/🆔 Biostamp 😃 talker.md>)

```yaml
Consumer: <consumer-uuid>
Query: <query-uuid>
Bind: <bind-uuid>
``` 