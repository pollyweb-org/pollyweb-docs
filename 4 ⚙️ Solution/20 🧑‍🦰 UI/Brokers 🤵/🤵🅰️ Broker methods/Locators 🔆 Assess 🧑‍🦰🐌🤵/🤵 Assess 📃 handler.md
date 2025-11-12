# 🤵📃 Assess@Broker

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Assess@Broker` 🅰️ method](<🤵 Assess 🐌 msg.md>)


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
📃 Assess@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    AllOf: Locator, Hook
    Texts: Locator 
    UUIDs: Hook

# Get the Wallet item
- READ >> $wallet:
    Set: BrokerWallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Parse the locator
- RUN|Resolve-Alias >> $locator:
    Locator: $.Msg.Body.Locator

# Open a Chat on the Wallet app
- RUN|Converse@Broker >> $chat:
    Wallet: $wallet
    Locator: $locator

# Ask Finders to introduce Hosts
- RUN|Call-Introduce:
    wallet: $wallet
    chat: $chat
    locator: $locator
```

> Continues on the [`Introduce@Finder` 📃 handler](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Introduce 🤵🐌🔎/🔎 Introduce 📃 handler.md>)


<br/>

| Uses | |
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PARSE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN ▶️/▶️ RUN ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)    | [`Wallets` 🪣](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 BrokerWallets 🪣 table.md>)
[Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`Resolve Alias` 📃 script](<scripts/🤵 Resolve Alias 📃 script.md>) <br/> [`Call Converse` 📃 script](<scripts/🤵 Call Converse 📃 script.md>) <br/> [`Call Introduce` 📃 script](<scripts/🤵 Call Introduce 📃 script.md>) <br/> [`Save Chat` 📃 script](<scripts/🤵 Save Chat 📃 script.md>)
| 