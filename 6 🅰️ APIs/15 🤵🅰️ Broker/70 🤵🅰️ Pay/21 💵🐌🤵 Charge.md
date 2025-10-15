<!-- #TODO -->

<!-- Docs: https://quip.com/NBngAvaOflZ6#temp:C:FIJf947d432d602429aae120dcaf -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_PAY_TESTS.py#L10 -->


# 💵🐌🤵 Charge @ [Broker](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>)


## About

- Flow: [Charge 💵👉🧑‍🦰 ](<../../../5 ⏩ Flows/75 💵⏩ Sellers/02 💵⏩🧑‍🦰 Charge.md>)
- Previous: [Charge 💵👉🧑‍🦰](<../../../5 ⏩ Flows/75 💵⏩ Sellers/02 💵⏩🧑‍🦰 Charge.md>)
- Next: [Charge@Notifier 🤵💵🐌📣](<../../65 📣🅰️ Notifier/05 📣💳🅰️ Payments/61 🤵🐌📣 Charge.md>)


## Async Message 

|Property|Type|Description
|-|-|-


- Header:
    - [From 💵](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/70 💵 Sellers/$ 💵🎭 Seller role.md>): `any-seller.org`
    - [To 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>): `any-broker.com`
    - [Subject 📨](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/01 📨 Domain Message.md>): `Charge@Broker`
- Body:
    - [ChatID 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>): `<session-uuid@seller>`
    - Statement: `<reason-for-charge>`
    - Charge:
        - ChargeID: `<charge-uuid@seller>`
        - Amount: `12.34`
        - Currency: `EUR`
        - Operation: `DEBIT`
        - [Collectors 🏦](<../../../4 ⚙️ Solution/45 🛠️ Helper domains/18 🏦 Collectors/$ 🏦🛠️ Collector helper.md>): [ `revolut.com`, `paypal.com` ]

---