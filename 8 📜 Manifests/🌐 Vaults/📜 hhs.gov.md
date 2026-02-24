
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): hhs.gov


```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: hhs.gov
  Title: U.S. Department of Health & Human Services
  

Trusts:


  # Share SSR of US citizens with those trusted by US.
  - Role: CONSUMER
    Queries: 
      - airlines.any-igo.dom/SSR/*
    Domains: 
      - usa.gov


  # Blocks whoever the US blocks.
  - Action: INHERIT
    Domains:
      - usa.gov

                      
# Issues SSR tokens for US citizens.
Issuer:

  - From: 2022/01/09
    To: 9999/12/31
    Algorithm: RSA
    PublicKey: >-
      ...
```      