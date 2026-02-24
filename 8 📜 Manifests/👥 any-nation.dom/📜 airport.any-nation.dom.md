
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): airport.any-nation.dom


```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: airport.any-nation.dom
  Title: Any Airport
  
  
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
    Query: pollyweb.org/PALM/FOUND
    Domains: [ airline.any-business.dom ]
```