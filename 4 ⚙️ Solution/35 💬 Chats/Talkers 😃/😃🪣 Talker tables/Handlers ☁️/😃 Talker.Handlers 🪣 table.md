# 😃📨 Talker.Handlers 🪣 table

> Purpose
* Maps the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) subjects to [Script 📃](<../../../Scripts 📃/Script 📃.md>) handlers.

> Data access

* [`SAVE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) by [Hoster ☁️ helper domains](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️ Hoster helper/☁️ Hoster 🤲 helper.md>) when setting a [Hosted 📦 domain](<../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>)
* [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) by [Hoster ☁️ helper domains](<../../../../45 🤲 Helper domains/Hosters ☁️/☁️ Hoster helper/☁️ Hoster 🤲 helper.md>) when handling [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)

## Schema

Here's the [Itemized 🪣 dataset](<../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) schema.

```yaml
Prefix: Talker
Name: Handlers
Key: Domain, Subject
```

## Example

Here's the [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) output.

```yaml
Domain: any-domain.dom
Subject: Hello@Host
Handler: Hello@Host
```

Property | Type | Details | Origin | Purpose
|-|-|-|-|-
| `Domain` | text | [domain 👥](<../../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
| `Subject` | text| [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) subject
| `Handler` | text| [Script 📃](<../../../Scripts 📃/Script 📃.md>) name
|