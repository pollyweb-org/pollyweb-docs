# 🤵⏩🧑‍🦰 Converse @ Broker

> Part of [🤵⏩🧑‍🦰 Assess @ Broker](<🤵⏩🧑‍🦰 Assess 🔆.md>)

* Opens a new chat window in the app.

<br/>

## Flow diagram

![New chat](<../.📎 Assets/⚙️💬 Converse.png>)


| # | Call | Notes
|-|-|-|
| 1 | [👥🚀🕸 `Identity@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Identity.md>) | Get the Chat's name and icon
| 2 | [👥🚀🕸 `Translate@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>) | Get the Chat's title
| 3 | [🤵🐌📣 `Converse@Notifier`](<../../Notifiers 📣/📣🅰️ Notifier methods/2 💬 Chats/1 🤵🐌📣 Converse.md>) | Open a [💬 Chat](<../../../35 💬 Chats/💬 Chats/💬 Chat.md>) on the [Wallet 🧑‍🦰 app](<../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>)
| 4 | [🤵⏩🧑‍🦰 Update Chats 💬](<🤵⏩🧑‍🦰 Update Chats 💬.md>) | [Brokers 🤵](<../🤵🤲 Broker helper.md>) ask [Wallets 🧑‍🦰](<../../Wallets 🧑‍🦰/🧑‍🦰🛠️ Wallet app.md>) to reload
||

<br/>

## Resolver

Assume `$wallet` and `$locator` placeholders from [`Assess@Broker`](<../🤵🅰️ Broker methods/2 🤵🅰️ Locators/🧑‍🦰🐌🤵 Assess.md>).

> Continues from [`Assess@Broker`](<../🤵🅰️ Broker methods/2 🤵🅰️ Locators/🧑‍🦰🐌🤵 Assess.md>)


```yaml
⏩ Converse:

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
> Continues on [🤵⏩🧑‍🦰 Update Chats 💬](<🤵⏩🧑‍🦰 Update Chats 💬.md>)
