
# 📜 [Manifest](<../../../4 ⚙️ Solution/30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>): ec.europa.eu
<!--# 🇪🇺 https://quip.com/bBbpAAGfOCIz/-Europaeu-->

> Inherits from [`pollyweb.org/TOKEN 🧩`](<../../../4 ⚙️ Solution/30 🧩 Data/Tokens 🎫/🧩 Token schemas/🧩 TOKEN.md>)

```yaml
🤝: pollyweb.org/MANIFEST

About:
  Domain: ec.europa.eu
  Title: European Commission
```       
       
```yaml
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
      - airlines.any-igo.dom     # Any IGO Airlines
```    

```yaml
Schemas:

  # Regulate the Disability Card on behalf of the European Union.
  - Delegator: europa.eu
    Path: /DISABILITY/CARD
    Title: Disability Card
        
    Schemas:
      - Version: 1.0
        Inherits: pollyweb.org/TOKEN:1.0
        Format: Name, Surname, DateOfBirth, SerialNumber
```