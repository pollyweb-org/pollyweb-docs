<!-- Tests: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_BINDS_TESTS.py#L53 -->

# 🧑‍🦰🚀🤵 Binds @ Broker

> List the [Binds 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) of a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>).

> Used in:
> <br/> • [🧑‍🦰👉🤵 Translate](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/12 🧑‍🦰👉🤵 Translate.md>)
> <br/> • [🧑‍🦰👉🤵 List binds](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/30 👉🔗 Binds/01 🧑‍🦰👉🤵 List Binds.md>)
> <br/> • [🤵⏩🧑‍🦰 Update Binds 🔗](<../../../5 ⏩ Flows/10 🤵⏩ Brokers/03 🤵⏩🧑‍🦰 Update binds.md>)

<br/>

## Synchronous Request 🚀

```yaml
Header:
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Binds@Broker
Body: 
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) from [`Onboard@Notifier`](<../../65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
|           | `Subject`| string|  `Binds@Broker`
|

<br/>

## Synchronous Response 🚀


```yaml
Binds:
  - BindID: <bind-uuid>
    Vault: any-vault.org
    VaultTitle: AnyVault
    Code: any-authority.org/ANY-CODE
    CodeTitle: Any Code
```

| Object | Property | Type  | Description
|-|-|-|-
| Top      | `Binds`| list  | List of Bind objects
| Bind     | `BindID`   | uuid  | [Bind 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) ID
|          | `Vault`    | string| [Vault 🗄️ domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) name
|          | `VaultTitle`| string| [Vault 🗄️ domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) title
|          | `Code`     | string| [Schema Code 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>)
|          | `CodeTitle`| string| [Schema Code 🧩](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/02 🧩 Schema Code.md>) title
|