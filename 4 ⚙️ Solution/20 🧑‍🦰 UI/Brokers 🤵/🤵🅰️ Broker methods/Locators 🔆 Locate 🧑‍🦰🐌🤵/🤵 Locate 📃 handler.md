# 🤵📃 Locate@Broker

> [Script 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) that implements the [`Locate@Broker` 🅰️ method](<🤵 Locate 🐌 msg.md>)


## Flow

![alt text](<🤵 Locate ⚙️ uml.png>)


| # | Call | Notes
|-|-|-
| 1 | [👥🚀🖨️ `Resolve@Printer`](<../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Resolve 👥🚀🖨️/🖨️ Resolve 🚀 call.md>) | Get the underlying [Locator 🔆](<../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>) 
| 2 | [🤵⏩🧑‍🦰 Open 🔆](<../../🤵⏩ Broker flows/Open 🤵⏩💬/🤵 Open ⏩ flow.md>) | Ask [Wallets 🧑‍🦰](<../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)  to open a chat window
| 3 | [🔎⏩🧑‍🦰 Present 🤗](<../../../../50 🫥 Agent domains/Finders 🔎/🔎⏩ Finder flows/Present 🔎⏩🧑‍🦰/🔎 Present ⏩ flow.md>) | Ask [Finders 🔎](<../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) to introduce [Hosts 🤗](<../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>)
||




<br/> 

## Script

```yaml
📃 Locate@Broker:

# Verify the required inputs
- ASSERT|$.Msg:
    AllOf: Locator, Hook
    Texts: Locator 
    UUIDs: Hook

# Get the Wallet item
- READ >> $wallet:
    Set: Broker.Wallets
    Key: $.Msg.From

# Verify the signature
- VERIFY|$.Msg:
    Key: $wallet.PublicKey

# Parse the locator
- RUN|Resolve-Alias >> $locator:
    Locator: $.Msg.Body.Locator
```

> Continues on the [`Present@Finder` 📃 handler](<../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 📃 handler.md>)


<br/>

| Uses | |
|-|-
| [Commands ⌘](<../../../../35 💬 Chats/Scripts 📃/Command ⌘.md>)  | [`$.Msg`](<../../../../37 Scripts 📃/📃 Holders 🧠/🧠 System holders/$.Msg 📨/📨 $.Msg 🧠 holder.md>) [`READ`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) [`IF`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/IF ⤵️/⤵️ IF ⌘ cmd.md>) [`PARSE`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for holders 🧠/PARSE 🔆/🔆 PARSE ⌘ cmd.md>) [`RUN`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for control ▶️/RUN 🏃/🏃 RUN ⌘ cmd.md>) [`SEND`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/SEND 📬/📬 SEND ⌘ cmd.md>) [`VERIFY`](<../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for messages 📨/VERIFY 🔐/🔐 VERIFY ⌘ cmd.md>)
| [Datasets 🪣](<../../../../30 🧩 Data/Datasets 🪣/🪣 Dataset.md>)    | [`Wallets` 🪣](<../../🤵🪣 Broker tables/Wallets 🧑‍🦰 table/🤵 Broker.Wallets 🪣 table.md>)
[Scripts 📃](<../../../../35 💬 Chats/Scripts 📃/Script 📃.md>) | [`Resolve Alias` 📃 script](<📃 Resolve Alias/🤵 Resolve Alias 📃 script.md>)   <br/> [`Save Chat` 📃 script](<📃 Save Chat/🤵 Save Chat 📃 script.md>)
| 