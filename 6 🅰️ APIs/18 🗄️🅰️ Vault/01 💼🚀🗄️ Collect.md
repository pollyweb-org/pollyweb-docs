<!-- #TODO -->

<!-- https://quip.com/IZapAfPZPnOD#temp:C:PDZ67394972376e4fb8979d41209 -->


# 💼🚀🗄️ Collect @ [Vault](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)


## About

- Synchronous request sent from a [Consumer 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 💼 Consumers/04 💼🎭 Consumer role.md>) to a [Vault 🗄️](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>)
- Tells it to reply with the data [shared](<../05 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>) by the user.
- Allows HTTP responses have no theoretical size limit.
- Callers expect the response to be cached during [Consume 🐌](<../05 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>)
- The message is rejected if the TTL is exceeded.


## Request 🚀

- Header:
    - [From 💼](<../../4 ⚙️ Solution/20 🧑‍🦰 UI/25 💼 Consumers/04 💼🎭 Consumer role.md>): `any-consumer.com`
    - [Subject 📨](<../../4 ⚙️ Solution/40 👥 Domains/41 📨 Comms/01 📨 Domain Message.md>): `Collect@Vault`
- Body:
    - [Collection 🚀](<../05 💼🅰️ Consumer/01 🗄️🐌💼 Consume.md>): `6704488d-fb53-446d-a52c-a567dac20d20` 

---