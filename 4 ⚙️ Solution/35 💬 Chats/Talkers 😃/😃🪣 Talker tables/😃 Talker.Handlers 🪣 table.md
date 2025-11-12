# 😃📨 Talker.Handlers 🪣 table

> Purpose
* Maps the [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) subjects to [Script 📃](<../../Scripts 📃/Script 📃.md>) handlers.

## Schema

```yaml
Prefix: Talker
Name: Handlers
Key: Domain, Subject
```

## Example

```yaml
Domain: any-domain.dom
Subject: Hello@Host
Handler: Hello@Host
```

Property | Type | Details | Origin | Purpose
|-|-|-|-|-
| `Domain` | text | [domain 👥](<../../../40 👥 Domains/👥 Domain/👥 Domain.md>) name
| `Subject` | text| [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) subject
| `Handler` | text| [Script 📃](<../../Scripts 📃/Script 📃.md>) name
|