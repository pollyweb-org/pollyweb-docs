# 🇺🇸 https://quip.com/VtTHA12LzVsr/-USAgov

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: federalreserve.gov
  Name: Federal Reserve of the United States


Trusts:
      
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
      

  # Allow bank operations with other countries.
  - Query: nlweb.org/BANK/*
    Domains: 
      # American banks
      - bankofamerica.com
      - capitalone.com
      - jpmorganchase.com
      # Other countries
      - europa.eu # EU-regulated finantial entities.
