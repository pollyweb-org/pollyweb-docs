<!-- TODO: add the code -->
<!-- TODO: add a script diagram -->

# 🗄️🐌🤵 Engage

> Part of [🗄️⏩🧑‍🦰 Engage @ Vault](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️⏩ Vault flows/Engage 🗄️⏩💬/🗄️ Engage ⏩ flow.md>)


> Purpose

* Allows for [Vault 🗄️ domains](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) 
    * to proactively start a new [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) 
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
| Object | Property | Type |Description| Origin|Purpose
|-|-|-|-|-|-
| Header |`From`|domain| [Vault 🗄️](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🎭 Vault role.md>) | [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
||`To`|domain| [Broker 🤵](<../../🤵🤲 Broker helper.md>) | [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
|| `Subject` | string | `Engage@Broker`
| Body | `Bind`  | uuid   | [Bind 🔗](<../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) of <br/> [`.HOST/BIND/SELF`](<../../../../../7 🧩 Codes/$/🧩 VAULT code.md>) | [`Bound@Vault`](<../../../../41 🎭 Domain Roles/Vaults 🗄️/🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)
| | `Locator`| string | [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) || [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
| | `Parameters`| object | Parameters || [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|