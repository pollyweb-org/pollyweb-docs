# 🤵▶️ Onboard script

> [Script ▶️](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/▶️ Script.md>) that implements [`Onboard@Broker` 🅰️ method](<../🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>)

<br/>

## Script

```yaml
# Get the Notifier
# GET|Notifiers@Broker|$.Msg.From >> $notifier

# Generate a new Wallet ID
- EVAL|.UUID >> $wallet

# Save the Wallet
- SAVE|Wallets@Broker:
    Wallet: $wallet
    Notifier: $.Msg.From
    PublicKey: $.Msg.PublicKey
    Language: $.Msg.Language

# Return the ID
- REEL:
    $wallet
```


| [Command ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| ⏬ [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) | Get the [Hook 🪝](<../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 Hooks 🪝.md>) from [`Bindable@Broker`](<../🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)  
| 💾 [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) | Save the [Bind 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to the [Wallets 🪣](<../🤵🪣 Broker tables/🤵🪣 Wallets.md>) table
| 🎣 [`REEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) | Respond to the [Synchronous Request 🚀](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Request Sync 🚀.md>)
|
