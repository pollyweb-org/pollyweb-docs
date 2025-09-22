
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>): health.any-igo.org
<!--# 🇺🇳 https://quip.com/PcpmA0e2TORI/-WHOint-->

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: health.any-igo.org
  Name: World Health Organization
  

Codes:
  
  # Vaccination dose certificate
  - Path: /DOSE
    Schemas:
      - Version: 1.0
        Inherits: nlweb.org/TOKEN:1.0
        Properties:
          - purpose   # ex. COVID
          - vaccine   # ex. Moderna
          - date      # date
          - dose      # ex. Booster
          - entity    # ex. health.any-nation.org
          - locator   # ex. KLDJ94H4592DJG5SA
          - firstName # ex. Jai
          - lastName  # ex. Gutten
        
  
  # Test certificate
  - Path: /TEST
    Schemas:
      - Version: 1.0
        Inherits: nlweb.org/TOKEN:1.0
        Properties:
          - purpose    # ex. COVID
          - type       # ex. PCR
          - date       # <date>
          - result     # ex. NEGATIVE
          - entity     # ex. health.any-nation.org
          - supervised # bool, ex. TRUE
          - supervisor # ex. Dr. Kay L9230411 
          - firstName  # ex. Jai
          - lastName   # ex. Gutten   
          

  # COVID certificates
  - Path: /COVID
  
  
  # COVID Vaccination certificate
  - Path: /COVID/DOSE
    Name: COVID Vaccination
    Translations:
      - Language: pt-br
        Translation: Vacina COVID
    Schemas:
      - Version: 1.0
        Inherits: health.any-igo.org/DOSE:1.0
        
        
  # COVID test certificate
  - Path: /COVID/TEST
    Name: COVID Test
    Translations:
      - Language: pt-br
        Translation: Teste COVID
    Schemas:
      - Inherits: health.any-igo.org/TEST:1.0
        