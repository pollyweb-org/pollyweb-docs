# 🗄️🐌🤵 Engage

> Part of [🗄️⏩🧑‍🦰 Engage @ Vault](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️⏩ Vault flows/🗄️⏩🧑‍🦰 Engage 💬.md>)

* Allows for [Vault 🗄️ domains](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) 
    * to proactively start a new [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) 
    * with a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/🧑‍🦰 Wallet app.md>) previously [bound 🔗](<../../../4 ⚙️ Solution/30 🧩 Data/20 🔗 Binds/🔗 Bind.md>)
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
| Header | `From`    | string | [Vault 🗄️](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/80 🗄️ Vaults/🗄️🎭 Vault role.md>) of the [Bind 🔗](<../../../4 ⚙️ Solution/30 🧩 Data/20 🔗 Binds/🔗 Bind.md>)
|| `To`      | string | [Broker 🤵](<../../../4 ⚙️ Solution/45 🤲 Helper domains/24 🤵 Brokers/$ 🤵 Broker domain.md>) of the [Bind 🔗](<../../../4 ⚙️ Solution/30 🧩 Data/20 🔗 Binds/🔗 Bind.md>)
|| `Subject` | string | `Engage@Broker`
| Body | `BindID`  | uuid   | [Bind 🔗](<../../../4 ⚙️ Solution/30 🧩 Data/20 🔗 Binds/🔗 Bind.md>) of [`.HOST/BIND/SELF` 🧩](<../../../7 🧩 Codes/$/🧩 VAULT code.md>)
| | `Locator`| string | [Locator 🔆](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/11 🔆 Locators/$ 🔆 Locator.md>) for [`Hello@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
| | `Parameters`| object | Parameters for [`Hello@Host`](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/🤗🅰️ Host methods/🤵🐌🤗 Hello.md>)
|