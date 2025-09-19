
# 📜 Manifest: any-nation.org

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: any-nation.org
  Name: Any Nation's Government
  Resources:
    NLWEB: 🏳️ https://quip.com/0ULzAy0gQ8w9/-Govuk
  

Trusts:

  - Title: Protection from malicious domains. 
    Action: INHERIT
    Domains:
      - any-firewall.org
      
  
  - Title: Share SSR of UK citizens via NHS.
    Role: VAULT
    Expires: '2050-01-01T10:00:00.000Z'  
    Queries: [ airlines.any-igo.org/SSR/* ]
    Domains: [ health.any-nation.org ]
    

  - Title: Allow transporters to ask SSR of UK citizens.
    Role: CONSUMER
    Queries: [ airlines.any-igo.org/SSR/* ]
    Domains: 
      - airlines.any-igo.org # Any IGO Airlines
      - aviation.any-igo.org # Aviation Members of Any IGO
      - nationalrail.co.uk   # UK Trains
      - tfl.any-nation.org   # London Transports
      

  - Title: Allow domains to share profiles of citizens.
    Query: nlweb.org/PROFILE
    Domains: 
      - taxes.any-nation.org  # Tax Service's
      - nations.any-igo.org   # Any IGO


  - Title: Allow palmist centers to query passport info.
    Query: aviation.any-igo.org/PASSPORT
    Role: CONSUMER
    Domains: [ any-palmist.uk ]