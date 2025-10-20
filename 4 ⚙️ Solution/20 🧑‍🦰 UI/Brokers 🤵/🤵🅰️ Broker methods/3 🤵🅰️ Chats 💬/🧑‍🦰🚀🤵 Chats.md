<!-- Docs: https://quip.com/HrgkAuQCqBez#temp:C:bXD09ae7595fe4943d5985d83fd0 -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L10 -->


# 🧑‍🦰🚀🤵 Chats @ Broker

> Implemented by [`Chats` 📃 script](<../../🤵📃 Broker scripts/🤵📃 Chats 🚀.md>)

* The [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) 
    * lists the [Chats 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) 
    * of a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

* Used in:
    * [🧑‍🦰👉🤵 Set language @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in App 🏠/💬🤵 Translate.md>)
    * [🧑‍🦰👉🤵 List chats @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in App 🏠/💬🤵 List Chats 💬.md>)
    * [🤵⏩🗄️ Update chats @ Broker](<../../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Chats 💬.md>)


<br/>

## Synchronous Request 🚀
  
```yaml
Header: 
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Chats@Broker
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `Subject`| string|  `Chats@Broker`
|

<br/>

## Response 


```yaml
Chats:
  - Chat: <chat-uuid>
    Host: any-host.dom
    Host$: Any Host
```

| Object    | Property  | Type  | Description
|-|-|-|-
| Top       | `Chats`     | Chat[]| List of `Chat` objects
| Chat      | `Chat`        | uuid  | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) from [`Converse@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
|           | `Host` | string | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) name
|           | `Host$` | string | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) title from [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
|


<br/>
