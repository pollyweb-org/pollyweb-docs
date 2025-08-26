<!-- https://quip.com/rKzMApUS5QIi#temp:C:WTI8724d650e2ae45dabb56baea4 -->

# 💼🐌🤵  Query @ [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)


## About

- Request:
    - Codes[]: → list of codes for which to return a vault and/or credential.
    - Vaults[]: → list of potential vaults for the user to bind to.
- Behavior:
    * For all credentials, only show the ones that are active;
        - i.e., within the start and expiration date.
    * For the following credentials types, only show the credentials issued by the consumer itself:
        * `🧩 //BOOKING/SELF: 🤝🤗 Host.nlweb.org`
        * `🧩 //ORDER: 🤝🤗 Host.nlweb.org`



## Async Message

- Header:
    - [From 💼](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/27 💼 Consumers/04 💼🎭 Consumer role.md>): `any-consumer.com`
    - [Subject 📨](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>): `Query@Broker`
- Body:
    - [ChatID 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>): `<chat-uuid>` 
    - Codes [ ]:
        - [Code 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>): `airlines.any-igo.org/SSR/WCH:1` 
        - Vaults [ ]:
            - [Vault 🗄️](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>): `any-vault.com`

---