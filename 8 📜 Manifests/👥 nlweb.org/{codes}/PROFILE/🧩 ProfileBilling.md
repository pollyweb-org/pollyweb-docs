
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): ProfileBilling
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /PROFILE/BILLING
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
        $ref: Country@nlweb.org/PROFILE/ADDRESS:1.0

      Address:
        $ref: Address@nlweb.org/PROFILE/ADDRESS:1.0
    