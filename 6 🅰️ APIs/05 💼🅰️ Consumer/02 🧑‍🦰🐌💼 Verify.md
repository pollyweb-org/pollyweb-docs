#TODO

<!-- Docs: -->
<!-- Code: -->
<!-- Test: -->


# Verify @ [Consumer 💼](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/25 ✅ 💼 Consumers/04 ✅ 💼🎭 Consumer role.md>) 

## About

- Asynchronous message sent by a Wallet to a [Consumer 💼](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/25 ✅ 💼 Consumers/04 ✅ 💼🎭 Consumer role.md>)
- Tells it to verify the user's [Tokens 🎫](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>)

## Async Message 🐌

- Header:
    - [From 🤵](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/03 ✅ 🤵 Brokers/03 ✅ 🤵 Broker domain.md>): `any-broker.org` 
    - [Subject 📨](<../../4 ⏳ ⚙️ Solution/40 ✅ 👥 Domains/41 ✅ 📨 Comms/01 ✅ 📨 Domain Message.md>): `Verify@Consumer`
- Body: 
    - [ChatID 💬](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/23 ✅ 💬 Chats/01 ✅ 💬 Chat.md>): `<chat-uuid>` 
    - [Tokens 🎫](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>) [ ]: 
        - [Code](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/24 ✅ 🗄️ Vaults/02 ✅ 🧩 Schema Code.md>) 🧩: `airlines.any-igo.org/SSR/WCH:1` 
        - [Issuer 🎴](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/02 ✅ 🎴🎭 Issuer role.md>): `any-issuer.com`
        - [TokenID 🎫](<../../4 ⏳ ⚙️ Solution/20 ✅ 🧑‍🦰 UI/27 ✅ 🎫 Tokens/01 ✅ 🎫 Token.md>): `<token-uuid>`
    

---