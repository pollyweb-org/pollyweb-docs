# 📥🛠️ Inboxer helper domain


1. **What is an Inboxer?**

    An [Inboxer 📥 helper domain](<03 📥🛠️ Inboxer helper.md>) is
    * any [Helper 🛠️ domain](<../24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)
    * that sends and receives [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) on behalf of a client [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>)
    * proxying incoming [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) to an HTTP endpoint in the client
    * and signing the client's outbound [Messages 📨](<../../40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>) to other [domains 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>).

    ---
    <br>


1. **What roles do Inboxers typically implement?**

    | [Role 🎭](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | Purpose
    |-|-
    | [🗄️ Vault](<../24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) | To store the [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) settings.
    | [🎴 Issuer](<../25 🎫 Tokens/02 🎴🎭 Issuer role.md>) | To issue [domain 👥](<../../40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) ownership [Tokens 🎫](<../25 🎫 Tokens/01 🎫 Token.md>).    

    ---
    <br/>


