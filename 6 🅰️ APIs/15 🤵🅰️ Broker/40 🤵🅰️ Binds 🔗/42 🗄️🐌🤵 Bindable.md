<!-- Docs: https://quip.com/oSzpA7HRICjq/-Broker-Binds#temp:C:DSD2aa2718d92bf4941ac7bb41e9 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L10 -->


# 🗄️🐌🤵 Bindable @ Broker

> The [Vault 🗄️ domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) offers bindable [Schema Codes 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) to the [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>).

> Called by [🗄️⏩🧑‍🦰 Bind @ Vault](<../../../5 ⏩ Flows/09 🗄️⏩ Vaults/01 🗄️⏩🧑‍🦰 Bind.md>).

<br/>

## Async Message  🐌

```yaml
Header:
    From: any-vault.com
    To: any-broker.com
    Subject: Bindable@Broker
Body:
    ChatID: <chat-uuid>
    Codes: 
      - any-authority.org/ANY-CODE
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| string  |  [Vault 🗄️ domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) name
|           | `To`  | string| [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) name
|           | `Subject`| string|  `Bindable@Broker`
| Body  | `ChatID`| UUID | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/23 💬 Chats/01 💬 Chat.md>) ID
| | `Codes`| string[] | List of [Schema Codes 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|