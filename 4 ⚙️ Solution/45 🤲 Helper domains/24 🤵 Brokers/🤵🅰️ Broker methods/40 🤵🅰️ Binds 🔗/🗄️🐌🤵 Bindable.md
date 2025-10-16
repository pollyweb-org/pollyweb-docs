<!-- Docs: https://quip.com/oSzpA7HRICjq/-Broker-Binds#temp:C:DSD2aa2718d92bf4941ac7bb41e9 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L10 -->


# 🗄️🐌🤵 Bindable @ Broker

> Called by [🗄️⏩🧑‍🦰 Bind @ Vault](<../../../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/02 🧑‍🦰👉🗄️ Bind 🔗.md>).


* A [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) 
    * offers bindable [Schema Codes 🧩](<../../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>) 
    * to a [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>).


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
| Header    | `From`| string  |  [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) name
|           | `To`  | string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Hello@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
|           | `Subject`| string|  `Bindable@Broker`
| Body  | `ChatID`| uuid | [Chat 💬](<../../../../35 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<../../../../41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
| | `Codes`| string[] | List of [Schema Codes 🧩](<../../../../30 Data/10 🧩 Schema Codes/🧩 Schema Code.md>)
|