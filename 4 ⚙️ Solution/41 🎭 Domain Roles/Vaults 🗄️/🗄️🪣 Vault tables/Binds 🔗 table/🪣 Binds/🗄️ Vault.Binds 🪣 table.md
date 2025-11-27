# 🗄️ Vault.Binds 🪣 table

> About
* Stores the content of the [`Bound@Vault` 🅰️ method](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>)

<br/>

## Data Access

| Action | [`READ`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) | [`SAVE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/SAVE 💾/💾 SAVE ⌘ cmd.md>) | [`DELETE`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/DELETE 🗑️/🗑️ DELETE ⌘ cmd.md>) |
|-|:-:|:-:|:-:|
| [`BIND` 📃 script](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND 📃 script.md>) |  | X |  |
| [`Bound` 📃 handler](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 📃 handler.md>) | X | X |  |
| [`Unbound` 📃 handler](<../../../🗄️🅰️ Vault methods/Unbound 🤵🐌🗄️/🗄️ Unbound 📃 handler.md>) | X | X |  |
|


<br/>

## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).


```yaml
Prefix: Vault
Table: Binds
Item: Bind
```


<br/>

## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# Automatic
ID: <bind-id>

# From BIND command
Chat: <chat-id>             # Chat where the Bind was offered
Broker: any-broker.dom      # Broker owning the Chat
Schema: .BIND               # Schema offered
Reference: <reference>      # Hosted domain internal anchor 
Internals: {...}            # Hosted domain internal data 

# From Bound@Vault
Answer: ACCEPTED|DECLINED     # User answer to the offer
```

| Property | Type | Details | From | Purpose |
|-|-|-|-|-
| `ID` | uuid | [Bind 🔗](<../../../../../30 🧩 Data/Binds 🔗/🔗 Bind.md>) ID |  | [`Bind@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>) |
| `Chat` | uuid | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID | [`$.Chat`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) | [`Bind@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
| `Broker` |text| [Broker 🤵 domain](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵 Broker helper/🤵 Broker 🤲 helper.md>) | [`$.Chat`](<../../../../../37 Scripts 📃/📃 Holders 🧠/System holders 🔩/$.Chat 💬/💬 $.Chat 🧠 holder.md>) | [`Bind@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
| `Schema` |text| [Schema Code 🧩](<../../../../../30 🧩 Data/Codes 🧩/🧩 Schema Code.md>) | [`BIND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) | [`Bind@Broker`](<../../../../../20 🧑‍🦰 UI/Brokers 🤵/🤵🅰️ Broker methods/Binds 🔗 Bind 🗄️🐌🤵/🤵 Bind 🐌 msg.md>)
| `Reference` | text | [Hosted 📦](<../../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) internal anchor | [`BIND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) | [`ASYNC`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>)
| `Internals` | map | [Hosted 📦](<../../../../../55 👷 Build domains/Hosteds 📦/📦👥 Hosted domain.md>) internal data | [`BIND`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for methods 🤵/BIND 🔗/🔗 BIND ⌘ cmd.md>) | [`ASYNC`](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for async/ASYNC 👷🏼/👷🏼 ASYNC ⌘ cmd.md>)
| `Answer` | enum | `ACCEPTED` `DECLINED` | [`Bound@`](<../../../🗄️🅰️ Vault methods/Bound 🤵🐌🗄️/🗄️ Bound 🐌 msg.md>) | 
|