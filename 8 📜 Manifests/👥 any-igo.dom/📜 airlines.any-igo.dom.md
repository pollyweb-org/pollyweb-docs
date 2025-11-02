
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): airlines.any-igo.dom
<!--# 💺🏛️ https://quip.com/FuTpA83cGJ3L-->

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: airlines.any-igo.dom
  Name: Any IGO Airlines
  

Delegates:


  # Delegate the definition of SSR codes.
  - Delegate: airlines-ssr.any-igo.dom
    Schema: /SSR
    

Trusts:

  # Request Disability Card from Europe.
  - Role: VAULT
    Query: europa.eu/DISABILITY/CARD
    Domain: europa.eu

  # Provide Disability Card to airlines.
  - Role: CONSUMER
    Query: europa.eu/DISABILITY/CARD
    Domains:
      - airline.any-business.dom
      - airport.any-nation.dom
      - flytap.dom
    

  # Request SSR info from UN countries.
  - Role: VAULT
    Query: airlines.any-igo.dom/SSR/*
    Domains:
      - nations.any-igo.dom
      

  # Share SSR info between airlines.   
  - Query: airlines.any-igo.dom/SSR/*
    Domains:
      - airline.any-business.dom
      - airport.any-nation.dom
      - flytap.dom
      

  # Protect from malicious domains.
  - Action: INHERIT
    Domain: any-firewall.org
      