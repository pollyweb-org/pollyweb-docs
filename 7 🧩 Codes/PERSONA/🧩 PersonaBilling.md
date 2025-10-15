
# [🧩](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/02 🧩 Schema Code.md>): PersonaBilling

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

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
    