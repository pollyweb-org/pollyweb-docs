# 🇺🇸🏥 https://quip.com/xt4NAtlVAjQJ/-HHSgov

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: hhs.gov
  Name: U.S. Department of Health & Human Services
  

Trusts:


  # Share SSR of US citizens with those trusted by US.
  - Role: CONSUMER
    Queries: 
      - airlines.any-igo.org/SSR/*
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
