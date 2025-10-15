# 🗄️🐌🤵 Engage

> Part of [🗄️⏩🧑‍🦰 Engage @ Vault](<../../../5 ⏩ Flows/80 🗄️⏩ Vaults/04 🗄️⏩🧑‍🦰 Engage 💬.md>)

* Allows for [Vault 🗄️ domains](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) 
    * to proactively start a new [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/01 💬 Chat.md>) 
    * with a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/01 🧑‍🦰 Wallet app.md>) previously [bound 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>)
    * in the best interest of the user.

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-vault.com
    To: any-broker.com
    Subject: Help@Broker

Body:
    Bind: <bind-id>
    Locator: any-locator-key
    Parameters: 
        Param1: Value1
        Param2: Value2
```
| Object | Property | Type |Description
|-|-|-|-
| Header | `From`    | string | [Vault 🗄️](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/03 🗄️🎭 Vault role.md>) of the [Bind 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>)
|| `To`      | string | [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/03 🤵 Broker domain.md>) of the [Bind 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>)
|| `Subject` | string | `Engage@Broker`
| Body | `BindID`  | uuid   | [Bind 🔗](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/24 🗄️ Vaults/01 🔗 Bind.md>) of [`.HOST/BIND/SELF` 🧩](<../../../7 🧩 Codes/$/🧩 Vault.md>)
| | `Locator`| string | [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/01 🔆 Locator.md>) for [`Hello@Host`](<../../50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>)
| | `Parameters`| object | Parameters for [`Hello@Host`](<../../50 🤗🅰️ Host/01 🤵🐌🤗 Hello.md>)
|