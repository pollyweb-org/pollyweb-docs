<!-- #TODO -->

<!-- https://quip.com/EzmaAjGwmvRq#temp:C:bSR232c2e6eecff4c639e0bf6068 -->

# 🧑‍🦰🐌💳 Endorse @ [Payer](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 💳🫥 Payer agent.md>)

## About

   - Flow: [Charge 💵👉🧑‍🦰](<../../5 ⏩ Flows/05 💵⏩ Sellers/02 💵⏩🧑‍🦰 Charge.md>)
   - Caller: 

## Async Message 🐌

- Header:

   - [From 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>): `any-broker.org`
   - [To 💳](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/01 💳🫥 Payer agent.md>): `any-payer.org`
   - [Subject 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>): `Endorse@Payer`

- Body:

   - [BindID 🔗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>): `<bind-uuid>`
   - [Collector 🏦](<../../4 ⚙️ Solution/30 🫥 Agents/04 💳 Payers/03 🏦🛠️ Collector helper.md>): `any-collector.org`
   - Session: 
      - [Host 🤗](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/03 🤗🎭 Host role.md>): `any-seller.org`
      - [Broker 🤵](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>): `any-broker.org`
      - [Locator 🔆](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/22 🔆 Locators/01 🔆 Locator.md>): `<any-locator>`
      - [SessionID 💬](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>): `<session-uuid>`
   - [Charge 💵](<../../5 ⏩ Flows/05 💵⏩ Sellers/02 💵⏩🧑‍🦰 Charge.md>): { ... }

---