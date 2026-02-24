
# 📜 [Manifest](<../../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): ecb.europa.eu
<!--# 🇪🇺 https://quip.com/bBbpAAGfOCIz/-Europaeu-->

```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: ecb.europa.eu
  Title: European Central Bank
              

Trusts:   

  # Protect from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
      
      
  # Allow bank operations between countries.
  - Query: pollyweb.org/BANK/*
    Domains: 
      
      # European Union countries
      - gov.mt      # Malta
      - gov.pt      # Portugal
      - governo.it  # Italy
      - gv.at       # Austria
      # ...

      # Other countries
      - any-nation.dom      # Any nation
      - usa.gov     # USA
      # ...
```