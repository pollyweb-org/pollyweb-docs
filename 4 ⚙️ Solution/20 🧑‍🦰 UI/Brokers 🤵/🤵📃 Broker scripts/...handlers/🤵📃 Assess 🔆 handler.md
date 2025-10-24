# 🤵📃 Assess@Broker

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/📃 Script.md>) that implements the [`Assess@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/2 🤵🅰️ Locators/🧑‍🦰🐌🤵 Assess.md>)

<br/>

## Script

```yaml
📃 Access@Broker:

# Verify the required inputs
- ASSERT:
    - $.Msg.Locator
    - $.Msg.Hook

# Get the Wallet item
- GET >> $wallet:
    Set: Wallets@Broker
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Parse the locator
- PARSE >> $locator:
    Locator: $.Msg.Body.Locator

# Resolve any ALIAS locator
- IF|$locator.IsAlias:
    Then: 

        # Send the request to the Printer
        - SEND >> $resolved:
            To: $locator.Host
            Subject: Resolve@Printer
            Locator: $.Msg.Locator

        # Parse the locator again
        - PARSE >> $locator:
            Locator: $resolved

# Open a Chat on the Wallet app
- RUN|Converse
```

> Calls the [`Converse` 📃 script](<../...procedures/🤵📃 Converse ⏩.md>)

```yaml
# Ask Finders to introduce Hosts
- SEND:
    To: $wallet.Finder
    Subject: Introduce@Finder
    Chat: $chat.Chat
    Host: $chat.Chat
```

> Continues on [🔎⏩🧑‍🦰 Introduce 🤗](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>)


<br/>

| Uses | |
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/⌘ Command.md>)  | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages/$.Msg 📨.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET ⏬ item.md>) [`IF`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... control ▶️/IF ⤵️.md>) [`PARSE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... placeholders 🧠/PARSE 🔆.md>) [`RUN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/... control ▶️/RUN ▶️.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages/SEND 📬 msg.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages/VERIFY 🔐 msg.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)    | [`Wallets`](<../../🤵🪣 Broker tables/🤵🪣 Wallets table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Resolve@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/👥🚀🖨️ Resolve.md>)
| [Schemas 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)   | [`ALIAS` 🧩](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
| 