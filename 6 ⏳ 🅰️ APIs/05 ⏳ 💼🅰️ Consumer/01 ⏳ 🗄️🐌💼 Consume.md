<!-- https://quip.com/UbokAEferibV#temp:C:Yfbbd64684ba1df4ea683cf4e49b -->
# 🗄️🐌💼 Consume @ [Consumer 💼](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/25 ✅ 💼 Consumers/04 ✅ 💼🎭 Consumer role.md>) 


## About

- Asynchronous message sent by a [Vault 🗄️](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>) to a [Consumer 💼](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/25 ✅ 💼 Consumers/04 ✅ 💼🎭 Consumer role.md>) 
- Tells them to collect data shared by a user in a chat.
- Vaults are expected to cache the answer ahead of [Collect 🚀](<../18 ⏳ 🗄️🅰️ Vault/01 ⏳ 💼🚀🗄️ Collect.md>)
- The cache duration is expressed in the TTL field.


## Async Message 🐌

- Header:
    - [From 🗄️](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/03 ✅ 🗄️🎭 Vault role.md>): `any-vault.com` 
    - [Subject 📨](<../../4 ⏳ ⚙️ Solution/40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>): `Consume@Consumer`
- Body:
    - [Chat 💬](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/23 ✅ 💬 Chats/01 ✅ 💬 Chat.md>): 
        - [Broker 🤵](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>): `any-broker.org` 
        - [ChatID 💬](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/23 ✅ 💬 Chats/01 ✅ 💬 Chat.md>): `chat-uuid` 
    - [Bind 🔗](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/01 ✅ 🔗 Bind.md>): 
        - [Code 🧩](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>): `airlines.any-igo.org/SSR/WCH:1` 
        - [Collection 🚀](<../18 ⏳ 🗄️🅰️ Vault/01 ⏳ 💼🚀🗄️ Collect.md>): `<collection-uuid>` 
        - TTL: `2023-04-01T05:00:30.001000Z`

---