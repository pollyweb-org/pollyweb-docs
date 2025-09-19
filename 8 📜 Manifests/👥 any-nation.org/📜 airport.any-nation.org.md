<!--# 🏳️🛩️ https://quip.com/YJvcAJB72qzI-->

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: airport.any-nation.org
  Name: Any Airport
  
  
Trusts:
      
  # Receive info from airline industry domains.
  - Role: VAULT
    Queries: 
      - airlines.any-igo.org/SSR/*
      - europa.eu/DISABILITY/CARD
    Domains: [ airlines.any-igo.org ]

  # Share WCHR tokens with the airline industry.
  - Role: CONSUMER
    Query: airlines.any-igo.org/SSR/WCHR/CRED
    Domains: [ airlines.any-igo.org ]

  # Notify AnyAirline that a passenger was found at gate.
  - Role: CONSUMER
    Query: nlweb.org/PALM/FOUND
    Domains: [ airline.any-business.org ]
