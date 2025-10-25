<!-- #TODO -->

<!-- Docs: https://quip.com/NBngAvaOflZ6#temp:C:FIJf947d432d602429aae120dcaf -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_PAY_TESTS.py#L10 -->


# 💵🐌🤵 Charge @ [Broker](<../../🤵🤲 Broker helper.md>)


## About

- Flow: [Charge 💵👉🧑‍🦰 ](<../../../../41 🎭 Domain Roles/Sellers 💵/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>)
- Previous: [Charge 💵👉🧑‍🦰](<../../../../41 🎭 Domain Roles/Sellers 💵/💵⏩ Seller flows/💵⏩🧑‍🦰 Charge.md>)
- Next: [Charge@Notifier 🤵💵🐌📣](<../../../Notifiers 📣/📣🅰️ Notifier methods/📣 Payments 💳 Charge 🤵🐌📣/Charge 🐌 msg.md>)


## Async Message 

|Property|Type|Description
|-|-|-


- Header:
    - [From 💵](<../../../../41 🎭 Domain Roles/Sellers 💵/💵🎭 Seller role.md>): `any-seller.dom`
    - [To 🤵](<../../🤵🤲 Broker helper.md>): `any-broker.dom`
    - [Subject 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>): `Charge@Broker`
- Body:
    - [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>): `<session-uuid@seller>`
    - Statement: `<reason-for-charge>`
    - Charge:
        - ChargeID: `<charge-uuid@seller>`
        - Amount: `12.34`
        - Currency: `EUR`
        - Operation: `DEBIT`
        - [Collectors 🏦](<../../../../45 🤲 Helper domains/Collectors 🏦/🏦🤲 Collector helper.md>): [ `revolut.com`, `paypal.com` ]

---