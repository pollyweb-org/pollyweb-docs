# 🤵📃 Converse ⏩

> [Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements [🤵⏩🧑‍🦰 Converse 💬](<../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Converse 💬.md>)

<br/>

## Script

Assume `$wallet` and `$locator` placeholders from [🤵😃 `Assess` 🐌](<🤵📃 Assess 🐌.md>).

> Continues from the [`Assess` 📃 script](<🤵📃 Assess 🐌.md>)


```yaml
📃 Converse:

# Get the default Graph from settings
- GET >> $graph
    Pool: Settings@Hoster
    Key: Graph

# Get the Chat details from the Graph
- SEND >> $domain:
    To: $graph
    Subject: Identity@Graph
    Domain: $locator.Host

# Save the Host info
- SAVE|Hosts@Broker >> $host:
    Host: $domain.Domain
    Host$: $domain.Name
    SmallIcon: $domain.SmallIcon
    BigIcon: $domain.BigIcon

# Get the translation for the language
- SEND >> $translation:
    To: $graph
    Subject: Translate@Graph
    Language: $wallet.Language
    Domain: $locator.Host

# Create a new key pair
- KEYS >> $keys

# Create a new Chat
- SAVE|Chats@Broker >> $chat:
    Chat: {.UUID}
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
    To: $wallet.Notifier
    Subject: Converse@Notifier
    Wallet: $chat.Wallet
    Hook: $.Msg.Hook
    Chat: $chat.Chat
    PrivateKey: $keys.PrivateKey
    Host: $chat.Host
    Host$: $chat.Host$
    SmallIcon: $host.SmallIcon
    BigIcon: $host.BigIcon

# Update the Chats
- RUN|⏩ UpdateChats
```


> Continues on [🤵⏩🧑‍🦰 Update Chats 💬](<../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Update Chats 💬.md>)

|Needs | |
|-|-
| ⌘ Commands | [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) [`KEYS`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/KEYS 🔑.md>) [`SAVE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/SAVE 💾 item.md>) [`SEND`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) [`RUN`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/RUN ▶️.md>)
| 🅰️ Methods | [`Converse@Notifier`](<../../Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>) <br/>  [`Identity@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>)  <br/> [`Translate@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| {{Placeholder}} | [`$.Settings`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Settings 🎛️.md>)
| 📃 Scripts |[`UpdateChats`](<🤵📃 Update Chats 💬.md>)
| 🪣 Tables | [`Chats`](<../🤵🪣 Broker tables/🤵🪣 Chats.md>) [`Hosts`](<../🤵🪣 Broker tables/🤵🪣 Hosts.md>)
|