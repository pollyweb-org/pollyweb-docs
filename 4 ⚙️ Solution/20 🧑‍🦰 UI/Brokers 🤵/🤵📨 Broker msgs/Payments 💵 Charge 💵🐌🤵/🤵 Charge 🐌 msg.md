# 💵🐌🤵 Charge @ [Broker](<../../🤵/🤵 Broker 🤲 helper.md>)


## About

- Flow: [Charge 💵👉🧑‍🦰 ](<../../../../41 🎭 Domain Roles/Sellers 💵/💵⏩ Seller flows/Charge 💵⏩🧑‍🦰/💵 Charge ⏩ flow.md>)
- Previous: [Charge 💵👉🧑‍🦰](<../../../../41 🎭 Domain Roles/Sellers 💵/💵⏩ Seller flows/Charge 💵⏩🧑‍🦰/💵 Charge ⏩ flow.md>)
- Next: [Charge@Notifier 🤵💵🐌📣](<../../../Notifiers 📣/📣📨 Notifier msgs/Payments 💳 Charge 🤵🐌📣/📣 Charge 🐌 msg.md>)


## Async Message 

|Property|Type|Description
|-|-|-


- Header:
    - [From 💵](<../../../../41 🎭 Domain Roles/Sellers 💵/💵 Seller /💵🎭 Seller role.md>): `any-seller.dom`
    - [To 🤵](<../../🤵/🤵 Broker 🤲 helper.md>): `any-broker.dom`
    - [Subject 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>): `Charge@Broker`
- Body:
    - [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>): `<session-uuid@seller>`
    - Text: `<reason-for-charge>`
    - Charge:
        - ChargeID: `<charge-uuid@seller>`
        - Amount: `12.34`
        - Currency: `EUR`
        - Operation: `DEBIT`
        - [Collectors 🏦](<../../../../45 🤲 Helper domains/Collectors 🏦/🏦 Collector/🏦🤲 Collector helper.md>): [ `revolut.com`, `paypal.com` ]

---