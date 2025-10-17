<!-- Docs: https://quip.com/oSzpA7HRICjq/-Broker-Binds#temp:C:DSD2aa2718d92bf4941ac7bb41e9 -->
<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L10 -->


# 🗄️🐌🤵 Bindable @ Broker

> Called by [🗄️⏩🧑‍🦰 Bind @ Vault](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in Prompts 🤔/👉🗄️ Bind 🔗.md>).


* A [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) 
    * offers bindable [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) 
    * to a [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>).


<br/>

## Async Message  🐌

```yaml
Header:
    From: any-vault.dom
    To: any-broker.dom
    Subject: Bindable@Broker
    
Body:
    ChatID: <chat-uuid>
    Codes: 
      - any-authority.org/ANY-CODE
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| string  |  [Vault 🗄️ domain](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) name
|           | `To`  | string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
|           | `Subject`| string|  `Bindable@Broker`
| Body  | `ChatID`| uuid | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID from [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
| | `Codes`| string[] | List of [Schema Codes 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)
|