# 🤵🪣 Chats @ Broker table

> Implements the [Broker 🤵 domain](<../../../🤵 Broker helper/🤵 Broker 🤲 helper.md>)

> Stores [Chats 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>)



## Schema

Here's the [Itemized 🛢 schema](<../../../../../30 🧩 Data/Datasets 🪣/🪣🔣 Dataset types/Itemized 🛢 dataset.md>).

```yaml
# Chats.yaml
Prefix: Broker
Table: Chats
Key: ID

Parents:
    Wallet: { Wallets.ID: Chats.Wallet }
    Host: { Domains.Name: Chats.Host }

Propagate:
    - Host

Children:
    Chatters: { Chatters.Chat: Chats.ID }

Handlers:
    OnChatChanges: ALTERED                   # call Updated@Notifier
    OnChatCreated: CREATED                   # call Translate@Graph
    OnChatLocated: CREATED > LOCATED         # call Open@Notifier
    OnChatOpened: LOCATED > OPENED           # call Present@Finder
    OnChatPresented: OPENED > PRESENTED      # call Hello@Host
    OnChatTerminated: PRESENTED > TERMINATED # call Terminated@Host
    OnChatWrapped: PRESENTED > WRAPPED

Handlers:

    OnChatTerminated:       # On Join@Broker + Terminate
        Events: UPDATED     # >> call Terminated@Host
        Assert: 
            New.Status: TERMINATED

    OnChatWrapped:          # On Wrap@Broker
        Events: UPDATED     # >> call @Advertise
        Assert:
            New.Status: WRAPPED
```

## Links

| Link | Table | Contains
|-|-|-
| Parents   | [`Wallets` 🪣](<../../Wallets 🧑‍🦰 table/🪣 Wallets/🤵 Broker.Wallets 🪣 table.md>) | [Wallets 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>)
|           | [`Domains` 🪣](<../../Domains 👥 table/🪣 Domains/🤵 Broker.Domains 🪣 table.md>) | [domains 👥](<../../../../../40 👥 Domains/👥 Domain/👥 Domain.md>)
| Children | [`Chatters` 🪣](<../../Chatters 👥 table/🪣 Chatters/🤵 Broker.Chatters 🪣 table.md>) | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) participants


## Handlers

| [Handler 🔔](<../../../../../30 🧩 Data/Datasets 🪣/🪣🛢 Itemized datasets/Item 🛢 Handlers.md>) | [Message 📨](<../../../../../30 🧩 Data/Messages 📨/📨 Message/📨 Message.md>)
|-|-
|[`OnChatChanges` 📃](<../🪣🔔 on Altered/🤵 OnChatAltered 📃 handler.md>) | [`Update@Notifier` 🅰️ ](<../../../../Notifiers 📣/📣🅰️ Notifier methods/Wallets 🧑‍🦰 Updated 🤵🐌📣/📣 Updated 🐌 msg.md>)


## Example

Here's the [`READ` command](<../../../../../37 Scripts 📃/📃 Commands ⌘/⌘ for datasets 🪣/READ 🧲/🧲 READ ⌘ cmd.md>) result.

```yaml
# READ|Chats|<chat-id>

ID: <chat-uuid>

# Wallet info
Wallet: <wallet-uuid>

# To change the language of the chat
Language: en-us

# Host info
Host: any-host.dom
Host$: Any Host
Emoji: 😃

# For Wallets to sign messages
PrivateKey: <PrivateKey>

# For domains to verify Wallet messages
PublicKey: <PublicKey>

# Origin chat (if any)
Origin: <origin-chat-uuid>
```

Property|Type|Details|Origin|Purpose
|-|-|-|-|-
|`ID`|uuid | [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) ID |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Wallet`| uuid | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) ID | [`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Host` | text | [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) name |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Host$`|text | [Host 🤗](<../../../../../41 🎭 Domain Roles/Hosts 🤗/🤗 Host role/🤗🎭 Host role.md>) title |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Emoji`|text | [Manifest 📜](<../../../../../30 🧩 Data/Manifests 📜/📜 Manifest/📜 Manifest.md>) emoji |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chats@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`PublicKey` | text | [Wallet 🧑‍🦰](<../../../../Wallets 🧑‍🦰/🧑‍🦰 Wallet app/🧑‍🦰 Wallet 🛠️ app.md>) verification |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>)| [`Chat@`](<../../../🤵🅰️ Broker methods/Wallets 🧑‍🦰 Frontend 🧑‍🦰🚀🤵/🤵 Frontend 🚀 call.md>)
|`Origin` | uuid | Parent [Chat 💬](<../../../../../35 💬 Chats/Chats 💬/💬 Chat.md>) |[`Locate@`](<../../../🤵🅰️ Broker methods/Locators 🔆 Locate 🧑‍🦰🐌🤵/🤵 Locate 🐌 msg.md>) | [`Presented@`](<../../../🤵🅰️ Broker methods/Chats 💬 Presented 🔎🐌🤵/🤵 Presented 🐌 msg.md>)
|