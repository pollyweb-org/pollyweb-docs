
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): airport.any-nation.dom
<!--# 🏳️🛩️ https://quip.com/YJvcAJB72qzI-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: airport.any-nation.dom
  Name: Any Airport
  
  
Trusts:
      
  # Receive info from airline industry domains.
  - Role: VAULT
    Queries: 
      - airlines.any-igo.dom/SSR/*
      - europa.eu/DISABILITY/CARD
    Domains: [ airlines.any-igo.dom ]

  # Share WCHR tokens with the airline industry.
  - Role: CONSUMER
    Query: airlines.any-igo.dom/SSR/WCHR/CRED
    Domains: [ airlines.any-igo.dom ]

  # Notify AnyAirline that a passenger was found at gate.
  - Role: CONSUMER
    Query: nlweb.org/PALM/FOUND
    Domains: [ airline.any-business.org ]