
# 🧩 [Schema Code](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): VaultMsgBound
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /VAULT/MSG/BOUND

Description: >
  Message sent by broker, informing that the wallet has accepted a bind
  offered by the vault within the current session.


Schema: 

  Properties:
    - SessionID # The session between the vault and the broker.
    - PublicKey # The public key of the wallet.
    - Binds:    # List of binds accepted by the wallet.
        - ID      # The unique ID of the bind, created by the broker.
        - Code    # The code offered by the vault to be bound.

  Format:
    type: object
    required: [Session, PublicKey]
    properties:

      SessionID:
        $ref: UUID@nlweb.org/TYPES
        descrition: The session between the vault and the broker.

      PublicKey:
        $ref: Key@nlweb.org
        description: The public key of the wallet.

      Binds:
        description: List of binds accepted by the wallet.
        type: array
        items:
          type: object
          required: [ID, Code]
          properties: 

            ID:
              $ref: UUID@nlweb.org/TYPES
              description: The unique ID of the bind, created by the broker.

            Code:
              $ref: Code@nlweb.org/TYPES
              description: The code offered by the vault to be bound.