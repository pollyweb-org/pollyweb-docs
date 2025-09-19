
# 📜 Manifest: usa.gov
<!--# 🇺🇸 https://quip.com/VtTHA12LzVsr/-USAgov-->

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: usa.gov
  Name: US Government


Trusts:
      
      
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
      

  # Share SSR of US citizens via HHS.
  - Query: airlines.any-igo.org/SSR/*
    Role: VAULT
    Domain: hhs.gov
    
  # Allow transporters to ask SSR of US citizens.
  - Query: airlines.any-igo.org/SSR/*
    Role: CONSUMER
    Domains: 
      - airlines.any-igo.org     # Any IGO Airlines
      - aviation.any-igo.org     # Airlines @ICAO

      
  # Allow domains to share profiles of citizens.
  - Query: nlweb.org/PROFILE/*
    Domains: 
      - irs.gov     # Internal Revenue Service
      - nations.any-igo.org      # Any IGO   
      

  # Delegate bank trusts to the federal reserve.
  - Query: nlweb.org/BANK/*
    Domain: federalreserve.gov
