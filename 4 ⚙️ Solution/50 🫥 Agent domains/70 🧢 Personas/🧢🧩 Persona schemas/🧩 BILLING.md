
# [🧩](<../../../30 Data/🧩 Schema Codes/🧩 Schema Code.md>) [Schema Code](<../../../30 Data/🧩 Schema Codes/🧩 Schema Code.md>): PersonaBilling

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /PERSONA/BILLING
Name: Billing address

Translations:
  pt: Endereço de pagamento

Schemas:  
  
  Properties:
    - Buyer           # name of the buyer
    - TaxNumber       # business/personal tax number - e.g. VAT
    - Country         # Country@//ADDRESS
    - Address         # Address@//ADDRESS
  
  Format:
    type: object
    required: [Buyer, Country, Address]
    properties:

      Buyer:
        type: string

      TaxNumber:
        type: string

      Country: 
        $ref: Country@nlweb.org/PERSONA/ADDRESS:1.0

      Address:
        $ref: Address@nlweb.org/PERSONA/ADDRESS:1.0
    