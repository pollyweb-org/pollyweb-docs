# 🤵📃 Assess@Broker

> [Script 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Assess@Broker` 🅰️ method](<../../🤵🅰️ Broker methods/Locators 🔆 Assess 🧑‍🦰🐌🤵/🤵 Assess 🐌 msg.md>)

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
            Header:
                To: $locator.Host
                Subject: Resolve@Printer
            Body:
                Locator: $.Msg.Locator

        # Parse the locator again
        - PARSE >> $locator:
            Locator: $resolved

# Open a Chat on the Wallet app
- RUN|Converse

# Ask Finders to introduce Hosts
- SEND:
    Header:
        To: $wallet.Finder
        Subject: Introduce@Finder
    Body:
        Chat: $chat.Chat
        Host: $chat.Chat
```

> Continues on [🔎⏩🧑‍🦰 Introduce 🤗](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/🔎⏩🧑‍🦰 Introduce 🤗.md>)


<br/>

| Uses | |
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Command ⌘/Command ⌘.md>)  | [`$.Msg`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/$.Msg 📨.md>) [`GET`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...datasets 🪣/GET/GET ⏬ item.md>) [`IF`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/IF ⤵️/IF ⤵️.md>) [`PARSE`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...placeholders 🧠/PARSE 🔆.md>) [`RUN`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...control ▶️/RUN ▶️/RUN ▶️.md>) [`SEND`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/SEND 📬 msg.md>) [`VERIFY`](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐 msg.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)    | [`Wallets` 🪣](<../../🤵🪣 Broker tables/🤵 Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Resolve@Printer` 🅰️](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/👥🚀🖨️ Resolve.md>) <br/>[`Introduce@Finder` 🅰️](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/🤵🐌🔎 Introduce.md>)
| [Schemas 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)   | [`ALIAS` 🧩](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
[Scripts 📃](<../../../../35 💬 Chats/😃 Talkers/😃⚙️ Talker cmds/...commands ⌘/Script 📃/📃 Script.md>) | [`Converse` 📃 script](<../🤵 Converse 🤵⏩💬/Converse 📃 script.md>)
| 