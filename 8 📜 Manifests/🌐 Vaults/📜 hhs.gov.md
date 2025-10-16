
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): hhs.gov
<!--# 🇺🇸🏥 https://quip.com/xt4NAtlVAjQJ/-HHSgov-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: hhs.gov
  Name: U.S. Department of Health & Human Services
  

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