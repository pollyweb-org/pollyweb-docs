# 🗄️🐌🤵 Engage

> Part of [🗄️⏩🧑‍🦰 Engage @ Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⏩ Vault flows/🗄️⏩🧑‍🦰 Engage 💬 flow.md>)

* Allows for [Vault 🗄️ domains](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) 
    * to proactively start a new [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) 
    * with a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) previously [bound 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
    * in the best interest of the user.

<br/>

## Async Message 🐌

```yaml
Header:
    From: any-vault.dom
    To: any-broker.dom
    Subject: Join@Broker

Body:
    Bind: <bind-id>
    Locator: any-locator-key
    Parameters: 
        Param1: Value1
        Param2: Value2
```
| Object | Property | Type |Description
|-|-|-|-
| Header | `From`    | string | [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) of the [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
|| `To`      | string | [Broker 🤵](<../../🤵🤲 Broker helper.md>) of the [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>)
|| `Subject` | string | `Engage@Broker`
| Body | `Bind`  | uuid   | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) of [`.HOST/BIND/SELF` 🧩](<../../../../../7 🧩 Codes/$/🧩 VAULT code.md>)
| | `Locator`| string | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) for [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| | `Parameters`| object | Parameters for [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|