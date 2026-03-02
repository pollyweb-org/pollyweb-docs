# 🧑‍🦰🐌🤵 Locate @ Broker

> Implementation
* Implemented by [`Locate@Broker` 📃 script](<🤵 Locate 📃 handler.md>)

> Flow
* Part of the [`Locate` ⏩ flow](<../../🤵⏩ Broker flows/Locate 🔆⏩🤵/🤵 Locate ⏩ flow.md>)
* Precedes [`Open@Notifier` 🅰️](<../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) method

> Purpose
* Parses the [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) in the [Broker 🤵 domain](<../../🤵/🤵 Broker 🤲 helper.md>).
    * If the [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) is [`.ALIAS 🧩`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>) 
    * then it needs to be be resolved by a [Printer 🖨️ helper domain](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🤲 Printer helper.md>)
    * into the final [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>).


## Async Message 🐌

```yaml
Header:
    From: <wallet-id>
    To: any-broker.dom
    Subject: Locate@Broker
    
Body:
    Hook: <hook-uuid>
    Locator: .ALIAS,any-printer.dom,7V8KD3G
    Inputs:
        A: 1
        B: 2
```

|Object|Property|Type|Description|Origin|Purpose
|-|-|-|-|-|-
|Header|`From`|uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`To`|text| [Broker 🤵](<../../🤵/🤵 Broker 🤲 helper.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 call.md>)
||`Subject`|text|`Locate@Broker`
|Body  |`Locator` |text| Host [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) || [`Hello@Host`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗📨 Host msgs/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>)
|||| Schemas [`.HOST`](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🧩 Host schemas/🧩 HOST.md>) [`.ALIAS`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
|| `Hook` | uuid | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) Hook || [`Open@`](<../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
|| `Inputs` | object | Custom parameters | | [`Chat@`](<../Chats 💬 Chat 🤗🚀🤵/🤵 Chat 🚀 call.md>)
|

