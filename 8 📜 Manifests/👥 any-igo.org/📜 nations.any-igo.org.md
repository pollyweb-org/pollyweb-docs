
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>): nations.any-igo.org
<!--# 🇺🇳 https://quip.com/OV9hAzKhb8Wf/-UNorg-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: nations.any-igo.org
  Name: Nation Members of Any IGO
  

Trusts:
      
  # Inherit blockers from parent. 
  - Action: INHERIT
    Domain: any-igo.org


  # Allow countries to share profiles of citizens.
  - Queries:
      - nlweb.org/EXCHANGE
      - nlweb.org/PAY
      - nlweb.org/PERSONA      
      - nlweb.org/STORAGE         
    Domains: 
      - europa.eu       # European Union
      - any-nation.org  # Any Nation
      - usa.gov         # United States      