
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): airlines.any-igo.org
<!--# 💺🏛️ https://quip.com/FuTpA83cGJ3L-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: airlines.any-igo.org
  Name: Any IGO Airlines
  

Delegates:


  # Delegate the definition of SSR codes.
  - Delegate: airlines-ssr.any-igo.org
    Code: /SSR
    

Trusts:

  # Request Disability Card from Europe.
  - Role: VAULT
    Query: europa.eu/DISABILITY/CARD
    Domain: europa.eu

  # Provide Disability Card to airlines.
  - Role: CONSUMER
    Query: europa.eu/DISABILITY/CARD
    Domains:
      - airline.any-business.org
      - airport.any-nation.org
      - flytap.com
    

  # Request SSR info from UN countries.
  - Role: VAULT
    Query: airlines.any-igo.org/SSR/*
    Domains:
      - nations.any-igo.org
      

  # Share SSR info between airlines.   
  - Query: airlines.any-igo.org/SSR/*
    Domains:
      - airline.any-business.org
      - airport.any-nation.org
      - flytap.com
      

  # Protect from malicious domains.
  - Action: INHERIT
    Domain: any-firewall.org
      