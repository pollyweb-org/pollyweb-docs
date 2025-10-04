
# 🧑‍💻 [Hoster](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/05 🧑‍💻🛠️ Hoster helper.md>) Configuration

> From [🏪 Drink at vending machines](<01 🏪 Index.md>)

<br/>

## Locators

| [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) | Purpose
|-|-
| `machine-1` | NFC/QR for customer to tap.

<br/> 

## Roles

| [Roles 🎭](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/00 👥 Domain.md>) | Purpose |
|-|-
| [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | To manage the [Chats 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>).
| [💵 Seller](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 💵🎭 Seller role.md>) | To charge for the products.
| [💼 Consumer](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>) | To verify minimum age.

<br/> 


## Helpers

| [Helper 🛠️](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/05 🛠️👥 Helper domain.md>)  | Purpose |
|-|-
| [🏦 Collector](<../../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 🏦🛠️ Collector helper.md>) | To collect the amount paid.
| [👂 Listener](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/02 👂🛠️ Listener helper.md>) | To propagate [Manifest 📜](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/01 📜 Domain Manifest.md>)  changes.
| [🕸 Graph](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/03 🕸🛠️ Graph helper.md>) | To query [Trust 👍](<../../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/01 👍 Domain Trust.md>) relationships.
| [⏳ Buffer](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/03 ⏳🛠️ Buffer helper.md>) | To buffer inbound [Messages 📨](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>).
| [🛰️ Relayer](<../../../4 ⚙️ Solution/60 🧰 Edge/61 🔌 Pluggables/04 🛰️🛠️ Relayer helper.md>) | To remotely control the machines.

<br/> 


<!-- 
TODO: other scenarios
  * 21 🏢 Plan route 🗺️.md
  * 22 🏢 Load truck 🚚.md
  * 31 🏪 Stock machine 📦.md
-->
