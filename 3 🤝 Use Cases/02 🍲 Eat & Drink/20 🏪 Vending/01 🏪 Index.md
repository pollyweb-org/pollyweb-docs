# 🏪 Drink at vending machines  `index`

> Part of [🍲 Eat & Drink use cases](<../🍲 Eat & Drink index.md>)

<br/> 

![alt text](<.📎 Assets/cartoon.png>)

<br/>

## 💬 User Chats

|Persona|[Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) | [Agents 🫥](<../../../4 ⚙️ Solution/25 Data/24 🗄️ Vaults/04 🫥🗄️ Agent vault.md>)
|-|-|-
| `🧑‍🦰 Customer`|[Buy water 💧](<11 💧 Buy water.md>)  | [`💳 Payer`](<../../../4 ⚙️ Solution/30 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>)
| `🧑‍🦰 Customer` | [Buy beer 🍺 21+ ](<12 🍺 Buy beer.md>)| [`🆔 Identity`](<../../../4 ⚙️ Solution/30 🫥 Agents/45 🆔 Identities/01 🆔🫥 Identity agent.md>)  [`💳 Payer`](<../../../4 ⚙️ Solution/30 🫥 Agents/60 💳 Payers/03 💳🎭 Payer role.md>) 
||



<!-- 
TODO: other scenarios
  * 21 🏢 Plan route 🗺️.md
  * 22 🏢 Load truck 🚚.md
  * 31 🏪 Stock machine 📦.md
-->

<br/>

## 🧑‍💻 Business Resources

| Resource | Purpose|
|-|-|
| [🔆 Locators](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) | For scanning: `machine-1` `machine-2`
| [📜 Manifest](<92 📜 Owner: Manifest.md>) | To identify the vending machine domain
| [😃 Talker](<93 😃 Owner: Talker.md>) | To interact with customers
| [🪣 Item map](<94 🪣 Owner: Items.md>) | To list the items available
| [🪣 Locator map](<95 🪣 Owner: Locators.md>) | To map [Locators 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) to [Relayer 🛰️](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/70 🛰️ Relayers/$ 🛰️🛠️ Relayer helper.md>) devices

<br/> 

## 🎭 Domain Roles

| [Roles 🎭](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/00 👥 Domain.md>) | Purpose |
|-|-
| [🤗 Host](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/04 🤗🎭 Host role.md>) | To manage the [Chats 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>)
| [💵 Seller](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/70 💵 Sellers/$ 💵🎭 Seller role.md>) | To charge for the products
| [💼 Consumer](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/27 💼 Consumers/$ 💼🎭 Consumer role.md>) | To verify minimum age

<br/> 


## 🛠️ Domain Helpers

| [Helper 🛠️](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/$ 🛠️ Helpers/$ 🛠️👥 Helper domain.md>)  | Purpose |
|-|-
| [🧑‍💻 Hoster](<91 🧑‍💻 Owner: Hoster.md>) | To bootstrap an inbox API
| [🏦 Collector](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/18 🏦 Collectors/$ 🏦🛠️ Collector helper.md>) | To collect the amount paid
| [👂 Listener](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/50 👂 Listeners/$ 👂🛠️ Listener helper.md>) | To propagate [Manifest 📜](<../../../4 ⚙️ Solution/40 👥 Domains/44 📜 Manifests/$ 📜 Domain Manifest.md>)  changes
| [🕸 Graph](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/40 🕸 Graphs/$ 🕸🛠️ Graph helper.md>) | To query [Trust 👍](<../../../4 ⚙️ Solution/40 👥 Domains/43 👍 Trusts/$ 👍 Domain Trust.md>) relationships
| [⏳ Buffer](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/16 ⏳ Buffers/$ ⏳🛠️ Buffer helper.md>) | To buffer inbound [Messages 📨](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>)
| [🛰️ Relayer](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/70 🛰️ Relayers/$ 🛰️🛠️ Relayer helper.md>) | To remotely control the machines

<br/> 

