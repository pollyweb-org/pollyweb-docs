# 🤵📃 Chats 🚀 Broker

> [Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements [`Chats@Broker`](<../🤵🅰️ Broker methods/3 🤵🅰️ Chats 💬/🧑‍🦰🚀🤵 Chats.md>)


<br/>

## Script

```yaml
📃 Chats@Broker:

# Get the wallet item
- GET >> $wallet:
    Pool: Wallets@Broker
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg|$wallet.PublicKey


# Add the titles
- MERGE >> $chats:
    Lists: 
        CHATS: $wallet.Chats
        DOMAINS: $translations.Domains
    Match: 
        CHATS.Host: DOMAINS.Domain
    Output: 
        Chat: CHATS.Chat
        Host: CHATS.Host
        Host$: DOMAINS.Translation

# Respond
- REEL:
    Chats: $chats
```

| [Command ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| ⏬ [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) | Get the [Wallet 🪣 item](<../🤵🪣 Broker tables/🤵🪣 Wallets.md>)
| 🧬 [`MERGE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/MERGE 🧬 lists.md>) | Add the translations to the dataset
| 📬 [`SEND`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) | Call [`Translate@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| 🎣 [`REEL`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/REEL 🎣.md>) | Respond to the [Synchronous Request 🚀](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Request Sync 🚀.md>)
| 🔐 [`VERIFY`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>) | Verify the  [Signature 🔏](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Signatures 🔏.md>) of the [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>)
|

Needs ||
|-|-
| [Messages 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`translate@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Datasets 🪣](<🪣 Dataset.md>) | [`Wallets` 🪣](<../🤵🪣 Broker tables/🤵🪣 Wallets.md>)
|