
# [🧩](<../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) [`HOST`](<🧩 HOST.md>)/[`BOOKING`](<🧩 HOST'BOOKING.md>)/`SELF`

Brokers only share these credentials with the issuers;
  * i.e. if there’s a booking for a medical appointment and a restaurant, the user is only asked to share the restaurant booking when checking into the restaurant (not the medical appointment).

<br/>

## Definition

> 🤝: [`.MANIFEST/CODE`](<../../../30 🧩 Data/Manifests 📜/📜🧩 Manifest schemas/🧩 CODE.md>)

```yaml
Path: /HOST/BOOKING/SELF
Description: Token for a self booking.

Blueprint:
  Version: 1.0
  Inherits: nlweb.dom/HOST/BOOKING:1.0