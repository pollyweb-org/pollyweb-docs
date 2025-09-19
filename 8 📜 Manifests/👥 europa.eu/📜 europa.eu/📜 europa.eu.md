
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>): europa.eu
<!--# 🇪🇺 https://quip.com/bBbpAAGfOCIz/-Europaeu-->

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: europa.eu
  Name: European Union
              

Delegates:

  # Delete the disability card to the european comission.
  - Delegate: ec.europa.eu
    Code: /DISABILITY/CARD


Trusts:   

  # Protect from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
      
  # Delegate disability card trusts to the European Comission.
  - Query: europa.eu/DISABILITY/CARD/*
    Domain: ec.europa.eu
  
  # Delegate bank trusts to the European Central Bank.
  - Query: nlweb.org/BANK/*
    Domain: ecb.europa.eu