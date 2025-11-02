
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): governo.it
<!--# 🇮🇹 https://quip.com/Aa9oAaGzmFFh/-Governoit-->

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: governo.it
  Title: Italian Government
  

Issuer:
  # Issue SSR tokens for Italian citizens.
  - From: 2022/01/09
    To: 9999/12/31
    Algorithm: RSA
    PublicKey: >-
      ...  


Trusts:

  # Allow queries on SSR of Italian citizens.
  - Role: CONSUMER
    Query: europa.eu/DISABILITY/CARD
    Domains:
      - europa.eu
      
  # Trusts 16+ tokens from the nation.
  - Role: CONSUMER
    Query: nlweb.dom/PALM/16+
    Domains: 
      - any-nation.dom
      