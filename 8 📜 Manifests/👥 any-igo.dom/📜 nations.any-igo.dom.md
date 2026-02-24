
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): nations.any-igo.dom
<!--# 🇺🇳 https://quip.com/OV9hAzKhb8Wf/-UNorg-->

```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: nations.any-igo.dom
  Title: Nation Members of Any IGO
  

Trusts:
      
  # Inherit blockers from parent. 
  - Action: INHERIT
    Domain: any-igo.dom


  # Allow countries to share profiles of citizens.
  - Queries:
      - pollyweb.org/EXCHANGE
      - pollyweb.org/PAY
      - pollyweb.org/PERSONA      
      - pollyweb.org/STORAGE         
    Domains: 
      - europa.eu       # European Union
      - any-nation.dom  # Any Nation
      - usa.gov         # United States      
```