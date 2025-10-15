
# [🧩](<../../4 ⚙️ Solution/25 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/25 🧩 Data/10 🧩 Schema Codes/$ 🧩 Schema Code.md>): IdentitySelfie

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/40 🧩 CODE code.md>)

```yaml
Path: /IDENTITY/SELFIE
Name: Face verification

Description: >
  Used by vaults to authenticate users before disclosures.
  * On AWS, see Rekognition Face Liveness - mzraghib@. 

Schema:
  Version: 1.0

  Properties:
    - OrderID   # Return of Order@Selfie(Pictures:list[str])
    - Liveness  # Percentage of confidence that it was a live selfie.
    - Match     # Percentage of confidence that it was the person in the pictures.
  
  Format:
    type: object
    require: [OrderID, Liveness, Match]
    properties:

      OrderID:
        type: string
        format: uuid
        description: > 
          Return of Order@Selfie(Pictures:list[str]).
          A vault must first order the selfie to be taken:
          1. Sends the list of pictures in base64 to the Selfie;
          2. Receive the OrderID as an UUID in a sync response;
          3. Send the OrderID as a token to the session's Broker.
      
      Liveness:
        type: integer
        minimum: 10
        maximum: 100
        description: > 
          Percentage of confidence that it was a live selfie.
          This is to detect fraude.
          
      Match:
        type: integer
        minimum: 10
        maximum: 100
        description: > 
          Percentage of confidence that it was the person in the pictures.
          This is done by comparing the picture taken with the ones given 
          by the vault when it invoked the Order@Selfie.

  