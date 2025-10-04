
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>): taxes.any-nation.org
<!--# 🏳️🏛️ https://quip.com/cVKTAXdzJmY6-->

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: taxes.any-nation.org
  Name: Any Nation's Tax Services
  
  
Trusts:
      
  # Allow parkings to consume licence plates.
  - Role: CONSUMER
    Queries: 
      - nlweb.org/PERSONA/VEHICLE/PARKING
    Domains: 
      - carpark.any-business.org
      