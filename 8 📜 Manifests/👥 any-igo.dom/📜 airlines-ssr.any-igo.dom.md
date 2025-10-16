
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): airlines-ssr.any-igo.dom
<!--# 💺🏛️ https://quip.com/FuTpA83cGJ3L-->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: airlines-ssr.any-igo.dom
  Name: SSR Department of Any IGO Airlines
```
  
```yaml
Datasets:
````

```yaml
  # [🧩](<../../4 ⚙️ Solution/30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) //MEALS list.
  - Dataset: airlines.any-igo.dom/SSR/MEAL
    Requires: 
      Language: Code@standards.any-igo.dom/639-1
```

```yaml
Codes:
```

```yaml
  # --------------------------------------------------
  # [🧩](<../../4 ⚙️ Solution/30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) /SSR
  # Manage SSR on behalf of Any IGO Airlines
  # --------------------------------------------------

  - Path: /SSR
    Delegator: airlines.any-igo.dom
```  
  
```yaml
  # --------------------------------------------------
  # [🧩](<../../4 ⚙️ Solution/30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) //WCHR/CRED
  # Token: Wheelchair for ramp
  # --------------------------------------------------

  - Path: /SSR/WCHR/CRED
    Delegator: airlines.any-igo.dom
    Name: Wheelchair for ramp
    
    Translations:
      - Language: en-us
        Translation: Wheelchair for ramp
        
    Schemas:
      - Version: 1.0
        Inherits: nlweb.org/TOKEN:1.0
        Format: IsElectric, Size, NeedsAssistant, DateOfBirth
        Location: https://airlines.any-igo.dom/nlweb/schemas/SSR-WCHR.json
```

```yaml
  # --------------------------------------------------
  # [🧩](<../../4 ⚙️ Solution/30 🧩 Data/1 🧩 Schema Codes/🧩 Schema Code.md>) //MEAL
  # --------------------------------------------------

  - Path: /SSR/MEAL
    Delegator: airlines.any-igo.dom
    References:
      Amadeus: https://servicehub.amadeus.com/c/portal/view-solution/768896/special-services-request-ssr-codes-and-airline-specific-codes
      Any IGO Airlines: https://guides.developer.airlines.any-igo.dom/archive/docs/list-of-service-ssrs 

    Schemas:
      - Properties: 
          - Title
          - Code
        Format:
          type: object
          properties: 

            Title: 
              type: string
              example: Vegetarian Hindu

            Code:
              enum: 
                - AVML  # Vegetarian Hindu
                - BBML  # Baby
                - BLML  # Bland
                - CHML  # Child
                - DBML  # Diabetic
                - FPML  # Fruit platter
                - GFML  # Gluten intolerant
                - HNML  # Hindu
                - JPML  # Japanese 
                - KSML  # Kosher
                - LCML  # Low calorie
                - LFML  # Low fat
                - LSML  # Low salt
                - MOML  # Muslim
                - NFML  # No fish 
                - NLML  # Low lactose
                - RVML  # Raw vegetarian
                - SFML  # Seafood
                - VGML  # Vegetarian vegan
                - VJML  # Vegetarian Jain
                - VLML  # Vegetarian lacto-ovo
                - VOML  # Vegetarian Oriental
```                