
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>): airlines-ssr.any-igo.org
<!--# 💺🏛️ https://quip.com/FuTpA83cGJ3L-->

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: airlines-ssr.any-igo.org
  Name: SSR Department of Any IGO Airlines
  
  
Datasets:

  # 🧩 //MEALS list.
  - Dataset: airlines.any-igo.org/SSR/MEAL
    Requires: 
      Language: Code@standards.any-igo.org/639-1
    

Codes:

  # --------------------------------------------------
  # 🧩 /SSR
  # Manage SSR on behalf of Any IGO Airlines
  # --------------------------------------------------

  - Path: /SSR
    Delegator: airlines.any-igo.org
    
  # --------------------------------------------------
  # 🧩 //WCHR/CRED
  # Token: Wheelchair for ramp
  # --------------------------------------------------

  - Path: /SSR/WCHR/CRED
    Delegator: airlines.any-igo.org
    Name: Wheelchair for ramp
    
    Translations:
      - Language: en-us
        Translation: Wheelchair for ramp
        
    Schemas:
      - Output: SHARE
        Version: '1.2'
        Location: https://airlines.any-igo.org/nlweb/schemas/SSR-WCHR.json
        
      - Output: QR
        Version: 1.0
        Inherits: nlweb.org/TOKEN:1.0
        Format: IsElectric, Size, NeedsAssistant, DateOfBirth

  # --------------------------------------------------
  # 🧩 //MEAL
  # --------------------------------------------------

  - Path: /SSR/MEAL
    Delegator: airlines.any-igo.org
    References:
      Amadeus: https://servicehub.amadeus.com/c/portal/view-solution/768896/special-services-request-ssr-codes-and-airline-specific-codes
      Any IGO Airlines: https://guides.developer.airlines.any-igo.org/archive/docs/list-of-service-ssrs 

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
                