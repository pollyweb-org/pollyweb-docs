
# 🧩 HostOrderSelf
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /HOST/ORDER/SELF
Name: Order
Description: Token for a self order

Translations:
  - Language: pt-br
    Translation: Encomenda

Schema:  
  Version: 1.0
  Output: QR
  Inherits: nlweb.org/TOKEN:1.0
  
  Properties: 
    - Summary

  Format:
    type: object
    properties:
      Summary:
        type: string   
