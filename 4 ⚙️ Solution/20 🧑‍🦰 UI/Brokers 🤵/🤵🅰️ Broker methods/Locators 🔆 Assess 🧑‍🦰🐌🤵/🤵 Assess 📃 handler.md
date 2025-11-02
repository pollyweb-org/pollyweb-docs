# 🤵📃 Assess@Broker

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) that implements the [`Assess@Broker` 🅰️ method](<🤵 Assess 🐌 msg.md>)


## Flow

![alt text](<🤵 Assess ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🚀🖨️ `Resolve@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Resolve 👥🚀🖨️/🖨️ Resolve 🚀 request.md>) | Get the underlying [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) 
| 2 | [🤵⏩🧑‍🦰 Converse 🔆](<../../🤵⏩ Broker flows/Converse 🤵⏩💬/🤵 Converse ⏩ flow.md>) | Ask [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  to open a chat window
| 3 | [🔎⏩🧑‍🦰 Introduce 🤗](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/Introduce 🔎⏩🧑‍🦰/🔎 Introduce ⏩ flow.md>) | Ask [Finders 🔎](<../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) to introduce [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)
||




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
- RUN|Converse@Broker >> $chat:
    Wallet: $wallet
    Locator: $locator

# Ask Finders to introduce Hosts
- SEND:
    Header:
        To: $wallet.Finder
        Subject: Introduce@Finder
    Body:
        Chat: $chat.Chat
        Host: $locator.Host
        Language: $wallet.Language
        Reviewer: $wallet.Reviewer
```

> Continues on the [`Introduce@Finder` 📃 handler](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 📃 handler.md>)


<br/>

| Uses | |
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Command ⌘.md>)  | [`$.Msg`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`GET`](<../../../../35 💬 Chats/Scripts 📃/📃 datasets 🪣/GET 🧲/🧲 GET ⌘ cmd.md>) [`IF`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PARSE`](<../../../../35 💬 Chats/Scripts 📃/📃 holders 🧠/PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`RUN`](<../../../../35 💬 Chats/Scripts 📃/📃 control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>) [`SEND`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../35 💬 Chats/Scripts 📃/📃 messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)    | [`Wallets` 🪣](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Wallets 🪣 table.md>)
| [Messages 📨](<../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>) | [`Resolve@Printer` 🅰️](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Resolve 👥🚀🖨️/🖨️ Resolve 🚀 request.md>) <br/>[`Introduce@Finder` 🅰️](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 🐌 msg.md>)
| [Schemas 🧩](<../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>)   | [`ALIAS` 🧩](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🧩 Printer schemas/🧩 ALIAS.md>)
[Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/📃 basics/Script 📃.md>) | [`Converse` 📃 script](<../../🤵⏩ Broker flows/Converse 🤵⏩💬/🤵 Converse 📃 script.md>)
| 