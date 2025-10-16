
# 📜 [Manifest](<../../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): ecb.europa.eu
<!--# 🇪🇺 https://quip.com/bBbpAAGfOCIz/-Europaeu-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: ecb.europa.eu
  Name: European Central Bank
              

Trusts:   

  # Protect from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
      
      
  # Allow bank operations between countries.
  - Query: nlweb.org/BANK/*
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