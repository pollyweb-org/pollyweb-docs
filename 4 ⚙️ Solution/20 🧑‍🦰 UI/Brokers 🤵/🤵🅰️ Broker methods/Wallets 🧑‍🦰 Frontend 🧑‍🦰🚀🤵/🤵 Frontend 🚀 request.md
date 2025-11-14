<!-- Docs: https://quip.com/HrgkAuQCqBez#temp:C:bXD09ae7595fe4943d5985d83fd0 -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L10 -->


# 🧑‍🦰🚀🤵 Chats @ Broker

> Implementation 
* Implements the [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
* Implemented by the [`Chats` 📃 script](<🤵 Frontend 📃 handler.md>)

> Purpose
* The [Broker 🤵 domain](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) 
    * lists the [Chats 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) 
    * of a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>).



## Synchronous Request 🚀
  
```yaml
Header: 
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Chats@Broker
```

| Object | Property | Type  | Description|Origin
|-|-|-|-|-
| Header    |`From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|           |`To`|domain| [Broker 🤵](<../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`Onboard@`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Onboard 🧑‍🦰🚀📣/📣 Onboard 🚀 request.md>)
|           | `Subject`| string|  `Chats@Broker`
|



## Response 


```yaml
Chats:
  - Chat: <chat-uuid>
    Host: any-host.dom
    Host$: Any Host
```

| Object    | Property  | Type  | Description
|-|-|-|-
| Chats      | `Chat`        | uuid  | [Chat 💬](<../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) from [`Open@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
|           | `Host` | string | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name
|           | `Host$` | string | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) title from [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|


<br/>
