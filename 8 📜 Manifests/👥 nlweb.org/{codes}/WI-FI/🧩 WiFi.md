
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): WiFi
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /WI-FI
Description: Enabling wi-fi for things.

Resources:
  NLWEB: 🤝📶 https://quip.com/sDX4ArZbzqua/-Wi-FiNLWEBorg

Schemas:
  Version: 1.0
  Inherits: nlweb.org/LOCATOR:1.0
  
  Properties:
    - NetworkName   #string
    - Hidden        #boolean
    - Password      #string
    - Encryption    #string: [NONE, WPA/WPA2, WEP]

  Format:
    type: object
    properties:
        NetworkName:
          type: string
        Hidden:
          type: boolean
        Password:
          type: string
        Encryption:
          type: string
          enum:
          - NONE
          - WPA/WPA2
          - WEP