# ▶️ Assess@Broker

> [Script 📃](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/📃 Script.md>) that implements [`Assess@Broker` 🅰️](<../🤵🅰️ Broker methods/2 🤵🅰️ Locators/🧑‍🦰🐌🤵 Assess.md>)


<br/>

## Script

```yaml
▶️ Access@Broker:

# Get the Wallet item
- GET|Wallets@Broker|$.Msg.From >> $wallet

# Verify the signature
- VERIFY|$.Msg|$wallet.PublicKey

# Parse the locator
- PARSE|$.Msg.Body.Locator >> $locator

# Resolve any ALIAS locator
- IF|$locator.IsAlias:
    Then: 
        # Send the request to the Printer
        - SEND >> $resolved:
            To: $locator.Host
            Subject: Resolve@Printer
            Locator: $.Msg.Locator
        # Parse the locator again
        - PARSE|$resolved >> $locator

# Open a Chat on the Wallet app
- RUN|⏩ Converse
```

> Calls [🤵⏩🧑‍🦰 Converse 💬](<../🤵⏩ Broker flows/🤵⏩🧑‍🦰 Converse 💬.md>)

```yaml
# Ask Finders to introduce Hosts
- SEND:
    To: $wallet.Finder
    Subject: Introduce@Finder
    Chat: $chat.Chat
    Host: $chat.Chat
```

> Continues on [🔎⏩🧑‍🦰 Introduce 🤗](<../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>)


<br/>

| [Command ⌘](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/⌘ Command.md>) | Purpose
|-|-
| 📨 [`$.Msg`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/$.Msg 📨.md>) | Read the incoming [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>)
| ⏬ [`GET`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for data/GET ⏬ item.md>) | Get the [Wallet 🪣 item](<../🤵🪣 Broker tables/🤵🪣 Wallets.md>)
|⤵️ [`IF`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for control/IF ⤵️.md>) |Verify if it is an [ALIAS 🧩 locator](<../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
| 📬 [`SEND`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for flows/.SEND 📬 msg.md>) | Call [`Translate@Graph`](<../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 Translate.md>)
| 🔆 [`PARSE`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/PARSE 🔆.md>) | Parse the [Locator 🔆](<../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
| 🔐 [`VERIFY`](<../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/for handlers/VERIFY 🔐 msg.md>) | Verify the  [Signature 🔏](<../../../30 🧩 Data/Messages 📨/📨⏩ Message flows/Signatures 🔏.md>) of the [Message 📨](<../../../30 🧩 Data/Messages 📨/📨 Message.md>)
|