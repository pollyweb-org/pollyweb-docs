# 🤵📃 Onboard script

> [Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements [`Onboard@Broker` 🅰️ method](<../🤵🅰️ Broker methods/1 🤵🅰️ Wallets 🧑‍🦰/📣🚀🤵 Onboard.md>)

<br/>

## Script

<!-- TODO: Charge the Notifier -->

```yaml
📃 Onboard:

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

Commands: [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) [`EVAL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/EVAL ⬇️ flow.md>) [`REEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>)

| [Command ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| ⏬ [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) | Get the [Hook 🪝](<../../../35 💬 Chats/😃 Talkers/😃🪣 Talker tables/😃🪣 Hooks 🪝.md>) from [`Bindable@Broker`](<../🤵🅰️ Broker methods/4 🤵🅰️ Binds 🔗/🗄️🐌🤵 Bindable.md>)  
| 💾 [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) | Save the [Bind 🔗](<../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) to the [Wallets 🪣](<../🤵🪣 Broker tables/🤵🪣 Wallets table.md>) table
|
