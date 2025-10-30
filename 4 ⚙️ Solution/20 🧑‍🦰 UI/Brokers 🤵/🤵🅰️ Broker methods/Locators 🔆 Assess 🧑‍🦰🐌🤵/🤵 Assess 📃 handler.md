# 🤵📃 Assess@Broker

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/...commands ⌘/Script 📃/📃 Script.md>) that implements the [`Assess@Broker` 🅰️ method](<🤵 Assess 🐌 msg.md>)

<br/> 

## Script

```yaml
📃 Access@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    AllOf: Locator, Hook
    Texts: Locator 
    UUIDs: Hook

# Get the Wallet item
- GET >> $wallet:
    Set: BrokerWallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Parse the locator
- PARSE >> $locator:
    Locator: $.Msg.Body.Locator

# Resolve any ALIAS locator
- IF|$locator.IsAlias:

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
- RUN|Converse:
    Wallet: $wallet
    Locator: $locator

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
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/...commands ⌘/Command ⌘/⌘ Command.md>)  | [`$.Msg`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/...datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`IF`](<../../../../35 💬 Chats/Scripts 📃/...control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PARSE`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...holders 🧠/PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`RUN`](<../../../../35 💬 Chats/Scripts 📃/...control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Talkers 😃/😃⚙️ Talker cmds/...messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)    | [`Wallets` 🪣](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message.md>) | [`Resolve@Printer` 🅰️](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Resolve 👥🚀🖨️/🖨️ Resolve 🚀 request.md>) <br/>[`Introduce@Finder` 🅰️](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/🤵🐌🔎 Introduce.md>)
| [Schemas 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)   | [`ALIAS` 🧩](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
[Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/...commands ⌘/Script 📃/📃 Script.md>) | [`Converse` 📃 script](<../../🤵⏩ Broker flows/Converse 🤵⏩💬/🤵 Converse 📃 script.md>)
| 