
# 📜 [Manifest](<../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): health.any-igo.dom


```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: health.any-igo.dom
  Title: World Health Organization
  

Schemas:
  
  # Vaccination dose certificate
  - Path: /DOSE
    Schemas:
      - Version: 1.0
        Inherits: pollyweb.org/TOKEN:1.0
        Properties:
          - purpose   # ex. COVID
          - vaccine   # ex. Moderna
          - date      # date
          - dose      # ex. Booster
          - entity    # ex. health.any-nation.dom
          - locator   # ex. KLDJ94H4592DJG5SA
          - firstName # ex. Jai
          - lastName  # ex. Gutten
        
  
  # Test certificate
  - Path: /TEST
    Schemas:
      - Version: 1.0
        Inherits: pollyweb.org/TOKEN:1.0
        Properties:
          - purpose    # ex. COVID
          - type       # ex. PCR
          - date       # <date>
          - result     # ex. NEGATIVE
          - entity     # ex. health.any-nation.dom
          - supervised # bool, ex. TRUE
          - supervisor # ex. Dr. Kay L9230411 
          - firstName  # ex. Jai
          - lastName   # ex. Gutten   
          

  # COVID certificates
  - Path: /COVID
  
  
  # COVID Vaccination certificate
  - Path: /COVID/DOSE
    Title: COVID Vaccination
    Translations:
      - Language: pt-br
        Title: Vacina COVID
    Schemas:
      - Version: 1.0
        Inherits: health.any-igo.dom/DOSE:1.0
        
        
  # COVID test certificate
  - Path: /COVID/TEST
    Title: COVID Test
    Translations:
      - Language: pt-br
        Title: Teste COVID
    Schemas:
      - Inherits: health.any-igo.dom/TEST:1.0
```