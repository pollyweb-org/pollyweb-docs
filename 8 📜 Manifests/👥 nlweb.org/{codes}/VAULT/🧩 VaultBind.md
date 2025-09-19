
# 🧩 [Schema Code](<../../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): VaultBind
```yaml
🤝: nlweb.org/MANIFEST/CODE

Path: /VAULT/BIND
Name: Vault Registration

Resources:
  NLWEBB: 🗄️ https://quip.com/IZapAfPZPnOD

Description: >
  Allows wallets to register on vaults.
  * 1. Vaults offer this bindable code for wallets;
  * 2. Wallets tell their broker that they accept the bind;
  * 3. Brokers create a sharable canonical BindID;
  * 3. Brokers send the BindID and the Wallet's public key to the vault;
  * 4. Vaults attach the BindID and the public key to an internal VaultID.

  When wallets check-in to vaults:
  * 1. Brokers send the bindID to the vault in the session check-in;
  * 2. Vaults lookup the VaultID by BindID.

  When wallets send messages directly to vaults:
  * 1. Vaults validate the signature with the public key of the bind.