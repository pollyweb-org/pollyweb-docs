# 🤵 Broker.Chats.Open ⏩ flow

> About
* Part of the [`Broker.Chats` 🪣 table](<../🪣 Chats/🤵 Broker.Chats 🪣 table.md>)

<br/>

## Diagram

![alt text](<🤵 Broker.Chats.Open ⚙️ uml.png>)

<br/>

## State Transitions


|| [State 🛢](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 State.md>) | Blame | Next action | Details
|-|-|-|-|-
||[`ASKED`](<../🪣🧱 11 Asked 🔔 event/🤵 OnChatAsked 🔔 handler.md>) |[`Locate` 🐌](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 📃 handler.md>)| [`Resolve@Printer` 🚀](<../../../../../45 🤲 Helper domains/Printers 🖨️/🖨️🅰️ Printer methods/Resolve 👥🚀🖨️/🖨️ Resolve 📃 handler.md>) | Inserted
||[`RESOLVED`](<../🪣🧱 12 Resolved 🔔 event/🤵 OnChatResolved 🔔 handler.md>) || [`About@Graph` 🚀](<../../../../../45 🤲 Helper domains/Graphs 🕸/🕸🅰️ Graph methods/👥🚀🕸 About/🕸 About 📃 handler.md>) | Final [Locator 🔆](<../../../../../25 🔆 Locators/Locators 🔆/🔆 Locator.md>)
||[`DETAILED`](<../🪣🧱 13 Detailed 🔔 event/🤵 OnChatDetailed 🔔 handler.md>) || [`Open@Notifier` 🐌](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) | With translations
||[`OPENED`](<../🪣🧱 14 Opened 🔔 event/🤵 OnChatOpened 🔔 handler.md>) | [`Opened` 🐌](<../../../🤵🅰️ Broker methods/Chats 💬 Opened 🧑‍🦰🐌🤵/🤵 Opened 📃 handler.md>) | [`Present@Finder` 🐌](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎🅰️ Finder methods/Present 🤵🐌🔎/🔎 Present 🐌 msg.md>) | Open on [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
||[`PRESENTED`](<../🪣🧱 15 Presented 🔔 event/🤵 OnChatPresented 🔔 handler.md>) | [`Presented` 🐌](<../../../🤵🅰️ Broker methods/Chats 💬 Presented 🔎🐌🤵/🤵 Presented 📃 handler.md>) | [`Prompt@Notifier` 🐌](<../../../🤵🅰️ Broker methods/Chats 💬 Prompt 🤗🐌🤵/🤵 Prompt 🐌 msg.md>) |With  [Finder 🔎](<../../../../../50 🫥 Agent domains/Finders 🔎/🔎 Finder agent/🔎 Finder 🫥 agent.md>) intro
||[`ACTIVATED`](<../🪣🧱 16 Activated 🔔 event/🤵 OnChatActivated 🔔 handler.md>)|| [`Hello@Host` 🐌](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗🅰️ Host methods/Hello 🤵🐌🤗/🤗 Hello 🐌 msg.md>) | With [Broker 🤵](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) intro
|
