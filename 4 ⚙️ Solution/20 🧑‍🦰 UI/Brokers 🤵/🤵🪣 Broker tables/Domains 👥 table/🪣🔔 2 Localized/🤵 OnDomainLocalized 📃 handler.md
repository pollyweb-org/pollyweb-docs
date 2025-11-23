# 🤵 OnDomainLocalized 📃 handler

## Diagram

![alt text](<🤵 OnDomainLocalized ⚙️ uml.png>)

## Script

```yaml
📃 OnDomainLocalized:

# Translate the domain info
- TRANSLATE >> $domain:
    To: $Domain.Language
    Domain: $Domain.Name
    
# Save the translation
- SAVE|$Domain:
    Title: $domain.Title
    Description: $domain.Description
```

|Uses ||
|-|-
| [Commands ⌘](<../../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`TRANSLATE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/TRANSLATE 🈯/🈯 TRANSLATE ⌘ cmd.md>)
| [Datasets 🪣](<../../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`Domains`](<../🪣 Domains/🤵 Broker.Domains 🪣 table.md>)
|