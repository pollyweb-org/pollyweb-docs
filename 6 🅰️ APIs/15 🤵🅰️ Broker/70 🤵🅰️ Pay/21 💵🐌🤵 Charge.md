<!-- #TODO -->

<!-- Docs: https://quip.com/NBngAvaOflZ6#temp:C:FIJf947d432d602429aae120dcaf -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_PAY_TESTS.py#L10 -->


# 💵🐌🤵 Charge @ [Broker](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>)


## About

- Flow: [Charge 💵👉🧑‍🦰 ](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/70 💵 Sellers/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>)
- Previous: [Charge 💵👉🧑‍🦰](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/70 💵 Sellers/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>)
- Next: [Charge@Notifier 🤵💵🐌📣](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/02 📣 Notifiers/🅰️ Notifier methods/5 💳 Payments/🤵🐌📣 Charge.md>)


## Async Message 

|Property|Type|Description
|-|-|-


- Header:
    - [From 💵](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/70 💵 Sellers/💵🎭 Seller role.md>): `any-seller.org`
    - [To 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>): `any-broker.com`
    - [Subject 📨](<../../../4 ⚙️ Solution/40 👥 Domains/41 📨 Messages/📨 Message.md>): `Charge@Broker`
- Body:
    - [ChatID 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>): `<session-uuid@seller>`
    - Statement: `<reason-for-charge>`
    - Charge:
        - ChargeID: `<charge-uuid@seller>`
        - Amount: `12.34`
        - Currency: `EUR`
        - Operation: `DEBIT`
        - [Collectors 🏦](<../../../4 ⚙️ Solution/45 🤲 Helper domains/30 🏦 Collectors/$ 🏦🤲 Collector helper.md>): [ `revolut.com`, `paypal.com` ]

---