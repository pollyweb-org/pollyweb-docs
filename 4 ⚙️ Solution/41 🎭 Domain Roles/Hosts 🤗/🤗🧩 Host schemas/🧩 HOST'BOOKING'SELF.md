
# [🧩](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>) [Schema Code](<../../../30 🧩 Data/Schema Codes 🧩/🧩 Schema Code.md>): HostBookingSelf

> Brokers only share these credentials with the issuers - i.e. if there’s a booking for a medical appointment and a restaurant, the user is only asked to share the restaurant booking when checking into the restaurant (not the medical appointment).

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../40 👥 Domains/👥📜 Domain Manifests/🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /HOST/BOOKING/SELF
Description: Token for a self booking.

Schema:
  Version: 1.0
  Inherits: nlweb.dom/HOST/BOOKING:1.0