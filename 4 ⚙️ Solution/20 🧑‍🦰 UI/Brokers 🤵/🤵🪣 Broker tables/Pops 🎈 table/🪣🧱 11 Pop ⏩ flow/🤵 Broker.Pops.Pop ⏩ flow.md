# 🤵 Broker.Pops.Pop ⏩ flow

> About
* Part of the [`Broker.Pops` 🪣 table](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
* Allows users to summon the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) for contextualized actions.

<br/>

## Diagram

![alt text](<🤵 Broker.Pops.Pop ⚙️ uml.png>)

Step | Purpose |
|-|-
|[`Pop@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 🐌 msg.md>)| [Wallet 🧑‍🦰 apps](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) summon their [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)
| [`Pop@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Pop 🧑‍🦰🐌🤵/🤵 Pop 📃 handler.md>) | Inserts into the [`Broker.Pops` 🪣 table](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>)
| [`OnPopInserted` 🔔 handler](<../🪣🧱 12 Pop 🔔 event/🤵 OnPopInserted 🔔 handler.md>) | Inserts into the [`Broker.Chats` 🪣 table](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>)
| [`OnChatInserted` 🔔 handler](<../../Chats 💬 table/🪣🧱 11 Asked 🔔 event/🤵 OnChatAsked 🔔 handler.md>) | Calls [`Open@Notifier` 🐌 msg](<../../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>)
| [`Open@Notifier` 🐌 msg](<../../../../Notifiers 📣/📣📨 Notifier msgs/Chats 💬 Open 🤵🐌📣/📣 Open 🐌 msg.md>) | [Wallet 🧑‍🦰 app](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) endpoint to open [Chats 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)
| [`Opened@Broker` 🐌 msg](<../../../🤵📨 Broker msgs/Chats 💬 Opened 🧑‍🦰🐌🤵/🤵 Opened 🐌 msg.md>) | Tells [Broker 🤵 domains](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) that a [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) is ready
|[`Opened@Broker` 📃 handler](<../../../🤵📨 Broker msgs/Chats 💬 Opened 🧑‍🦰🐌🤵/🤵 Opened 📃 handler.md>) | Marks the [`Broker.Chats`](<../../Chats 💬 table/🪣 Chats/🤵 Broker.Chats 🪣 table.md>) item as opened
| [`OnChatOpened` 🔔 handler](<../../Chats 💬 table/🪣🧱 14 Opened 🔔 event/🤵 OnChatOpened 🔔 handler.md>) | Adds the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>) to [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants
| [`OnChatterPop` 🔔 handler](<../../Chatters 👥 table/🪣🧱 11 Pop 🔔 event/🤵 OnChatterPop 🔔 handler.md>) | Marks the [`Broker.Pops`](<../🪣 Pops/🤵 Broker.Pops 🪣 table.md>) item as opened
|