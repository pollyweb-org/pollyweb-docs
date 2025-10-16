
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): nations.any-igo.dom
<!--# 🇺🇳 https://quip.com/OV9hAzKhb8Wf/-UNorg-->

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: nations.any-igo.dom
  Name: Nation Members of Any IGO
  

Trusts:
      
  # Inherit blockers from parent. 
  - Action: INHERIT
    Domain: any-igo.dom


  # Allow countries to share profiles of citizens.
  - Queries:
      - nlweb.dom/EXCHANGE
      - nlweb.dom/PAY
      - nlweb.dom/PERSONA      
      - nlweb.dom/STORAGE         
    Domains: 
      - europa.eu       # European Union
      - any-nation.dom  # Any Nation
      - usa.gov         # United States      