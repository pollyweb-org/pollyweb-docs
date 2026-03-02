# 🤵🪣 Frontend @ Broker table

> About
* Implements the [Broker 🤵 domain](<../../../🤵/🤵 Broker 🤲 helper.md>)
* [Itemized 🪣 dataset](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>) that manages CQRS projections for [Notifier 📣 domains](<../../../../Notifiers 📣/📣/📣 Notifier 👥 domain.md>)
* Supports the [`Frontend@Broker` 📨 msg](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)

<br/>

## Diagram

![alt text](<🤵 Broker.Frontend ⚙️ uml.png>)

<br/>

## Data access

|Actor|[`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>)|[`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | Purpose
|-|:-:|:-:|-|
|[`OnWalletAltered` 🔔](<../../Wallets 🧑‍🦰 table/🪣🧱 00 Altered 🔔 event/🤵 OnWalletAltered 🔔 handler.md>)|X|X| Updates `Wallet` projections
|[`OnBindAltered` 🔔](<../../Binds 🔗 table/🪣🧱 00 Altered 🔔 event/🤵 OnBindAltered 🔔 handler.md>)|X|X| Updates `Binds` projections
|[`OnChatAltered` 🔔](<../../Chats 💬 table/🪣🧱 0 Altered 🔔 event/🤵 OnChatAltered 🔔 handler.md>)|X|X| Updates `Chats` projections
|[`OnTokenAltered` 🔔](<../../Tokens 🎫 table/🪣🧱 00 Altered 🔔 event/🤵 OnTokenAltered 🔔 handler.md>)|X|X| Updates `Tokens` projections
|[`OnDomainAltered` 🔔](<../../Domains 👥 table/🪣🧱 0 Altered 🔔 event/🤵 OnDomainAltered 🔔 handler.md>)|X|X| Updates `Domain` projections
|[`OnSchemaAltered` 🔔](<../../Schemas 🧩 table/🪣🔔 Altered/🤵 OnSchemaAltered 🔔 handler.md>)|X|X| Updates `Schema` projections
|[`OnFrontendAltered` 🔔](<../🪣🔔 Altered/🤵 OnFrontendAltered 🔔 handler.md>) |X|| Calls [`Updated@Notifier`](<../../../../Notifiers 📣/📣📨 Notifier msgs/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)
|[`Frontend@Broker` 📃](<../../../🤵📨 Broker msgs/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 📃 handler.md>)  |X|| Called by [Wallet 🧑‍🦰 apps](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
Prefix: Broker
Table: Frontend
Key: Wallet
```

<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# From OnWalletAltered
Wallet: <wallet-uuid>
Language: en-us
PublicKey: <public-key>

Chats: {...}    # From OnChatAltered
Binds: {...}    # From OnBindAltered
Tokens: {...}   # From OnTokenAltered
Domains: {...}  # From OnDomainAltered
Schemas: {...}  # From OnSchemaAltered
```