
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): airlines-ssr.any-igo.dom
<!--# 💺🏛️ https://quip.com/FuTpA83cGJ3L-->

```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: airlines-ssr.any-igo.dom
  Title: SSR Department of Any IGO Airlines
```
  
```yaml
Datasets:
```

```yaml
  # [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) //MEALS list.
  - Dataset: airlines.any-igo.dom/SSR/MEAL
    Requires: 
      Language: Code@standards.any-igo.dom/639-1
```

```yaml
Schemas:
```

```yaml
  # --------------------------------------------------
  # [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) /SSR
  # Manage SSR on behalf of Any IGO Airlines
  # --------------------------------------------------

  - Path: /SSR
    Delegator: airlines.any-igo.dom
```  
  
```yaml
  # --------------------------------------------------
  # [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) //WCHR/CRED
  # Token: Wheelchair for ramp
  # --------------------------------------------------

  - Path: /SSR/WCHR/CRED
    Delegator: airlines.any-igo.dom
    Title: Wheelchair for ramp
    
    Translations:
      - Language: en-us
        Title: Wheelchair for ramp
        
    Schemas:
      - Version: 1.0
        Inherits: pollyweb.org/TOKEN:1.0
        Format: IsElectric, Size, NeedsAssistant, DateOfBirth
        Location: https://airlines.any-igo.dom/pollyweb/schemas/SSR-WCHR.json
```

```yaml
  # --------------------------------------------------
  # [🧩](<../../4 ⚙️ Solution/30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) //MEAL
  # --------------------------------------------------

  - Path: /SSR/MEAL
    Delegator: airlines.any-igo.dom
    References:
      Amadeus: https://servicehub.amadeus.dom/c/portal/view-solution/768896/special-services-request-ssr-codes-and-airline-specific-codes
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