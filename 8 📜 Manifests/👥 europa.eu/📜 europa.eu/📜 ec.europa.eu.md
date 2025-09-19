# 🇪🇺 https://quip.com/bBbpAAGfOCIz/-Europaeu

```yaml
🤝: nlweb.org/MANIFEST

Identity:
  Domain: ec.europa.eu
  Name: European Comission
              

Trusts:   

  # Protect from malicious domains. 
  - Action: INHERIT
    Domain: any-firewall.org
  
  # Share disability of EU citizens via members.
  - Role: VAULT
    Query: europa.eu/DISABILITY/CARD
    Domains: 
      - governo.it
      - gov.mt
    
  # Allow transporters to ask SSR of EU citizens.
  - Role: CONSUMER
    Query: europa.eu/DISABILITY/CARD
    Domains: 
      - airlines.any-igo.org     # Any IGO Airlines
    

Codes:

  # Regulate the Disability Card on behalf of the European Union.
  - Delegator: europa.eu
    Path: /DISABILITY/CARD
    Name: Disability Card
        
    Schemas:
      - Output: QR
        Version: 1.0
        Inherits: nlweb.org/TOKEN:1.0
        Format: Name, Surname, DateOfBirth, SerialNumber
 
