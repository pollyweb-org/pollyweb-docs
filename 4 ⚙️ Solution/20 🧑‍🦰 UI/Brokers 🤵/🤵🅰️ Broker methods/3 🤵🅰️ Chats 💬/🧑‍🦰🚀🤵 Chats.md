<!-- Docs: https://quip.com/HrgkAuQCqBez#temp:C:bXD09ae7595fe4943d5985d83fd0 -->
<!-- Test: https://github.com/jorgemjfonseca/domain-trust-framework/blob/2896911396280f90ec68c32b50aa99dc4a3c90e2/python/roles/broker/BROKER_SESSIONS_TESTS.py#L10 -->


# 🧑‍🦰🚀🤵 Chats @ Broker

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
    Title: Any Hosts
```

| Object    | Property  | Type  | Description
|-|-|-|-
| Top       | `Chats`     | Chat[]| List of `Chat` objects
| Chat      | `Chat`        | uuid  | [Chat 💬](<../../../../35 💬 Chats/💬 Chats/💬 Chat.md>) from [`Converse@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>)
|           | `Title` | string | [Host 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🎭 Host role.md>) title from [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
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

# Translate the hosts
- SEND >> $translations:
    Subject: Translate@Graph
    Language: $wallet.Language
    Domains: $wallet.Hosts

# Add the titles
- MERGE >> $chats:
    Lists: 
        $wallet.Chats
        $translations.Domains
    Match: 
        Host: Domain
    Eval: 
        Title: Translation
    Output: 
        Chat: Chat
        Title: Translation

# Respond
- REEL:
    $chats
```

| [Command ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| ⏬ [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) | Get the [Wallet 🪣 item](<../../🤵🪣 Broker tables/🤵🪣 Wallets.md>)
| 🔐 [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>) | Verify the  [Signature 🔏](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Signatures 🔏.md>) of the [Message 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| 📬 [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) | Call [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| 🧬 [`MERGE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/MERGE 🧬 lists.md>) | Add the translations to the dataset
| 🎣 [`REEL`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) | Respond to the [Synchronous Request 🚀](<../../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Request Sync 🚀.md>)
|
