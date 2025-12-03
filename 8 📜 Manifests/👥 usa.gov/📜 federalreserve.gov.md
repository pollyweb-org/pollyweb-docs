
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): federalreserve.gov
<!--# 🇺🇸 https://quip.com/VtTHA12LzVsr/-USAgov-->

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: federalreserve.gov
  Title: Federal Reserve of the United States


Trusts:
      
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
      

  # Allow bank operations with other countries.
  - Query: nlweb.dom/BANK/*
    Domains: 
      # American banks
      - bankofamerica.dom
      - capitalone.dom
      - jpmorganchase.dom
      # Other countries
      - europa.eu # EU-regulated finantial entities.
```