<!-- Docs: https://quip.com/HrgkAuQCqBez#temp:C:bXD09ae7595fe4943d5985d83fd0 -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L10 -->


# 🧑‍🦰🚀🤵 Chats @ Broker

> The [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) lists the [Chats 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) of a [Wallet 🧑‍🦰 app](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>).

> Used in:
> <br/>• [🧑‍🦰👉🤵 Set language @ Wallet](<../../../1 🧑‍🦰 Wallets/in App 🏠/🧑‍🦰💬🤵 Translate.md>)
> <br/>• [🧑‍🦰👉🤵 List chats @ Wallet](<../../../1 🧑‍🦰 Wallets/in App 🏠/🧑‍🦰💬🤵 List Chats 💬.md>)
> <br/>• [🤵⏩🗄️ Update chats @ Broker](<../../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Chats 💬.md>)


<br/>

## Synchronous Request 🚀
  
```yaml
Header: 
    From: <wallet-uuid>
    To: any-broker.com
    Subject: Chats@Broker
Body: 
```

| Object | Property | Type  | Description
|-|-|-|-
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../1 🧑‍🦰 Wallets/🧑‍🦰🛠️ Wallet app.md>)  from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../🤵🤲 Broker helper.md>) from [`Onboard@Notifier`](<../../../2 📣 Notifiers/📣🅰️ Notifier methods/1 🤵 Onboard/1 🧑‍🦰🚀📣 Onboard.md>)
|           | `Subject`| string|  `Chats@Broker`
|

<br/>

## Response 


```yaml
Chats:
  - ChatID: <chat-uuid>
    HostTitle: Any Hosts
```

| Object    | Property  | Type  | Description
|-|-|-|-
| Top       | `Chats`     | Chat[]| List of `Chat` objects
| Chat      | `ChatID`        | uuid  | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID
|           | `HostTitle` | string | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) title
|
