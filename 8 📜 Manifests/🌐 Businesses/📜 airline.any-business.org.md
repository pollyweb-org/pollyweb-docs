
# 📜 [Manifest](<../../4 ⚙️ Solution/40 👥 Domains/👥📜 Domain Manifests/📜 Manifest.md>): airline.any-business.org
<!--# 🏳️💺 https://quip.com/Yp6rADERIDPv/-Air-France-Airline -->

```yaml
🤝: nlweb.org/MANIFEST

About:
  Domain: airline.any-business.org
  Name: Any Airline

  
Trusts:

  # Receive info from airline industry domains.
  - Role: VAULT
    Queries: 
      - airlines.any-igo.org/SSR/*
      - europa.eu/DISABILITY/CARD
    Domain: airlines.any-igo.org    

  # Share WCHR tokens with the airline industry.
  - Role: CONSUMER
    Query: airlines.any-igo.org/SSR/WCHR/CRED
    Domain: airlines.any-igo.org  

  # Receive info from NHS.
  - Role: VAULT
    Queries: [ health.any-igo.org/COVID/DOSE ]
    Domain: health.any-nation.org

    
Issuer:

  - From: 2020/05/01
    To: 9999/12/31
    Algorithm: RSA
    PublicKey: >-
      MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQBRaKQ8LCftqaKxJGCmAZnMsirnBUhBicaP64gHPlvw9AEBkLzLFjO/TJq7BjBJN3VCXMfBrTR20i6DUoq9tV+JtFPcIfAXvGdBPK/aLMLQJlzAtFCQBTglV7i6lineprAwqaMRjD1nz0XNMGJQme/bmSSqhjBBNMQWwxH05Sq6Ths/KgdyFoGmrHcpJAOC9wR6sW8Kx+ViRErlIS0viWl6OT+livtrUjaTEVYtX3IdkU7/9+POXv2XTwawqiBtzUysXmF4F5HcIEGKkHyLGPueNkS1OBGnoACNhZ/Uf/8YuuQ+r8yXrc/jYtKjnigKM1bp0XAIVVo9R6QWU3cLEFFrAgMBAAE=
      