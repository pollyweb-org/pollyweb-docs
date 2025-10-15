
# [🧩](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) [Schema Code](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): HostBookingSelf

> Brokers only share these credentials with the issuers - i.e. if there’s a booking for a medical appointment and a restaurant, the user is only asked to share the restaurant booking when checking into the restaurant (not the medical appointment).

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/11 🧩 CODE code.md>)

```yaml
Path: /HOST/BOOKING/SELF
Description: Token for a self booking.

Schema:
  Version: 1.0
  Inherits: nlweb.org/HOST/BOOKING:1.0