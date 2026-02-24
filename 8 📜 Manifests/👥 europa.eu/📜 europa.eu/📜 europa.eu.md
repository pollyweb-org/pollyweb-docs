
# 📜 [Manifest](<../../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): europa.eu
<!--# 🇪🇺 https://quip.com/bBbpAAGfOCIz/-Europaeu-->

```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: europa.eu
  Title: European Union
              

Delegates:

  # Delete the disability card to the european comission.
  - Delegate: ec.europa.eu
    Schema: /DISABILITY/CARD


Trusts:   

  # Protect from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
      
  # Delegate disability card trusts to the European Comission.
  - Query: europa.eu/DISABILITY/CARD/*
    Domain: ec.europa.eu
  
  # Delegate bank trusts to the European Central Bank.
  - Query: pollyweb.org/BANK/*
    Domain: ecb.europa.eu
```