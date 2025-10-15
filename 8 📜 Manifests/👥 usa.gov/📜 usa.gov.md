
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/📜 Manifest.md>): usa.gov
<!--# 🇺🇸 https://quip.com/VtTHA12LzVsr/-USAgov-->

```yaml
🤝: nlweb.org/MANIFEST
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
  - Query: airlines.any-igo.org/SSR/*
    Role: VAULT
    Domain: hhs.gov
```

```yaml 
  # Allow transporters to ask SSR of US citizens.
  - Query: airlines.any-igo.org/SSR/*
    Role: CONSUMER
    Domains: 
      - airlines.any-igo.org     # Any IGO Airlines
      - aviation.any-igo.org     # Airlines @ICAO
```

```yaml      
  # Allow domains to share profiles of citizens.
  - Query: nlweb.org/PERSONA/*
    Domains: 
      - irs.gov     # Internal Revenue Service
      - nations.any-igo.org      # Any IGO   
```

```yaml
  # Delegate bank trusts to the federal reserve.
  - Query: nlweb.org/BANK/*
    Domain: federalreserve.gov
```