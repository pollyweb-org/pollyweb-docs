# 🤵📃 Converse 💬

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Converse` ⏩ flow](<🤵 Converse ⏩ flow.md>)

<br/>

## Script

> Assumes `$wallet` and `$locator` placeholders from the [`Assess` 📃 script](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 📃 handler.md>).

> Continues from the [`Assess` 📃 script](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 📃 handler.md>)

<!-- TODO: Change the ASSERT -->

```yaml
📃 Converse:

- ASSERT:
    - $wallet
    - $locator

# Get the Host details from the Graph
- SEND >> $domain:
    Header:
        To: $.Settings.Graph
        Subject: Identity@Graph
    Body:
        Domain: $locator.Host

# Save the Host info
- SAVE|BrokerDomains:
    Domain: $domain.Domain
    Domain$: $domain.Name
    SmallIcon: $domain.SmallIcon
    BigIcon: $domain.BigIcon

# Get the translation for the language
- SEND >> $translation:
    Header:
        To: $.Settings.Graph
        Subject: Translate@Graph
    Body:
        Language: $wallet.Language
        Domain: $locator.Host

# Create a new key pair
- KEYS >> $keys

# Create a new Chat
- SAVE|BrokerChats >> $chat:
    Chat: .UUID()
    Wallet: $wallet.Wallet
    # Host info
    Host: $locator.Host
    Host$: $translation.Domain
    # Locator info
    Key: $locator.Key
    Parameters: $locator.Parameters
    # For Wallets to sign messages
    PrivateKey: $keys.PrivateKey
    # For domains to verify Wallet messages
    PublicKey: $keys.PublicKey     

# Open the Chat in the Wallet app
- SEND:
    Header:
        To: $wallet.Notifier
        Subject: Converse@Notifier
    Body:
        Wallet: $chat.Wallet
        Hook: $.Msg.Hook
        Chat: $chat.Chat
        PrivateKey: $keys.PrivateKey
        Host: $chat.Host
        Host$: $chat.Host$
        SmallIcon: $domain.SmallIcon
        BigIcon: $domain.BigIcon

# Update the Chats
- RUN|UpdateChats:
    wallet: $wallet
```


> Continues on [`UpdateChats` 📃 script](<../Update Chats 🤵⏩💬/🤵 Update Chats 📃 script.md>)

|Needs | |
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/⌘ Command.md>) | [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`KEYS`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/KEYS 🔑/🔑 KEYS ⌘ cmd.md>) [`SAVE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`RUN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Converse@Notifier`](<../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Converse 🤵🐌📣/📣 Converse 📣 msg.md>) <br/>  [`Identity@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)  <br/> [`Translate@Graph`](<../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| [Placeholders 🧠](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/$Placeholder 🧠.md>) | [`$.Settings`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Settings 🎛️.md>)
| [Scripts 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) |[`UpdateChats`](<../Update Chats 🤵⏩💬/🤵 Update Chats 📃 script.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>) | [`BrokerChats` 🪣](<../../🤵🪣 Broker tables/Chats 💬 table/🤵 BrokerChats 🪣 table.md>) [`BrokerDomains` 🪣](<../../🤵🪣 Broker tables/Domains 👥 table/🤵 BrokerDomains 🪣 table.md>)
|