<!-- Docs: https://quip.com/HrgkAuQCqBez#temp:C:bXD09ae7595fe4943d5985d83fd0 -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L10 -->


# 🧑‍🦰🚀🤵 Chats @ Broker

> The [Broker 🤵 domain](<../../🤵🤲 Broker helper.md>) lists the [Chats 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) of a [Wallet 🧑‍🦰 app](<../../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>).

> Used in:
> <br/>• [🧑‍🦰👉🤵 Set language @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in App 🏠/💬🤵 Translate.md>)
> <br/>• [🧑‍🦰👉🤵 List chats @ Wallet](<../../../Wallets 🧑‍🦰/🧑‍🦰💬 Wallet in App 🏠/💬🤵 List Chats 💬.md>)
> <br/>• [🤵⏩🗄️ Update chats @ Broker](<../../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Chats 💬.md>)


<br/>

## Synchronous Request 🚀
  
```yaml
Header: 
    From: <wallet-uuid>
    To: any-broker.dom
    Subject: Chats@Broker
Body: 
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
    Title: Any Hosts
```

| Object    | Property  | Type  | Description
|-|-|-|-
| Top       | `Chats`     | Chat[]| List of `Chat` objects
| Chat      | `Chat`        | uuid  | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) ID
|           | `Title` | string | [Host 🤗 domain](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) title
|


<br/>

## Handler

```yaml
# Get the wallet item
- GET >> $wallet:
    Pool: Wallets@Broker
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg|$wallet.PublicKey

# Get the Hosts
- EVAL|$wallet.Chats >> $hosts:
    .Host

# Translate the hosts
- MSG >> $translations:
    Subject: Translate@Graph
    Language: $wallet.Language
    Domains: $hosts

# Prepare the response
- EVAL|$wallet.Chats >> $chats:
    Chat: .Chat
    Title: 

# Add the titles
- CROSS|$chats:
    With: $translations.Domains
    When: .Host = .Domain
    Then: .Title = .Translation

# Respond
- REEL:
    $chats
```

| [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| ⏬ [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) | Get the [Hook 🪝](<../../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 Hooks 🪝.md>) from [`Bindable@Broker`](<../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)  
| 🔐 [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>) | Verify the  [Signature 🔏](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Signatures 🔏.md>) of the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| ⬇️ [`EVAL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/EVAL ⬇️ flow.md>) | Format the items from the  [Chats 🪣 table](<../../🤵🪣 Broker tables/🤵🪣 Chats.md>)
| 🎣 [`REEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) | Respond to the [Synchronous Request 🚀](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Request Sync 🚀.md>)
|
