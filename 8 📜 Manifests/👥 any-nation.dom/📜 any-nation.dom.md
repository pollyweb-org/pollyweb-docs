
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): any-nation.dom

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: any-nation.dom
  Name: Any Nation's Government


Trusts:

  - Title: Protection from malicious domains. 
    Action: INHERIT
    Domains:
      - any-firewall.org
      
  
  - Title: Share SSR of UK citizens via NHS.
    Role: VAULT
    Expires: '2050-01-01T10:00:00.000Z'  
    Queries: [ airlines.any-igo.dom/SSR/* ]
    Domains: [ health.any-nation.dom ]
    

  - Title: Allow transporters to ask SSR of UK citizens.
    Role: CONSUMER
    Queries: [ airlines.any-igo.dom/SSR/* ]
    Domains: 
      - airlines.any-igo.dom # Any IGO Airlines
      - aviation.any-igo.dom # Aviation Members of Any IGO
      - nationalrail.co.uk   # UK Trains
      - tfl.any-nation.dom   # London Transports
      

  - Title: Allow domains to share profiles of citizens.
    Query: nlweb.dom/PERSONA
    Domains: 
      - taxes.any-nation.dom  # Tax Service's
      - nations.any-igo.dom   # Any IGO


  - Title: Allow palmist centers to query passport info.
    Query: aviation.any-igo.dom/PASSPORT
    Role: CONSUMER
    Domains: [ any-palmist.uk ]