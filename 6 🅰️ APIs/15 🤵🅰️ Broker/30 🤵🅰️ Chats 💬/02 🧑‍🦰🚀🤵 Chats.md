<!-- Docs: https://quip.com/HrgkAuQCqBez#temp:C:bXD09ae7595fe4943d5985d83fd0 -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L10 -->


# 🧑‍🦰🚀🤵 Chats @ Broker

> The [Broker 🤵 domain](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) lists the [Chats 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) of a [Wallet 🧑‍🦰 app](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>).

> Used in:
> <br/>• [🧑‍🦰👉🤵 Set language @ Wallet](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/10 👉🤵 Set-up/12 🧑‍🦰👉🤵 Translate.md>)
> <br/>• [🧑‍🦰👉🤵 List chats @ Wallet](<../../../5 ⏩ Flows/90 🧑‍🦰👉 Wallets/20 👉💬 Chats/01 🧑‍🦰👉🤵 List chats.md>)
> <br/>• [🤵⏩🗄️ Update chats @ Broker](<../../../5 ⏩ Flows/10 🤵⏩ Brokers/04 🤵⏩🧑‍🦰 Update Chats 💬.md>)


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
| Header    | `From`| uuid  | [Wallet 🧑‍🦰](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/01 🧑‍🦰 Wallets/$ 🧑‍🦰 Wallet app.md>)  from [`Onboard@Notifier`](<../../65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
|           | `To`  | string| [Broker 🤵](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/03 🤵 Brokers/$ 🤵 Broker domain.md>) from [`Onboard@Notifier`](<../../65 📣🅰️ Notifier/01 📣🤵🅰️ Onboard/11 🧑‍🦰🚀📣 Onboard.md>)
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
| Chat      | `ChatID`        | uuid  | [Chat 💬](<../../../4 ⚙️ Solution/20 🧑‍🦰 UI/12 💬 Chats/$ 💬 Chat.md>) ID
|           | `HostTitle` | string | [Host 🤗 domain](<../../../4 ⚙️ Solution/41 🎭 Domain Roles/30 🤗 Hosts/04 🤗🎭 Host role.md>) title
|
