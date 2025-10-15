
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/📜 Manifest.md>): gov.mt
<!--# 🇲🇹 https://quip.com/WtVuAnRgeyD9/-Govmt-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: gov.mt
  Name: Government of Malta
  

Issuer:
  # Issue SSR tokens for Malta citizens.
  - From: 2022/01/09
    To: 9999/12/31
    Algorithm: RSA
    PublicKey: >-
      ...  


Trusts:              

  # Allow queries on SSR of Malta citizens.
  - Role: CONSUMER
    Queries: 
      - europa.eu/DISABILITY/CARD
    Domains:
      - europa.eu
    