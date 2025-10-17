
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest.md>): taxes.any-nation.dom
<!--# 🏳️🏛️ https://quip.com/cVKTAXdzJmY6-->

```yaml
🤝: nlweb.dom/MANIFEST

About:
  Domain: taxes.any-nation.dom
  Name: Any Nation's Tax Services
  
  
Trusts:
      
  # Allow parkings to consume licence plates.
  - Role: CONSUMER
    Queries: 
      - nlweb.dom/PERSONA/VEHICLE/PARKING
    Domains: 
      - carpark.any-business.dom
      