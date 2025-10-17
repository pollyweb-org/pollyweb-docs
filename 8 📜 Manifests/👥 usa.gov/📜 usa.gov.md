
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest.md>): usa.gov
<!--# 🇺🇸 https://quip.com/VtTHA12LzVsr/-USAgov-->

```yaml
🤝: nlweb.dom/MANIFEST
```
```yaml
About:
  Domain: usa.gov
  Name: US Government
```

```yaml
Trusts:
```

```yaml      
  # Protection from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
```      

```yaml
  # Share SSR of US citizens via HHS.
  - Query: airlines.any-igo.dom/SSR/*
    Role: VAULT
    Domain: hhs.gov
```

```yaml 
  # Allow transporters to ask SSR of US citizens.
  - Query: airlines.any-igo.dom/SSR/*
    Role: CONSUMER
    Domains: 
      - airlines.any-igo.dom     # Any IGO Airlines
      - aviation.any-igo.dom     # Airlines @ICAO
```

```yaml      
  # Allow domains to share profiles of citizens.
  - Query: nlweb.dom/PERSONA/*
    Domains: 
      - irs.gov     # Internal Revenue Service
      - nations.any-igo.dom      # Any IGO   
```

```yaml
  # Delegate bank trusts to the federal reserve.
  - Query: nlweb.dom/BANK/*
    Domain: federalreserve.gov
```