<!-- Docs: https://quip.com/oSzpA7HRICjq/-Broker-Binds#temp:C:DSD2aa2718d92bf4941ac7bb41e9 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L10 -->


# 🗄️🐌🤵 Bind @ Broker

> Called by [🗄️⏩🧑‍🦰 Bind @ Vault](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet chats/...in Prompts 🤔/Bind 👉🗄️🔗/🧑‍🦰 Bind vault ⏩ flow.md>).

> Purpose

* A [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) 
    * offers bindable [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) 
    * to a [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>).


## Async Message  🐌

```yaml
Header:
    From: any-vault.dom
    To: any-broker.dom
    Subject: Bind@Broker
    
Body:
    Chat: <chat-uuid>
    Offer: <offer-uuid>
    Schemas: 
        - any-authority.org/ANY-SCHEMA
```

| Object | Property | Type  | Description | Origin | Purpose
|-|-|-|-|-|-
| Header    |`From`|text|  [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) name
|           |`To`|text| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) name | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|           | `Subject`|text|  `Bind@Broker`
| Body  | `Chat`| uuid | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) | [`Hello@`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| | `Offer`| uuid | [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) hook || [`Bound@`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|  | `Schemas`|list| Bind [Schemas 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) || [`Bound@`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|